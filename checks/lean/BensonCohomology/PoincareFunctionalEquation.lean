import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.BigOperators.Ring.List
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# The functional equation of the Poincaré series

Section 5.18, the end of the proof of Theorem 5.18.1 (p. 212) and the proof
of Corollary 5.18.2 (p. 213).  If `H*(G, k)` is a free module over a
polynomial subring on `ζ₁, …, ζ_r` of degrees `n₁, …, n_r`, then
`p(t) = f(t) / ∏ (1 - t^(nᵢ))` with `f` the Poincaré series of
`H*(Hom_kG(C, k))`, which satisfies `t^s f(1/t) = f(t)`,
`s = Σ (nᵢ - 1)` (Corollary 5.17.4); the book then computes
`p(1/t) = (-t)^r p(t)`.  For a polynomial cohomology ring with generators of
degrees `d₁, …, d_r` (Corollary 5.18.2) the book concludes from this
functional equation that all `dᵢ = 1`.

Notation.  `K` is a field, `t, u ∈ K` with `t u = 1` (`u = 1/t`); the
degrees are a list `ns`, `r` its length; `F` and `Finv` stand for the values
`f(t)` and `f(1/t)`; the denominators are `∏ (1 - t^nᵢ)` and
`∏ (1 - u^nᵢ)`.

* `prod_inv`: `∏ (1 - u^nᵢ) = (-1)^r u^(Σ nᵢ) ∏ (1 - t^nᵢ)`.
* `functional_equation`: if `t^s · f(1/t) = f(t)` and `s + r = Σ nᵢ`, then
  `f(1/t) / ∏ (1 - u^nᵢ) = (-t)^r · (f(t) / ∏ (1 - t^nᵢ))`, i.e.
  `p(1/t) = (-t)^r p(t)` (both sides are `0` if a denominator vanishes).
* `sum_sub_one`: `s = Σ (nᵢ - 1)` satisfies `s + r = Σ nᵢ` when all
  `nᵢ ≥ 1`.
* `polynomial_degrees_one`: for `p(t) = 1/∏ (1 - t^dᵢ)` (all `dᵢ ≥ 1`), if
  `p(1/t) = (-t)^r p(t)` holds at `t = 2` in `ℚ` (as it does when it holds
  as an identity of rational functions), then every `dᵢ = 1`.

Not covered: the spectral sequence argument giving `p = f / ∏ (1 - t^nᵢ)`
and the duality of `f`; these are checked numerically (Poincaré series of
elementary abelian, dihedral and quaternion groups and of `GL₃(F₂)`) in
`checks/sage/chapter-5b.py`.
-/

namespace BensonCohomology.PoincareFunctionalEquation

variable {K : Type*} [Field K]

theorem one_sub_u_pow (t u : K) (htu : t * u = 1) (n : ℕ) :
    1 - u ^ n = -(u ^ n) * (1 - t ^ n) := by
  have h : u ^ n * t ^ n = 1 := by
    rw [← mul_pow, mul_comm, htu, one_pow]
  linear_combination (-1 : K) * h

theorem prod_inv (t u : K) (htu : t * u = 1) (ns : List ℕ) :
    (ns.map fun n => 1 - u ^ n).prod
      = (-1) ^ ns.length * u ^ ns.sum * (ns.map fun n => 1 - t ^ n).prod := by
  induction ns with
  | nil => simp
  | cons n ns ih =>
    simp only [List.map_cons, List.prod_cons, List.length_cons, List.sum_cons]
    rw [ih, one_sub_u_pow t u htu n, pow_succ, pow_add]
    ring

theorem functional_equation (t u : K) (htu : t * u = 1) (ns : List ℕ) (s : ℕ)
    (hs : s + ns.length = ns.sum) (F Finv : K) (hF : t ^ s * Finv = F) :
    Finv / (ns.map fun n => 1 - u ^ n).prod
      = (-t) ^ ns.length * (F / (ns.map fun n => 1 - t ^ n).prod) := by
  rw [prod_inv t u htu ns, ← hs]
  set D := (ns.map fun n => 1 - t ^ n).prod with hDdef
  set c : K := (-1) ^ ns.length with hc
  by_cases hD : D = 0
  · rw [hD]; simp
  · have hu : u ≠ 0 := by
      intro h0; rw [h0, mul_zero] at htu; exact zero_ne_one htu
    have hden : c * u ^ (s + ns.length) * D ≠ 0 :=
      mul_ne_zero (mul_ne_zero (pow_ne_zero _ (by norm_num)) (pow_ne_zero _ hu)) hD
    rw [div_eq_iff hden]
    have e : (-t) ^ ns.length * (F / D) * (c * u ^ (s + ns.length) * D)
        = (-t) ^ ns.length * c * u ^ (s + ns.length) * (F / D * D) := by ring
    rw [e, div_mul_cancel₀ F hD, ← hF, neg_pow]
    have hcc : c * c = 1 := by rw [hc, ← mul_pow]; norm_num
    have htu2 : t ^ (s + ns.length) * u ^ (s + ns.length) = 1 := by
      rw [← mul_pow, htu, one_pow]
    linear_combination (-Finv) * hcc + (-(c * c) * Finv) * htu2

