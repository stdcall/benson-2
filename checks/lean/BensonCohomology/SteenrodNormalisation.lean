import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The normalisation of the reduced powers: `θ₁` and `P⁰ = 1`

Book: D. J. Benson, *Representations and Cohomology II* (first paperback
edition 1998), Section 4.4, Definition 4.4.3 and the Remark after it
(printed p. 137), and Section 4.5, the constants `θ_r` (printed p. 144);
Section 4.6, the norm of `y₂` (printed p. 146).

Notation.  `p` is an odd prime, `m = (p - 1)/2`, `mf = m!` in `ZMod p`.
Definition 4.4.3 is `P^i(x) = (-1)^(i + m r(r+1)/2) (m!)^(-r) D_((p-1)(r-2i))(x)`
for `x` of degree `r`; with `D_((p-1)r)(x) = θ_r x` (p. 144) this gives
`P⁰(x) = θ_r / c r · x` with `c r = (-1)^(m r(r+1)/2) (m!)^r` (`c` below), so
`P⁰ = 1` in degree `r` iff `θ_r = c r`.  The book shows `θ_(2s) = (-1)^s` and
`θ_(2s+1) = (-1)^s θ₁` (`theta θ₁` below; these values are hypotheses taken
from the book, not proved here) and then chooses `θ₁ = m!`.

* `wilson`: `(p - 1)! = -1` in `ZMod p` (the proof of mathlib's
  `ZMod.wilsons_lemma`, repeated because `Mathlib.NumberTheory.Wilson` is not
  built in the local checkout).
* `descFactorial_cast`: `(p-1)(p-2)⋯(p-k) = (-1)^k k!` in `ZMod p`.
* `half_factorial_sq`: `(m!)² = (-1)^(m+1)` (the Remark after Definition
  4.4.3).
* `P0_eq_one_iff`: `P⁰ = 1` in every degree iff `θ₁ = (-1)^m m!`
  (= `-(m!)⁻¹`, `theta_one_eq`).
* `printed_theta_fails`: for `p ≡ 3 (mod 4)` the printed `θ₁ = m!` does not
  give `P⁰ = 1`.
* `printed_norm_fails`: the constant `c 1 = (-1)^m m!` of the first display
  of Case (ii) of Section 4.6 (degree `r = 1`) is never the printed `(m!)⁻¹`.

Not covered: the construction of the norm, the operations `D_j` and the
values of `θ_(2s)`, `θ_(2s+1)` (computed in `checks/sage/chapter-4a.py` and
`chapter-4b.py`), and the realisation of the sign of `θ₁` by an order of
the cosets.
-/

namespace BensonCohomology.SteenrodNormalisation

open Finset Nat FiniteField

section Wilson

variable (p : ℕ) [Fact p.Prime]

/-- Wilson's lemma `(p - 1)! = -1` in `ZMod p` (proof as in mathlib's `ZMod.wilsons_lemma`). -/
theorem wilson : (((p - 1)! : ℕ) : ZMod p) = -1 := by
  refine
    calc
      (((p - 1)! : ℕ) : ZMod p) = ∏ x ∈ Ico 1 (succ (p - 1)), (x : ZMod p) := by
        rw [← Finset.prod_Ico_id_eq_factorial, prod_natCast]
      _ = ∏ x : (ZMod p)ˣ, (x : ZMod p) := ?_
      _ = -1 := by
        simp_rw [← Units.coeHom_apply, ← map_prod (Units.coeHom (ZMod p)),
          prod_univ_units_id_eq_neg_one, Units.coeHom_apply, Units.val_neg, Units.val_one]
  have hp : 0 < p := (Fact.out (p := p.Prime)).pos
  symm
  refine prod_bij (fun a _ => (a : ZMod p).val) ?_ ?_ ?_ ?_
  · intro a _
    rw [mem_Ico, ← Nat.succ_sub hp, Nat.add_one_sub_one]
    constructor
    · apply Nat.pos_of_ne_zero; rw [← @ZMod.val_zero p]
      intro h; apply Units.ne_zero a (ZMod.val_injective p h)
    · exact ZMod.val_lt _
  · intro _ _ _ _ h; rw [Units.ext_iff]; exact ZMod.val_injective p h
  · intro b hb
    rw [mem_Ico, Nat.succ_le_iff, ← succ_sub hp, Nat.add_one_sub_one, pos_iff_ne_zero] at hb
    refine ⟨Units.mk0 b ?_, Finset.mem_univ _, ?_⟩
    · intro h; apply hb.1; apply_fun ZMod.val at h
      simpa only [ZMod.val_cast_of_lt hb.right, ZMod.val_zero] using h
    · simp only [ZMod.val_cast_of_lt hb.right, Units.val_mk0]
  · rintro a -; simp only [ZMod.cast_id, ZMod.natCast_val]

