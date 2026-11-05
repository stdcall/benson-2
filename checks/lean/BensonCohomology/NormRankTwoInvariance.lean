import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.RingTheory.MvPolynomial.Basic
import Mathlib.Algebra.CharP.Lemmas
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Proposition 4.1.4 (i): the invariance argument for `norm(x₂)`

Book: D. J. Benson, *Representations and Cohomology II* (first paperback
edition 1998), Section 4.1, the Example before Proposition 4.1.4 (printed
p. 125): with `G = ℤ/p × ℤ/p`, `H = 1 × ℤ/p`, `norm_(H,G)(x₂)` is invariant
under the automorphisms of the first factor, hence of the form
`x₂^p + λ x₁^(p-1) x₂ + μ x₁^(p-2) y₁ x₂ y₂`; it is also invariant under the
automorphism fixing the second generator and sending the first to its
product with the second, which sends `x₂ ↦ x₁ + x₂` and fixes `x₁`; "equating
… we find that `λ = -1`".

Notation.  The part of `H^*(G, F_p)` not involving `y₁, y₂` is the polynomial
ring `F_p[x₁, x₂]`, here `MvPolynomial (Fin 2) (ZMod p)` with `x₁ = X 0`,
`x₂ = X 1`; `p` is a prime (the book's `p` is odd, the statement holds for
every prime).

* `invariance_iff`: `x₂^p + λ x₁^(p-1) x₂` is invariant under
  `x₂ ↦ x₁ + x₂` iff `λ = -1`.
* `norm_x2_invariant`: hence `x₂^p - x₁^(p-1) x₂` is the invariant one.

Not covered: the part `μ x₁^(p-2) y₁ x₂ y₂` with the exterior generators
(`μ = 0`), the derivation of the general form from the invariance under the
automorphisms of the first factor, and the identity
`x₂^p - x₁^(p-1) x₂ = ∏_λ (x₂ + λ x₁)` (all checked in
`checks/sage/chapter-4a.py`, which also computes the norm at chain level).
-/

namespace BensonCohomology.NormRankTwoInvariance

open MvPolynomial

variable (p : ℕ) [Fact p.Prime]

/-- `x₂^p + λ x₁^(p-1) x₂` is invariant under `x₂ ↦ x₁ + x₂` iff `λ = -1`. -/
theorem invariance_iff (lam : ZMod p) :
    ((X 0 + X 1) ^ p + C lam * X 0 ^ (p - 1) * (X 0 + X 1) : MvPolynomial (Fin 2) (ZMod p)) =
      X 1 ^ p + C lam * X 0 ^ (p - 1) * X 1 ↔ lam = -1 := by
  have hp1 : 1 ≤ p := (Fact.out : p.Prime).one_lt.le
  have hfrob : ((X 0 + X 1) ^ p : MvPolynomial (Fin 2) (ZMod p)) = X 0 ^ p + X 1 ^ p :=
    add_pow_char _ _ _
  have hx : (X 0 ^ (p - 1) * X 0 : MvPolynomial (Fin 2) (ZMod p)) = X 0 ^ p := by
    rw [← pow_succ, Nat.sub_add_cancel hp1]
  constructor
  · intro h
    have h' : (C (1 + lam) * X 0 ^ p : MvPolynomial (Fin 2) (ZMod p)) = 0 := by
      rw [map_add, map_one]
      linear_combination h - hfrob - C lam * hx
    have hX : (X 0 ^ p : MvPolynomial (Fin 2) (ZMod p)) ≠ 0 := pow_ne_zero _ (X_ne_zero _)
    have hC : (C (1 + lam) : MvPolynomial (Fin 2) (ZMod p)) = 0 :=
      (mul_eq_zero.mp h').resolve_right hX
    rw [C_eq_zero] at hC
    linear_combination hC
  · rintro rfl
    rw [map_neg, map_one]
    linear_combination hfrob - hx

/-- The invariant form of Proposition 4.1.4 (i): `x₂^p - x₁^(p-1) x₂`. -/
theorem norm_x2_invariant :
    ((X 0 + X 1) ^ p - X 0 ^ (p - 1) * (X 0 + X 1) : MvPolynomial (Fin 2) (ZMod p)) =
      X 1 ^ p - X 0 ^ (p - 1) * X 1 := by
  have h := (invariance_iff p (-1)).mpr rfl
  rw [map_neg, map_one] at h
  linear_combination h

end BensonCohomology.NormRankTwoInvariance

#print axioms BensonCohomology.NormRankTwoInvariance.invariance_iff
#print axioms BensonCohomology.NormRankTwoInvariance.norm_x2_invariant