theorem sum_sub_one (ns : List ℕ) (h : ∀ n ∈ ns, 1 ≤ n) :
    (ns.map fun n => n - 1).sum + ns.length = ns.sum := by
  induction ns with
  | nil => simp
  | cons n ns ih =>
    simp only [List.map_cons, List.sum_cons, List.length_cons]
    have hn : 1 ≤ n := h n (by simp)
    have := ih (fun m hm => h m (by simp [hm]))
    omega

theorem sum_eq_length (ns : List ℕ) (h : ∀ n ∈ ns, 1 ≤ n)
    (hsum : ns.sum = ns.length) : ∀ n ∈ ns, n = 1 := by
  induction ns with
  | nil => simp
  | cons n ns ih =>
    simp only [List.sum_cons, List.length_cons] at hsum
    have hn : 1 ≤ n := h n (by simp)
    have hge : ns.length ≤ ns.sum := by
      have := sum_sub_one ns (fun m hm => h m (by simp [hm])); omega
    intro m hm
    rcases List.mem_cons.mp hm with rfl | hm'
    · omega
    · exact ih (fun k hk => h k (by simp [hk])) (by omega) m hm'

theorem polynomial_degrees_one (ns : List ℕ) (h : ∀ n ∈ ns, 1 ≤ n)
    (hFE : (1 : ℚ) / (ns.map fun n => 1 - (1 / 2 : ℚ) ^ n).prod
      = (-2) ^ ns.length * (1 / (ns.map fun n => 1 - (2 : ℚ) ^ n).prod)) :
    ∀ n ∈ ns, n = 1 := by
  apply sum_eq_length ns h
  have htu : (2 : ℚ) * (1 / 2) = 1 := by norm_num
  set D := (ns.map fun n => 1 - (2 : ℚ) ^ n).prod with hDdef
  have hD : D ≠ 0 := by
    apply List.prod_ne_zero
    intro h0
    obtain ⟨n, hn, hn0⟩ := List.mem_map.mp h0
    have h1 : (1 : ℚ) < 2 ^ n := one_lt_pow₀ (by norm_num) (by have := h n hn; omega)
    linarith
  rw [prod_inv (2 : ℚ) (1 / 2) htu ns, ← hDdef] at hFE
  set c : ℚ := (-1) ^ ns.length with hc
  set v : ℚ := (1 / 2) ^ ns.sum with hv
  have hcv : c * v * D ≠ 0 :=
    mul_ne_zero (mul_ne_zero (pow_ne_zero _ (by norm_num)) (pow_ne_zero _ (by norm_num))) hD
  rw [mul_one_div, div_eq_div_iff hcv hD, one_mul] at hFE
  have h1 : (1 : ℚ) * D = ((-2) ^ ns.length * c * v) * D := by linear_combination hFE
  have hA : (1 : ℚ) = (-2) ^ ns.length * c * v := mul_right_cancel₀ hD h1
  have hcc : c * c = 1 := by rw [hc, ← mul_pow]; norm_num
  have hA' : (1 : ℚ) = 2 ^ ns.length * v := by
    rw [hA, show (-2 : ℚ) = -1 * 2 by norm_num, mul_pow]
    linear_combination (2 ^ ns.length * v) * hcc
  have hB : v * 2 ^ ns.sum = 1 := by rw [hv, ← mul_pow]; norm_num
  have key : (2 : ℚ) ^ ns.sum = 2 ^ ns.length := by
    linear_combination (2 ^ ns.sum : ℚ) * hA' + (2 ^ ns.length : ℚ) * hB
  exact Nat.pow_right_injective (le_refl 2) (by exact_mod_cast key)

end BensonCohomology.PoincareFunctionalEquation

#print axioms BensonCohomology.PoincareFunctionalEquation.functional_equation
#print axioms BensonCohomology.PoincareFunctionalEquation.polynomial_degrees_one
#print axioms BensonCohomology.PoincareFunctionalEquation.sum_sub_one
#print axioms BensonCohomology.PoincareFunctionalEquation.one_sub_u_pow
#print axioms BensonCohomology.PoincareFunctionalEquation.prod_inv
#print axioms BensonCohomology.PoincareFunctionalEquation.sum_eq_length