/-- `(p - 1)(p - 2)⋯(p - k) = (-1)^k k!` in `ZMod p` for `k ≤ p - 1`. -/
theorem descFactorial_cast : ∀ k : ℕ, k ≤ p - 1 →
    (((p - 1).descFactorial k : ℕ) : ZMod p) = (-1) ^ k * ((k ! : ℕ) : ZMod p)
  | 0, _ => by simp
  | k + 1, hk => by
    have h2 := (Fact.out : p.Prime).two_le
    have hsub : ((p - 1 - k : ℕ) : ZMod p) = -((k + 1 : ℕ) : ZMod p) := by
      have h1 : (p - 1 - k) + (k + 1) = p := by omega
      have h0 : ((p - 1 - k : ℕ) : ZMod p) + ((k + 1 : ℕ) : ZMod p) = 0 := by
        rw [← Nat.cast_add, h1, ZMod.natCast_self]
      linear_combination h0
    rw [Nat.descFactorial_succ, Nat.cast_mul, descFactorial_cast k (by omega), hsub,
      Nat.factorial_succ, Nat.cast_mul]
    ring

/-- The Remark after Definition 4.4.3: `(m!)² = (-1)^(m+1)` in `ZMod p`, `m = (p-1)/2`. -/
theorem half_factorial_sq (hodd : p % 2 = 1) :
    ((((p - 1) / 2)! : ℕ) : ZMod p) ^ 2 = (-1) ^ ((p - 1) / 2 + 1) := by
  have h2 := (Fact.out : p.Prime).two_le
  set m := (p - 1) / 2 with hm
  have key := Nat.factorial_mul_descFactorial (show m ≤ p - 1 by omega)
  have hpm : p - 1 - m = m := by omega
  rw [hpm] at key
  have hw := wilson p
  rw [← key, Nat.cast_mul, descFactorial_cast p m (by omega)] at hw
  have hsq : ((-1 : ZMod p) ^ m) ^ 2 = 1 := by
    rw [← pow_mul, mul_comm, pow_mul, neg_one_sq, one_pow]
  rw [pow_succ]
  linear_combination (-1 : ZMod p) ^ m * hw - ((m ! : ℕ) : ZMod p) ^ 2 * hsq

end Wilson

section Normalisation

variable {R : Type*} [CommRing R]

/-- `c (2s) = (-1)^s` when `ε² = 1` and `mf² = -ε` (`ε = (-1)^m`). -/
theorem c_even (ε mf : R) (hε : ε ^ 2 = 1) (hmf : mf ^ 2 = -ε) (s : ℕ) :
    ε ^ (s * (2 * s + 1)) * mf ^ (2 * s) = (-1) ^ s := by
  have e1 : ε ^ (s * (2 * s + 1)) = ε ^ s := by
    rw [show s * (2 * s + 1) = 2 * (s * s) + s by ring, pow_add, pow_mul, hε, one_pow, one_mul]
  have e2 : mf ^ (2 * s) = (-1) ^ s * ε ^ s := by
    rw [pow_mul, hmf, neg_eq_neg_one_mul, mul_pow]
  rw [e1, e2]
  calc ε ^ s * ((-1) ^ s * ε ^ s) = (-1) ^ s * (ε ^ 2) ^ s := by ring
    _ = (-1) ^ s := by rw [hε, one_pow, mul_one]

