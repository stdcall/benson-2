import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The halving step in the proof of Theorem 7.4.1 (i)

Section 7.4, proof of Theorem 7.4.1 (i), p. 245.  `M` is a symplectic
space over a field `k` of odd characteristic with form `( , )`, `X` and `Y`
are isotropic, `z = x + y` with `x ∈ X`, `y ∈ Y` and `(x, y) = a ≠ 0`.
The book chooses `x' ∈ X` with `(x', y) = 0`, puts
`x₀ = ½(x + x')`, `x₀' = ½(x - x')`, chooses `y₀ ∈ Y` with
`(x₀, y₀) = 0` and `(x₀', y₀) = a/2`, puts `y₀' = y - y₀`, and claims
`(x₀ + y₀, x₀' + y₀') = (x₀, y₀') + (y₀, x₀') = a/2 - a/2 = 0` and
`z = (x₀ + y₀) + (x₀' + y₀')`, so that `ẑ` lies in the span of the hats of
the two isotropic 2-spaces `⟨x₀, y₀⟩` and `⟨x₀', y₀'⟩`.

Notation.  `B : V →ₗ[K] V →ₗ[K] K` is the form, alternating
(`halt : ∀ v, B v v = 0`), with `(2 : K) ≠ 0`.  Isotropy of `X` and `Y` is
used only through `hXX : B x x' = 0` and `hYY : B y₀ y = 0`; the choices of
`x'` and `y₀` are the hypotheses `hx'y`, `h0`, `h0'`.

* `antisymm`: an alternating form is antisymmetric.
* `halves_add`, `halves_sub`: `x₀ + x₀' = x`, `x₀ - x₀' = x'`.
* `isotropic_split`: `(x₀, y₀') = a/2`, `(y₀, x₀') = -a/2`,
  `(x₀ + y₀, x₀' + y₀') = 0`, `(x₀', y₀') = 0` (so `⟨x₀', y₀'⟩` is
  isotropic, as needed for the last inclusion of the proof) and
  `(x₀ + y₀) + (x₀' + y₀') = x + y`.
* `forced_zero`, `no_y0_of_xprime_zero`: when `X` is a line (`n = 1`) the only
  `x'` with `(x', y) = 0` is `0`, and then no `y₀` exists: the proof, and
  the theorem (see `checks/sage/chapter-7b.py`), need `n ≥ 2`.

Not covered: the existence of `y₀` for `n ≥ 2` (the pairing of `X` and `Y`
is perfect and `x₀`, `x₀'` are independent), and the passage from these
identities to `H₀(𝓕_M)`; `H₀(𝓕_M) = M` is computed for `Sp₄(𝔽₃)`,
`Sp₄(𝔽₅)`, `Sp₄(𝔽₇)`, `Sp₆(𝔽₃)` and the identities are checked for all
`z` of `Sp₄(𝔽₃)`, `Sp₄(𝔽₅)`, `Sp₆(𝔽₃)` in `checks/sage/chapter-7b.py`.
-/

namespace BensonCohomology.SymplecticHalving

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

theorem antisymm (B : V →ₗ[K] V →ₗ[K] K) (halt : ∀ v, B v v = 0) (u v : V) :
    B u v = -B v u := by
  have h := halt (u + v)
  simp only [map_add, LinearMap.add_apply, halt u, halt v] at h
  linear_combination h

theorem halves_add (h2 : (2 : K) ≠ 0) (x x' : V) :
    (2 : K)⁻¹ • (x + x') + (2 : K)⁻¹ • (x - x') = x := by
  have e : x + x' + (x - x') = (2 : K) • x := by rw [two_smul]; abel
  rw [← smul_add, e, smul_smul, inv_mul_cancel₀ h2, one_smul]

theorem halves_sub (h2 : (2 : K) ≠ 0) (x x' : V) :
    (2 : K)⁻¹ • (x + x') - (2 : K)⁻¹ • (x - x') = x' := by
  have e : x + x' - (x - x') = (2 : K) • x' := by rw [two_smul]; abel
  rw [← smul_sub, e, smul_smul, inv_mul_cancel₀ h2, one_smul]

