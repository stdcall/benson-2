import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# The sign of the dual of a cocycle

Section 5.17, Proposition 5.17.2 and its proof, pp. 209-210.  For
`ζ ∈ Hⁿ(G, k)` the book shows `Ωⁿ(ζ̂*) = λₙ ζ̂` with a constant `λₙ`
depending only on `n`, and derives from the facts that `ζ ↦ λₙ ζ` is an
anti-automorphism and that `λ₁ = -1` (the transpose inverse of
`[[1, α], [0, 1]]` is `[[1, 0], [-α, 1]]`):
`λₘ λₙ = (-1)^(mn) λ_(m+n)` and, by induction, `λₙ = (-1)^(n(n+1)/2)`.
The left-hand vertical map `k → k` of the last diagram of the proof is
induced by `γ ∘ (ζ̂* ⊗ 1) = λₙ ζ̂` on `Ωⁿk / L_ζ ≅ k`, so it is `λₙ`; the
diagram printed `(-1)^(n(n-1)/2)`, which differs from `λₙ` for odd `n`.

Notation.  `lam : ℕ → ℤ` is `n ↦ λₙ` (values in `ℤ`, mapped to `k`);
hypotheses `h1 : lam 1 = -1` and `hmul : lam m * lam n = (-1)^(m*n) *
lam (m+n)` for all `m, n ≥ 1` are the two facts quoted above.

* `lam_eq`: `lam n = (-1)^(n(n+1)/2)` for `n ≥ 1`.
* `lam_formula_consistent`: the formula satisfies both hypotheses (so they
  are consistent and determine `lam` on `n ≥ 1`).
* `printed_label_wrong`: `(-1)^(n(n-1)/2) = -(-1)^(n(n+1)/2)` for odd `n`;
  in particular the printed label is `+1` for `n = 1`, while `λ₁ = -1`.

Not covered: that `ζ ↦ λₙ ζ` is an anti-automorphism, the value `λ₁ = -1`
and the identification of the induced map with `λₙ`; these are checked for
cyclic groups of order 3, 5, 7 and for `Z/3 × Z/3` (`n ≤ 6`) in
`checks/sage/chapter-5b.py`, with the bottom row of the diagram the dual
complex with the transposed maps.
-/

namespace BensonCohomology.DualCocycleSign

theorem half_succ (n : ℕ) :
    (n + 1) * (n + 1 + 1) / 2 = n * (n + 1) / 2 + (n + 1) := by
  have e : (n + 1) * (n + 1 + 1) = n * (n + 1) + (n + 1) * 2 := by ring
  rw [e, Nat.add_mul_div_right _ _ (by norm_num : 0 < 2)]

theorem neg_one_pow_mul_self (n : ℕ) : ((-1 : ℤ) ^ n) * ((-1) ^ n) = 1 := by
  rw [← pow_add, ← two_mul, pow_mul]
  norm_num

theorem lam_eq (lam : ℕ → ℤ) (h1 : lam 1 = -1)
    (hmul : ∀ m n, 1 ≤ m → 1 ≤ n → lam m * lam n = (-1) ^ (m * n) * lam (m + n)) :
    ∀ n, 1 ≤ n → lam n = (-1) ^ (n * (n + 1) / 2) := by
  intro n hn
  induction n with
  | zero => omega
  | succ n ih =>
    rcases Nat.eq_zero_or_pos n with h0 | hpos
    · subst h0
      simp [h1]
    · have h := hmul n 1 hpos (le_refl 1)
      rw [h1, Nat.mul_one] at h
      have hsq := neg_one_pow_mul_self n
      have step : lam (n + 1) = (-1) ^ (n + 1) * lam n := by
        linear_combination (-((-1 : ℤ) ^ n)) * h + (-(lam (n + 1))) * hsq
      rw [step, ih hpos, half_succ, pow_add (-1 : ℤ) (n * (n + 1) / 2) (n + 1)]
      ring

theorem lam_formula_consistent (m n : ℕ) :
    ((-1 : ℤ) ^ (m * (m + 1) / 2)) * ((-1) ^ (n * (n + 1) / 2))
      = (-1) ^ (m * n) * (-1) ^ ((m + n) * (m + n + 1) / 2) := by
  have e : (m + n) * (m + n + 1) / 2 = m * (m + 1) / 2 + n * (n + 1) / 2 + m * n := by
    have hm : 2 ∣ m * (m + 1) := (Nat.even_mul_succ_self m).two_dvd
    have hn : 2 ∣ n * (n + 1) := (Nat.even_mul_succ_self n).two_dvd
    obtain ⟨a, ha⟩ := hm
    obtain ⟨b, hb⟩ := hn
    have e2 : (m + n) * (m + n + 1) = 2 * (a + b + m * n) := by
      have : (m + n) * (m + n + 1) = m * (m + 1) + n * (n + 1) + 2 * (m * n) := by ring
      rw [this, ha, hb]; ring
    rw [e2, ha, hb]
    simp [Nat.mul_div_cancel_left _ (by norm_num : 0 < 2)]
  rw [e, pow_add, pow_add]
  have hs := neg_one_pow_mul_self (m * n)
  linear_combination (-(-1 : ℤ) ^ (m * (m + 1) / 2) * (-1) ^ (n * (n + 1) / 2)) * hs

theorem formula_one : ((-1 : ℤ) ^ (1 * (1 + 1) / 2)) = -1 := by norm_num

theorem printed_label_wrong (n : ℕ) (hodd : n % 2 = 1) :
    ((-1 : ℤ) ^ (n * (n - 1) / 2)) = -((-1) ^ (n * (n + 1) / 2)) := by
  obtain ⟨k, rfl⟩ : ∃ k, n = 2 * k + 1 := ⟨n / 2, by omega⟩
  have e1 : (2 * k + 1) * (2 * k + 1 - 1) / 2 = k * (2 * k + 1) := by
    have : (2 * k + 1) * (2 * k + 1 - 1) = 2 * (k * (2 * k + 1)) := by
      rw [show 2 * k + 1 - 1 = 2 * k by omega]; ring
    rw [this, Nat.mul_div_cancel_left _ (by norm_num : 0 < 2)]
  have e2 : (2 * k + 1) * (2 * k + 1 + 1) / 2 = k * (2 * k + 1) + (2 * k + 1) := by
    have : (2 * k + 1) * (2 * k + 1 + 1) = 2 * (k * (2 * k + 1) + (2 * k + 1)) := by ring
    rw [this, Nat.mul_div_cancel_left _ (by norm_num : 0 < 2)]
  rw [e1, e2, pow_add, pow_add, pow_mul]
  norm_num

/-- For `n = 1` the printed label is `+1`, the constant `λ₁` is `-1`. -/
theorem printed_label_one (lam : ℕ → ℤ) (h1 : lam 1 = -1) :
    ((-1 : ℤ) ^ (1 * (1 - 1) / 2)) ≠ lam 1 := by
  rw [h1]; norm_num

end BensonCohomology.DualCocycleSign

#print axioms BensonCohomology.DualCocycleSign.lam_eq
#print axioms BensonCohomology.DualCocycleSign.lam_formula_consistent
#print axioms BensonCohomology.DualCocycleSign.printed_label_wrong
#print axioms BensonCohomology.DualCocycleSign.printed_label_one
#print axioms BensonCohomology.DualCocycleSign.half_succ
#print axioms BensonCohomology.DualCocycleSign.neg_one_pow_mul_self
#print axioms BensonCohomology.DualCocycleSign.formula_one