/-- `c (2s+1) = (-1)^s (ε mf)`. -/
theorem c_odd (ε mf : R) (hε : ε ^ 2 = 1) (hmf : mf ^ 2 = -ε) (s : ℕ) :
    ε ^ ((2 * s + 1) * (s + 1)) * mf ^ (2 * s + 1) = (-1) ^ s * (ε * mf) := by
  have e1 : ε ^ ((2 * s + 1) * (s + 1)) = ε ^ (s + 1) := by
    rw [show (2 * s + 1) * (s + 1) = 2 * (s * s + s) + (s + 1) by ring, pow_add, pow_mul, hε,
      one_pow, one_mul]
  have e2 : mf ^ (2 * s + 1) = (-1) ^ s * ε ^ s * mf := by
    rw [pow_succ, pow_mul, hmf, neg_eq_neg_one_mul, mul_pow]
  rw [e1, e2]
  calc ε ^ (s + 1) * ((-1) ^ s * ε ^ s * mf) = (-1) ^ s * (ε ^ 2) ^ s * (ε * mf) := by ring
    _ = (-1) ^ s * (ε * mf) := by rw [hε, one_pow, mul_one]

end Normalisation

section Steenrod

variable (p : ℕ) [Fact p.Prime]

/-- `m! ∈ ZMod p`, `m = (p - 1)/2`. -/
noncomputable def mf : ZMod p := (((p - 1) / 2)! : ℕ)

/-- `c r = (-1)^(m r(r+1)/2) (m!)^r`, the constant of Definition 4.4.3. -/
noncomputable def c (r : ℕ) : ZMod p := (-1) ^ ((p - 1) / 2 * (r * (r + 1) / 2)) * mf p ^ r

/-- `θ_(2s) = (-1)^s`, `θ_(2s+1) = (-1)^s θ₁` (p. 144). -/
def theta (θ₁ : ZMod p) (r : ℕ) : ZMod p := (-1) ^ (r / 2) * (if r % 2 = 1 then θ₁ else 1)

theorem c_two_mul (s : ℕ) : c p (2 * s) =
    ((-1 : ZMod p) ^ ((p - 1) / 2)) ^ (s * (2 * s + 1)) * mf p ^ (2 * s) := by
  unfold c
  rw [← pow_mul, show 2 * s * (2 * s + 1) / 2 = s * (2 * s + 1) by
    rw [show 2 * s * (2 * s + 1) = 2 * (s * (2 * s + 1)) by ring]; omega]

theorem c_two_mul_add_one (s : ℕ) : c p (2 * s + 1) =
    ((-1 : ZMod p) ^ ((p - 1) / 2)) ^ ((2 * s + 1) * (s + 1)) * mf p ^ (2 * s + 1) := by
  unfold c
  rw [← pow_mul, show (2 * s + 1) * (2 * s + 1 + 1) / 2 = (2 * s + 1) * (s + 1) by
    rw [show (2 * s + 1) * (2 * s + 1 + 1) = 2 * ((2 * s + 1) * (s + 1)) by ring]; omega]

theorem eps_sq : ((-1 : ZMod p) ^ ((p - 1) / 2)) ^ 2 = 1 := by
  rw [← pow_mul, mul_comm, pow_mul, neg_one_sq, one_pow]

theorem mf_sq (hodd : p % 2 = 1) : mf p ^ 2 = -((-1 : ZMod p) ^ ((p - 1) / 2)) := by
  unfold mf; rw [half_factorial_sq p hodd, pow_succ]; ring

/-- `P⁰ = 1` in every degree (`θ_r = c r` for all `r`) iff `θ₁ = (-1)^m m!`. -/
theorem P0_eq_one_iff (hodd : p % 2 = 1) (θ₁ : ZMod p) :
    (∀ r, theta p θ₁ r = c p r) ↔ θ₁ = (-1) ^ ((p - 1) / 2) * mf p := by
  constructor
  · intro h
    have h1 := h 1
    simpa [theta, c] using h1
  · intro h r
    obtain ⟨s, rfl | rfl⟩ := Nat.even_or_odd' r
    · rw [c_two_mul, c_even _ _ (eps_sq p) (mf_sq p hodd)]
      simp [theta]
    · rw [c_two_mul_add_one, c_odd _ _ (eps_sq p) (mf_sq p hodd), ← h]
      simp [theta, show (2 * s + 1) / 2 = s by omega, show (2 * s + 1) % 2 = 1 by omega]