theorem isotropic_split (B : V →ₗ[K] V →ₗ[K] K) (halt : ∀ v, B v v = 0)
    (h2 : (2 : K) ≠ 0) (x x' y y₀ : V) (a : K)
    (hXX : B x x' = 0) (hYY : B y₀ y = 0) (hxy : B x y = a) (hx'y : B x' y = 0)
    (h0 : B ((2 : K)⁻¹ • (x + x')) y₀ = 0)
    (h0' : B ((2 : K)⁻¹ • (x - x')) y₀ = a / 2) :
    B ((2 : K)⁻¹ • (x + x')) (y - y₀) = a / 2 ∧
    B y₀ ((2 : K)⁻¹ • (x - x')) = -(a / 2) ∧
    B ((2 : K)⁻¹ • (x + x') + y₀) ((2 : K)⁻¹ • (x - x') + (y - y₀)) = 0 ∧
    B ((2 : K)⁻¹ • (x - x')) (y - y₀) = 0 ∧
    ((2 : K)⁻¹ • (x + x') + y₀) + ((2 : K)⁻¹ • (x - x') + (y - y₀)) = x + y := by
  have hx'x : B x' x = 0 := by rw [antisymm B halt, hXX, neg_zero]
  have hyy₀ : B y₀ x' = -B x' y₀ := antisymm B halt _ _
  have hy₀x : B y₀ x = -B x y₀ := antisymm B halt _ _
  have hxx := halt x
  have hx'x' := halt x'
  have hy₀y₀ := halt y₀
  simp only [map_add, map_sub, map_smul, LinearMap.add_apply, LinearMap.sub_apply,
    LinearMap.smul_apply, smul_eq_mul] at h0 h0' ⊢
  simp only [hxy, hx'y, hXX, hx'x, hxx, hx'x', hy₀y₀, hYY, hyy₀, hy₀x]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · linear_combination -h0
  · linear_combination -h0'
  · linear_combination -h0 - h0'
  · linear_combination -h0'
  · calc _ = ((2 : K)⁻¹ • (x + x') + (2 : K)⁻¹ • (x - x')) + y := by abel
      _ = x + y := by rw [halves_add h2 x x']

theorem forced_zero (B : V →ₗ[K] V →ₗ[K] K) (x x' y : V) (a : K) (ha : a ≠ 0)
    (hxy : B x y = a) (hline : ∃ c : K, x' = c • x) (hx'y : B x' y = 0) : x' = 0 := by
  obtain ⟨c, rfl⟩ := hline
  simp only [map_smul, LinearMap.smul_apply, smul_eq_mul, hxy] at hx'y
  rcases mul_eq_zero.mp hx'y with hc | hc
  · rw [hc, zero_smul]
  · exact absurd hc ha

theorem no_y0_of_xprime_zero (B : V →ₗ[K] V →ₗ[K] K) (h2 : (2 : K) ≠ 0) (x y₀ : V) (a : K)
    (ha : a ≠ 0) :
    ¬ (B ((2 : K)⁻¹ • (x + 0)) y₀ = 0 ∧ B ((2 : K)⁻¹ • (x - 0)) y₀ = a / 2) := by
  rintro ⟨h0, h1⟩
  rw [add_zero] at h0
  rw [sub_zero, h0] at h1
  rcases div_eq_zero_iff.mp h1.symm with h | h
  · exact ha h
  · exact h2 h

end BensonCohomology.SymplecticHalving

#print axioms BensonCohomology.SymplecticHalving.isotropic_split
#print axioms BensonCohomology.SymplecticHalving.halves_sub
#print axioms BensonCohomology.SymplecticHalving.no_y0_of_xprime_zero
#print axioms BensonCohomology.SymplecticHalving.forced_zero
#print axioms BensonCohomology.SymplecticHalving.antisymm
#print axioms BensonCohomology.SymplecticHalving.halves_add
