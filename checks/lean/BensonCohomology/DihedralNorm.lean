import Mathlib.Tactic.NoncommRing
import Mathlib.Algebra.Ring.Basic

/-!
# The norm of the index-two dihedral subgroup in characteristic two

Section 5.13, proof of Theorem 5.13.1 (ii), p. 197.  For the dihedral group
`G = D_4q = ⟨x, y | x² = y² = 1, (xy)^q = (yx)^q⟩` over a field `k` of
characteristic two, put `X = 1 + x`, `Y = 1 + y`, so that `X² = Y² = 0`.  The
book computes the sum `H̃` of the elements of `H = ⟨xyx, y⟩` as
`((1 + xyx)(1 + y))^(q/2) = ((Y + XY + YX + XYX) Y)^(q/2)
 = (YXY + XYXY)^(q/2) = (YX)^(q-1) Y + (XY)^q`
(the printed text omits the first opening parenthesis of the second
expression).

Notation.  `R` is any ring; `X`, `Y` are elements with `X * X = 0`,
`Y * Y = 0`; characteristic two is the hypothesis `(2 : R) = 0`; `m` stands
for `q / 2`, written `m + 1` (so `q = 2m + 2`).

* `one_add_xyx`: `1 + xyx = Y + XY + YX + XYX` (uses `2 = 0`, `X² = 0`).
* `one_add_y`: `1 + y = Y` (uses `2 = 0`).
* `base_eq`: `(Y + XY + YX + XYX) Y = YXY + XYXY` (uses `Y² = 0`).
* `pow_eq`: `(YXY + XYXY)^(m+1) = (YX)^(2m+1) Y + (XY)^(2m+2)` (uses `Y² = 0`
  only).
* `norm_eq`: the whole display, `((1 + xyx)(1 + y))^(m+1) =
  (YX)^(2m+1) Y + (XY)^(2m+2)`.

Not covered: that `H̃ = ((1 + xyx)(1 + y))^(q/2)` is the sum of the elements
of `H`, that `G̃ = (XY)^q`, and the relation `(XY)^q = (YX)^q` of `k D_4q`;
these are checked in the group algebras of `D_8`, `D_16`, `D_32` over `F_2`
in `checks/sage/chapter-5b.py`.
-/

namespace BensonCohomology.DihedralNorm

variable {R : Type*} [Ring R]

theorem one_add_xyx (h2 : (2 : R) = 0) (X Y : R) (hX : X * X = 0) :
    1 + (1 + X) * (1 + Y) * (1 + X) = Y + X * Y + Y * X + X * Y * X := by
  have e : 1 + (1 + X) * (1 + Y) * (1 + X)
      = (Y + X * Y + Y * X + X * Y * X) + (2 : R) * (1 + X) + X * X := by
    noncomm_ring
  rw [e, hX, h2, zero_mul, add_zero, add_zero]

theorem one_add_y (h2 : (2 : R) = 0) (Y : R) : 1 + (1 + Y) = Y := by
  have e : 1 + (1 + Y) = Y + (2 : R) := by rw [← one_add_one_eq_two]; abel
  rw [e, h2, add_zero]

theorem base_eq (X Y : R) (hY : Y * Y = 0) :
    (Y + X * Y + Y * X + X * Y * X) * Y = Y * X * Y + X * Y * X * Y := by
  have e : (Y + X * Y + Y * X + X * Y * X) * Y
      = Y * Y + X * (Y * Y) + Y * X * Y + X * Y * X * Y := by noncomm_ring
  rw [e, hY, mul_zero, zero_add, zero_add]

section powers

variable (X Y : R) (hY : Y * Y = 0)
include hY

theorem u_A (k : ℕ) : (Y * X) ^ k * Y * (Y * X * Y) = 0 := by
  calc (Y * X) ^ k * Y * (Y * X * Y) = (Y * X) ^ k * (Y * Y) * (X * Y) := by
        simp only [mul_assoc]
    _ = 0 := by rw [hY, mul_zero, zero_mul]

theorem v_A (k : ℕ) : (X * Y) ^ (k + 1) * (Y * X * Y) = 0 := by
  rw [pow_succ]
  calc (X * Y) ^ k * (X * Y) * (Y * X * Y)
        = (X * Y) ^ k * X * (Y * Y) * (X * Y) := by simp only [mul_assoc]
    _ = 0 := by rw [hY, mul_zero, zero_mul]

omit hY in
theorem u_B (k : ℕ) :
    (Y * X) ^ k * Y * (X * Y * X * Y) = (Y * X) ^ (k + 2) * Y := by
  rw [pow_add, pow_two]
  simp only [mul_assoc]

omit hY in
theorem v_B (k : ℕ) : (X * Y) ^ k * (X * Y * X * Y) = (X * Y) ^ (k + 2) := by
  rw [pow_add, pow_two]
  simp only [mul_assoc]

theorem pow_eq (m : ℕ) :
    (Y * X * Y + X * Y * X * Y) ^ (m + 1)
      = (Y * X) ^ (2 * m + 1) * Y + (X * Y) ^ (2 * m + 2) := by
  induction m with
  | zero =>
    simp only [Nat.mul_zero, zero_add, pow_one, pow_two,
      mul_assoc]
  | succ m ih =>
    rw [pow_succ, ih, add_mul, mul_add, mul_add, u_A X Y hY,
      u_B X Y, v_A X Y hY, v_B X Y, zero_add, zero_add]
    have e1 : 2 * m + 1 + 2 = 2 * (m + 1) + 1 := by omega
    have e2 : 2 * m + 2 + 2 = 2 * (m + 1) + 2 := by omega
    rw [e1, e2]

end powers

/-- The display of p. 197: `((1 + xyx)(1 + y))^(q/2) = (YX)^(q-1) Y + (XY)^q`
with `q / 2 = m + 1`, in characteristic two with `X² = Y² = 0`. -/
theorem norm_eq (h2 : (2 : R) = 0) (X Y : R) (hX : X * X = 0)
    (hY : Y * Y = 0) (m : ℕ) :
    ((1 + (1 + X) * (1 + Y) * (1 + X)) * (1 + (1 + Y))) ^ (m + 1)
      = (Y * X) ^ (2 * m + 1) * Y + (X * Y) ^ (2 * m + 2) := by
  rw [one_add_xyx h2 X Y hX, one_add_y h2 Y, base_eq X Y hY, pow_eq X Y hY]

end BensonCohomology.DihedralNorm

#print axioms BensonCohomology.DihedralNorm.norm_eq
#print axioms BensonCohomology.DihedralNorm.one_add_xyx
#print axioms BensonCohomology.DihedralNorm.one_add_y
#print axioms BensonCohomology.DihedralNorm.base_eq
#print axioms BensonCohomology.DihedralNorm.u_A
#print axioms BensonCohomology.DihedralNorm.v_A
#print axioms BensonCohomology.DihedralNorm.u_B
#print axioms BensonCohomology.DihedralNorm.v_B
#print axioms BensonCohomology.DihedralNorm.pow_eq