theorem mf_ne_zero (hodd : p % 2 = 1) : mf p ≠ 0 := by
  intro h0
  have h1 := mf_sq p hodd
  rw [h0, zero_pow two_ne_zero] at h1
  have hε : (-1 : ZMod p) ^ ((p - 1) / 2) = 0 := neg_eq_zero.mp h1.symm
  have h2 := eps_sq p
  rw [hε, zero_pow two_ne_zero] at h2
  exact zero_ne_one h2

theorem two_ne_zero' (hodd : p % 2 = 1) : (2 : ZMod p) ≠ 0 := by
  intro h
  have h' : ((2 : ℕ) : ZMod p) = 0 := by exact_mod_cast h
  rw [ZMod.natCast_eq_zero_iff] at h'
  have := Nat.le_of_dvd two_pos h'
  have := (Fact.out : p.Prime).two_le
  omega

/-- The corrected value: `(-1)^m m! = -(m!)⁻¹`. -/
theorem theta_one_eq (hodd : p % 2 = 1) :
    (-1 : ZMod p) ^ ((p - 1) / 2) * mf p = -(mf p)⁻¹ := by
  have hne := mf_ne_zero p hodd
  have hx : (-1 : ZMod p) ^ ((p - 1) / 2) * mf p * mf p = -1 := by
    rw [mul_assoc, ← sq, mf_sq p hodd]
    linear_combination -(eps_sq p)
  calc (-1 : ZMod p) ^ ((p - 1) / 2) * mf p
        = (-1 : ZMod p) ^ ((p - 1) / 2) * mf p * mf p * (mf p)⁻¹ := by
          rw [mul_assoc _ (mf p), mul_inv_cancel₀ hne, mul_one]
    _ = -(mf p)⁻¹ := by rw [hx, neg_one_mul]

/-- The printed `θ₁ = m!` gives `P⁰ ≠ 1` (in degree 1) when `p ≡ 3 (mod 4)`. -/
theorem printed_theta_fails (hp3 : p % 4 = 3) : ¬ ∀ r, theta p (mf p) r = c p r := by
  have hodd : p % 2 = 1 := by omega
  rw [P0_eq_one_iff p hodd]
  intro h
  have hm : Odd ((p - 1) / 2) := Nat.odd_iff.mpr (by omega)
  rw [hm.neg_one_pow] at h
  have : (2 : ZMod p) * mf p = 0 := by linear_combination h
  rcases mul_eq_zero.mp this with h2 | h2
  · exact two_ne_zero' p hodd h2
  · exact mf_ne_zero p hodd h2

/-- The printed constant `(m!)⁻¹` of `norm(y₂)` (p. 146) is never `c 1 = (-1)^m m!`. -/
theorem printed_norm_fails (hodd : p % 2 = 1) : c p 1 ≠ (mf p)⁻¹ := by
  intro h
  have hc : c p 1 = (-1 : ZMod p) ^ ((p - 1) / 2) * mf p := by simp [c]
  rw [hc, theta_one_eq p hodd] at h
  have hne : (mf p)⁻¹ ≠ 0 := inv_ne_zero (mf_ne_zero p hodd)
  have : (2 : ZMod p) * (mf p)⁻¹ = 0 := by linear_combination -h
  rcases mul_eq_zero.mp this with h2 | h2
  · exact two_ne_zero' p hodd h2
  · exact hne h2

end Steenrod

end BensonCohomology.SteenrodNormalisation

#print axioms BensonCohomology.SteenrodNormalisation.wilson
#print axioms BensonCohomology.SteenrodNormalisation.descFactorial_cast
#print axioms BensonCohomology.SteenrodNormalisation.half_factorial_sq
#print axioms BensonCohomology.SteenrodNormalisation.c_even
#print axioms BensonCohomology.SteenrodNormalisation.c_odd
#print axioms BensonCohomology.SteenrodNormalisation.P0_eq_one_iff
#print axioms BensonCohomology.SteenrodNormalisation.theta_one_eq
#print axioms BensonCohomology.SteenrodNormalisation.printed_theta_fails
#print axioms BensonCohomology.SteenrodNormalisation.printed_norm_fails
