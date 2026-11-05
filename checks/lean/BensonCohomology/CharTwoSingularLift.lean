import Mathlib.Algebra.CharP.Two
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.Tactic.LinearCombination

/-!
# Singular lifts in characteristic two

Section 7.4, proof of Theorem 7.4.1 (ii), p. 245.  An orthogonal form in
characteristic two is a symmetric bilinear form `b` and a quadratic form
`q` with `q(x + y) = q(x) + q(y) + b(x, y)`.  The book states: if the form
is non-degenerate (here: `q` vanishes on no non-zero vector of the radical
of `b`), "the radical can only have one dimension, since the quadratic
form is (semi)linear on this radical", and, for the quotient by the
radical `⟨r⟩`, "Given a (necessarily isotropic) vector in the symplectic
space, among its preimages is exactly one isotropic vector in the
orthogonal space".  Both rest on the identity
`q(v + c r) = q(v) + c² q(r)` for `b(v, r) = 0` and on the bijectivity
of `c ↦ c²` on a finite field of characteristic two.

Notation.  `K` is a finite field with `CharP K 2`, `b : V →ₗ[K] V →ₗ[K] K`,
`Q : V → K` with `hpolar : Q (u + w) = Q u + Q w + b u w` and
`hhom : Q (c • w) = c ^ 2 * Q w`; `r` with `Q r ≠ 0`.

* `Q_line`: `Q (v + c • r) = Q v + c ^ 2 * Q r` when `b v r = 0`.
* `unique_lift`: for `b v r = 0` there is exactly one `c` with
  `Q (v + c • r) = 0` (the preimages of the class of `v` modulo `⟨r⟩` are
  the `v + c • r`).
* `radical_line`: if `b s r = 0` and `Q` vanishes on the line `s + K r`
  only at `0` (non-degeneracy on the radical), then `s ∈ K r`; so the
  radical is at most one dimensional.

Not covered: that `b` is alternating with a radical in odd dimension, and
the use of the lifts for `H₀(𝓕_M)`; these are checked for `GO(3, 2)`,
`GO(3, 4)`, `GO(5, 2)`, `GO(5, 4)`, `GO(7, 2)` (and `Sp₄(𝔽₂)`, `Sp₄(𝔽₄)`,
`Sp₆(𝔽₂)`) in `checks/sage/chapter-7b.py`.
-/

namespace BensonCohomology.CharTwoSingularLift

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

theorem Q_line (Q : V → K) (b : V →ₗ[K] V →ₗ[K] K)
    (hpolar : ∀ u w, Q (u + w) = Q u + Q w + b u w)
    (hhom : ∀ (c : K) w, Q (c • w) = c ^ 2 * Q w)
    (v r : V) (hvr : b v r = 0) (c : K) :
    Q (v + c • r) = Q v + c ^ 2 * Q r := by
  rw [hpolar, hhom, map_smul, hvr, smul_zero, add_zero]

theorem unique_lift [CharP K 2] [Finite K] (Q : V → K) (b : V →ₗ[K] V →ₗ[K] K)
    (hpolar : ∀ u w, Q (u + w) = Q u + Q w + b u w)
    (hhom : ∀ (c : K) w, Q (c • w) = c ^ 2 * Q w)
    (v r : V) (hvr : b v r = 0) (hr : Q r ≠ 0) :
    ∃! c : K, Q (v + c • r) = 0 := by
  obtain ⟨d, hd⟩ := isSquare_of_charTwo' (Q v / Q r)
  have hd2 : d ^ 2 * Q r = Q v := by
    rw [sq, ← hd, div_mul_cancel₀ _ hr]
  refine ⟨d, ?_, ?_⟩
  · show Q (v + d • r) = 0
    rw [Q_line Q b hpolar hhom v r hvr, hd2, CharTwo.add_self_eq_zero]
  · intro c hc
    rw [Q_line Q b hpolar hhom v r hvr] at hc
    have h1 : (c + d) ^ 2 * Q r = 0 := by
      rw [CharTwo.add_sq]
      linear_combination hc + hd2
    have h2 : (c + d) ^ 2 = 0 := (mul_eq_zero.mp h1).resolve_right hr
    exact CharTwo.add_eq_zero.mp ((pow_eq_zero_iff two_ne_zero).mp h2)

theorem radical_line [CharP K 2] [Finite K] (Q : V → K) (b : V →ₗ[K] V →ₗ[K] K)
    (hpolar : ∀ u w, Q (u + w) = Q u + Q w + b u w)
    (hhom : ∀ (c : K) w, Q (c • w) = c ^ 2 * Q w)
    (s r : V) (hsr : b s r = 0) (hr : Q r ≠ 0)
    (hnd : ∀ c : K, Q (s + c • r) = 0 → s + c • r = 0) :
    ∃ c : K, s = c • r := by
  obtain ⟨c, hc, -⟩ := unique_lift Q b hpolar hhom s r hsr hr
  refine ⟨c, ?_⟩
  have h := hnd c hc
  rw [add_eq_zero_iff_eq_neg, ← neg_smul, CharTwo.neg_eq] at h
  exact h

end BensonCohomology.CharTwoSingularLift

#print axioms BensonCohomology.CharTwoSingularLift.Q_line
#print axioms BensonCohomology.CharTwoSingularLift.unique_lift
#print axioms BensonCohomology.CharTwoSingularLift.radical_line
