import Mathlib.Data.Finsupp.SMul
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# The contraction of the acyclic Hochschild complex

Section 2.11, p. 73: on `S_n(Λ) = Λ ⊗ ⋯ ⊗ Λ` (`n + 2` factors) the
differential is `b'_n(λ₀ ⊗ ⋯ ⊗ λ_(n+1)) = ∑_(i=0)^n (-1)^i λ₀ ⊗ ⋯ ⊗ λ_i λ_(i+1)
⊗ ⋯ ⊗ λ_(n+1)` and `s_(n+1)` appends a factor `1`.  The text (as corrected)
states `b'_(n+1) ∘ s_(n+1) - s_n ∘ b'_n = (-1)^(n+1) id`, so that `(-1)^n s_n`
is a chain contraction; the printed reading has `id` on the right.

Notation.  A pure tensor `λ₀ ⊗ ⋯ ⊗ λ_k` is the list `[λ₀, …, λ_k]` of elements
of a monoid `M` (the multiplicative monoid of `Λ`); the maps are written on
the free `ℤ`-module `List M →₀ ℤ` on such words.  `merge i w` multiplies the
entries `i` and `i + 1` of `w`; `w ++ [1]` is `s(w)`.

* `merge_append_one`: `merge i (w ++ [1]) = merge i w ++ [1]` for
  `i + 1 < length w`.
* `merge_last`: `merge (n + 1) (w ++ [1]) = w` for `length w = n + 2`.
* `contraction`: the corrected identity on every word of length `n + 2`.
* `chain_contraction`: `b' ∘ ((-1)^(n+1) s) + ((-1)^n s) ∘ b' = id` on words.
* `printed_fails`: for `n = 0` the printed `id` disagrees (`M = ℕ`, `w = [1, 1]`).

Not covered: the passage from words to the tensor power `Λ^(⊗(n+2))`
(the identity holds word by word, so it descends to the tensor product, whose
elements are sums of pure tensors and on which the maps are defined by the
same formulae); the identity `b' ∘ b' = 0`; the projectivity of `S_n(Λ)`.
The identity is also checked numerically in `checks/sage/chapter-2b.py` for
five algebras and `n ≤ 3`.
-/

namespace BensonCohomology.AcyclicHochschildContraction

open Finset

variable {M : Type*} [Monoid M]

/-- Multiply the entries `i` and `i + 1` of a word. -/
def merge : ℕ → List M → List M
  | 0, a :: b :: l => (a * b) :: l
  | i + 1, a :: l => a :: merge i l
  | _, l => l

/-- `b'` on a word of length `n + 2` (the book's `S_n`). -/
noncomputable def bprime (n : ℕ) (w : List M) : List M →₀ ℤ :=
  ∑ i ∈ range (n + 1), Finsupp.single (merge i w) ((-1 : ℤ) ^ i)

/-- `s_n ∘ b'_n` on a word of length `n + 2`. -/
noncomputable def sAfterBprime (n : ℕ) (w : List M) : List M →₀ ℤ :=
  ∑ i ∈ range (n + 1), Finsupp.single (merge i w ++ [1]) ((-1 : ℤ) ^ i)

theorem merge_append_one :
    ∀ (i : ℕ) (w : List M), i + 1 < w.length → merge i (w ++ [1]) = merge i w ++ [1]
  | 0, [], h => by simp at h
  | 0, [_], h => by simp at h
  | 0, a :: b :: l, _ => by simp [merge]
  | i + 1, [], h => by simp at h
  | i + 1, a :: l, h => by
    have h' : i + 1 < l.length := by simp at h; omega
    simp [merge, merge_append_one i l h']

theorem merge_last :
    ∀ (n : ℕ) (w : List M), w.length = n + 2 → merge (n + 1) (w ++ [1]) = w
  | 0, [a, b], _ => by simp [merge]
  | 0, [], h => by simp at h
  | 0, [_], h => by simp at h
  | 0, _ :: _ :: _ :: _, h => by simp at h
  | n + 1, [], h => by simp at h
  | n + 1, a :: l, h => by
    have h' : l.length = n + 2 := by simp at h; omega
    simp [merge, merge_last n l h']

/-- The corrected identity of p. 73: `b'_(n+1) s_(n+1) - s_n b'_n = (-1)^(n+1) id`. -/
theorem contraction (n : ℕ) (w : List M) (hw : w.length = n + 2) :
    bprime (n + 1) (w ++ [1]) - sAfterBprime n w = Finsupp.single w ((-1 : ℤ) ^ (n + 1)) := by
  unfold bprime sAfterBprime
  rw [sum_range_succ, merge_last n w hw]
  have hsum : ∑ i ∈ range (n + 1), Finsupp.single (merge i (w ++ [1])) ((-1 : ℤ) ^ i) =
      ∑ i ∈ range (n + 1), Finsupp.single (merge i w ++ [1]) ((-1 : ℤ) ^ i) := by
    refine sum_congr rfl (fun i hi => ?_)
    rw [merge_append_one i w (by rw [hw]; simp at hi; omega)]
  rw [hsum, add_sub_cancel_left]

/-- Hence `(-1)^n s_n` is a chain contraction:
`b' ∘ ((-1)^(n+1) s_(n+1)) + ((-1)^n s_n) ∘ b' = id` on words of length `n + 2`. -/
theorem chain_contraction (n : ℕ) (w : List M) (hw : w.length = n + 2) :
    (-1 : ℤ) ^ (n + 1) • bprime (n + 1) (w ++ [1]) + (-1 : ℤ) ^ n • sAfterBprime n w =
      Finsupp.single w 1 := by
  have e : bprime (n + 1) (w ++ [1]) =
      sAfterBprime n w + Finsupp.single w ((-1 : ℤ) ^ (n + 1)) :=
    sub_eq_iff_eq_add'.mp (contraction n w hw)
  rw [e, smul_add, Finsupp.smul_single, smul_eq_mul]
  have h2 : (-1 : ℤ) ^ (n + 1) * (-1) ^ (n + 1) = 1 := by
    rw [← pow_add, ← two_mul, pow_mul]; norm_num
  have h3 : (-1 : ℤ) ^ (n + 1) • sAfterBprime n w + (-1) ^ n • sAfterBprime n w = 0 := by
    rw [← add_smul, pow_succ]; simp
  rw [h2, add_right_comm, h3, zero_add]

/-- The printed reading `b'_1 s_1 - s_0 b'_0 = id` fails (`n = 0`). -/
theorem printed_fails :
    bprime 1 (([1, 1] : List (Multiplicative ℕ)) ++ [1]) - sAfterBprime 0 [1, 1] ≠
      Finsupp.single [1, 1] 1 := by
  rw [contraction 0 _ rfl]
  intro h
  have := congrArg (fun f : List (Multiplicative ℕ) →₀ ℤ => f [1, 1]) h
  simp at this

end BensonCohomology.AcyclicHochschildContraction

#print axioms BensonCohomology.AcyclicHochschildContraction.contraction
#print axioms BensonCohomology.AcyclicHochschildContraction.chain_contraction
#print axioms BensonCohomology.AcyclicHochschildContraction.printed_fails
