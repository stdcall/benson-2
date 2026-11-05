import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Algebra.Module.Submodule.Range
import Mathlib.Algebra.Module.Submodule.Map

/-!
# Propositions 3.2.10 and 3.2.11: the five term exact sequences by splicing

Benson, *Representations and Cohomology II*, Section 3.2, Proposition 3.2.10
(`prop:five-term-cohomology`) and Proposition 3.2.11
(`prop:five-term-homology`); Section 3.5 applies them to the
inflation-restriction sequence.

Cohomology (p. 103): the sequence
`0 → E₂¹⁰ →e H¹ →e' E₂⁰¹ →d₂ E₂²⁰ →e H²` "is obtained by splicing
together" the exact sequences
`0 → E₂¹⁰ → H¹ → E_∞⁰¹ → 0`, `0 → E_∞⁰¹ → E₂⁰¹ →d₂ E₂²⁰ → E_∞²⁰ → 0` and
`0 → E_∞²⁰ → H²`, with `e' = g ∘ f` and the second `e = i ∘ k`.
Formalised as `five_term_cohomology`: from the exactness of the three pieces
the spliced sequence is exact at each of its five places.

Homology (p. 104): `H₂ →e E²₂₀ →d² E²₀₁ →e' H₁ →e E²₁₀ → 0` from
`H₂ ↠ E^∞₂₀`, `0 → E^∞₂₀ → E²₂₀ →d² E²₀₁ → E^∞₀₁ → 0` and
`0 → E^∞₀₁ → H₁ → E^∞₁₀ = E²₁₀ → 0`: `five_term_homology`.

Notation: `f : H¹ → E_∞⁰¹`, `g : E_∞⁰¹ → E₂⁰¹`, `k : E₂²⁰ → E_∞²⁰`,
`i : E_∞²⁰ → H²` (cohomology); `π : H₂ → E^∞₂₀`, `ι : E^∞₂₀ → E²₂₀`,
`q : E²₀₁ → E^∞₀₁`, `j : E^∞₀₁ → H₁`, `p : H₁ → E²₁₀` (homology).
Modules over any ring (abelian groups: `ℤ`).  Not covered: the
identification of the three short sequences with the filtration of `H¹`,
`H²` (Theorem 3.2.9) and with `E₃ = H(E₂, d₂)` in a first quadrant spectral
sequence; these are checked numerically in `checks/sage/chapter-3a.py`.
-/

namespace BensonCohomology.FiveTermSplice

variable {R : Type*} [Ring R]

/-- Proposition 3.2.10: the spliced cohomology sequence is exact. -/
theorem five_term_cohomology {E10 H1 Ei01 E01 E20 Ei20 H2 : Type*}
    [AddCommGroup E10] [Module R E10] [AddCommGroup H1] [Module R H1]
    [AddCommGroup Ei01] [Module R Ei01] [AddCommGroup E01] [Module R E01]
    [AddCommGroup E20] [Module R E20] [AddCommGroup Ei20] [Module R Ei20]
    [AddCommGroup H2] [Module R H2]
    (e : E10 →ₗ[R] H1) (f : H1 →ₗ[R] Ei01) (g : Ei01 →ₗ[R] E01)
    (d2 : E01 →ₗ[R] E20) (k : E20 →ₗ[R] Ei20) (i : Ei20 →ₗ[R] H2)
    -- 0 → E₂¹⁰ → H¹ → E_∞⁰¹ → 0
    (he : Function.Injective e) (hef : LinearMap.range e = LinearMap.ker f)
    (hf : Function.Surjective f)
    -- 0 → E_∞⁰¹ → E₂⁰¹ → E₂²⁰ → E_∞²⁰ → 0 (the last map onto is not used)
    (hg : Function.Injective g) (hgd : LinearMap.range g = LinearMap.ker d2)
    (hdk : LinearMap.range d2 = LinearMap.ker k)
    -- 0 → E_∞²⁰ → H²
    (hi : Function.Injective i) :
    Function.Injective e ∧
      LinearMap.range e = LinearMap.ker (g ∘ₗ f) ∧
      LinearMap.range (g ∘ₗ f) = LinearMap.ker d2 ∧
      LinearMap.range d2 = LinearMap.ker (i ∘ₗ k) := by
  refine ⟨he, ?_, ?_, ?_⟩
  · rw [LinearMap.ker_comp, LinearMap.ker_eq_bot.mpr hg, Submodule.comap_bot,
      hef]
  · rw [LinearMap.range_comp, LinearMap.range_eq_top.mpr hf, Submodule.map_top,
      hgd]
  · rw [LinearMap.ker_comp, LinearMap.ker_eq_bot.mpr hi, Submodule.comap_bot,
      hdk]

/-- Proposition 3.2.11: the spliced homology sequence is exact. -/
theorem five_term_homology {H2 Ei20 E20 E01 Ei01 H1 E10 : Type*}
    [AddCommGroup H2] [Module R H2] [AddCommGroup Ei20] [Module R Ei20]
    [AddCommGroup E20] [Module R E20] [AddCommGroup E01] [Module R E01]
    [AddCommGroup Ei01] [Module R Ei01] [AddCommGroup H1] [Module R H1]
    [AddCommGroup E10] [Module R E10]
    (π : H2 →ₗ[R] Ei20) (ι : Ei20 →ₗ[R] E20) (d2 : E20 →ₗ[R] E01)
    (q : E01 →ₗ[R] Ei01) (j : Ei01 →ₗ[R] H1) (p : H1 →ₗ[R] E10)
    -- H₂ ↠ E^∞₂₀
    (hπ : Function.Surjective π)
    -- 0 → E^∞₂₀ → E²₂₀ → E²₀₁ → E^∞₀₁ → 0
    (hιd : LinearMap.range ι = LinearMap.ker d2)
    (hdq : LinearMap.range d2 = LinearMap.ker q) (hq : Function.Surjective q)
    -- 0 → E^∞₀₁ → H₁ → E²₁₀ → 0
    (hj : Function.Injective j) (hjp : LinearMap.range j = LinearMap.ker p)
    (hp : Function.Surjective p) :
    LinearMap.range (ι ∘ₗ π) = LinearMap.ker d2 ∧
      LinearMap.range d2 = LinearMap.ker (j ∘ₗ q) ∧
      LinearMap.range (j ∘ₗ q) = LinearMap.ker p ∧
      Function.Surjective p := by
  refine ⟨?_, ?_, ?_, hp⟩
  · rw [LinearMap.range_comp, LinearMap.range_eq_top.mpr hπ, Submodule.map_top,
      hιd]
  · rw [LinearMap.ker_comp, LinearMap.ker_eq_bot.mpr hj, Submodule.comap_bot,
      hdq]
  · rw [LinearMap.range_comp, LinearMap.range_eq_top.mpr hq, Submodule.map_top,
      hjp]

end BensonCohomology.FiveTermSplice

#print axioms BensonCohomology.FiveTermSplice.five_term_cohomology
#print axioms BensonCohomology.FiveTermSplice.five_term_homology
