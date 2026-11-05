import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Linarith

/-!
# Degeneracies of the free cyclic object `S[1] ⋈ X`

Section 2.14, Examples 4 (p. 87): the degeneracy maps of `S[1] ⋈ X` are
`s_i(t_n^j, x) = (t_(n+1)^j, s_(i-j) x)` for `i ≥ j` and
`s_i(t_n^j, x) = (t_(n+1)^(j+1), s_(i-j+n+1) x)` for `i < j` (the printed
exponent is `j - 1`).  They are the normal forms of `s_i ∘ t_n^j` in the
cyclic category, i.e. the identities
`s_i t_n^j = t_(n+1)^j s_(i-j)` (`j ≤ i ≤ n`) and
`s_i t_n^j = t_(n+1)^(j+1) s_(i-j+n+1)` (`i < j ≤ n`),
which we derive from the relations of p. 86:
`s_i t_n = t_(n+1) s_(i-1)` (`1 ≤ i ≤ n`) and `s_0 t_n = t_(n+1)^2 s_n`.

Notation.  `X n` is the set of `n`-simplices of a cyclic object, `s n i :
X n → X (n+1)` the degeneracy `s_i`, `t n : X n → X n`; `(t n)^[j]` is `t_n^j`.
Only the two relations above are assumed (no other relation of a cyclic
object is used).

* `shift`: `s_i t_n^k = t_(n+1)^k s_(i-k)` for `k ≤ i ≤ n`.
* `degeneracy_ge`: the case `j ≤ i` of Examples 4.
* `degeneracy_lt`: the case `i < j` with exponent `j + 1`.

Not covered: the face maps of Examples 4 (checked with the degeneracies in a
model of Connes' category in `checks/sage/chapter-2b.py`, `n ≤ 7`, where the
printed exponent `j - 1` is refuted), that these formulas define the free
cyclic object, and the homeomorphism `|S[1] ⋈ X| ≅ |S[1] × X|`.
-/

namespace BensonCohomology.CyclicDegeneracy

variable (X : ℕ → Type*) (s : ∀ n, ℕ → X n → X (n + 1)) (t : ∀ n, X n → X n)

theorem shift
    (hst : ∀ n i, 1 ≤ i → i ≤ n → ∀ x, s n i (t n x) = t (n + 1) (s n (i - 1) x))
    (n : ℕ) : ∀ (k i : ℕ), k ≤ i → i ≤ n → ∀ x,
      s n i ((t n)^[k] x) = (t (n + 1))^[k] (s n (i - k) x)
  | 0, i, _, _, x => by simp
  | k + 1, i, hk, hi, x => by
    have h1 : s n i ((t n)^[k + 1] x) = (t (n + 1))^[k] (s n (i - k) (t n x)) := by
      rw [Function.iterate_succ_apply]
      exact shift hst n k i (by omega) hi (t n x)
    have h2 : s n (i - k) (t n x) = t (n + 1) (s n (i - (k + 1)) x) := by
      rw [hst n (i - k) (by omega) (by omega)]
      congr 2
    rw [h1, h2, ← Function.iterate_succ_apply]

theorem degeneracy_ge
    (hst : ∀ n i, 1 ≤ i → i ≤ n → ∀ x, s n i (t n x) = t (n + 1) (s n (i - 1) x))
    (n i j : ℕ) (hji : j ≤ i) (hi : i ≤ n) (x : X n) :
    s n i ((t n)^[j] x) = (t (n + 1))^[j] (s n (i - j) x) :=
  shift X s t hst n j i hji hi x

theorem degeneracy_lt
    (hst : ∀ n i, 1 ≤ i → i ≤ n → ∀ x, s n i (t n x) = t (n + 1) (s n (i - 1) x))
    (hs0 : ∀ n x, s n 0 (t n x) = t (n + 1) (t (n + 1) (s n n x)))
    (n i j : ℕ) (hij : i < j) (hj : j ≤ n) (x : X n) :
    s n i ((t n)^[j] x) = (t (n + 1))^[j + 1] (s n (i + n + 1 - j) x) := by
  obtain ⟨m, rfl⟩ : ∃ m, j = i + (m + 1) := ⟨j - i - 1, by omega⟩
  have e1 : (t n)^[i + (m + 1)] x = (t n)^[i] (t n ((t n)^[m] x)) := by
    rw [Function.iterate_add_apply, Function.iterate_succ_apply']
  have e2 : s n i ((t n)^[i] (t n ((t n)^[m] x))) =
      (t (n + 1))^[i] (s n 0 (t n ((t n)^[m] x))) := by
    rw [shift X s t hst n i i le_rfl (by omega), Nat.sub_self]
  have e3 : s n n ((t n)^[m] x) = (t (n + 1))^[m] (s n (i + n + 1 - (i + (m + 1))) x) := by
    rw [shift X s t hst n m n (by omega) le_rfl]
    congr 2
    omega
  rw [e1, e2, hs0, e3]
  have e4 : ∀ y, (t (n + 1))^[i] (t (n + 1) (t (n + 1) ((t (n + 1))^[m] y))) =
      (t (n + 1))^[i + (m + 1) + 1] y := by
    intro y
    rw [← Function.iterate_succ_apply' (t (n + 1)) m, ← Function.iterate_succ_apply' (t (n + 1)),
      ← Function.iterate_add_apply]
    congr 1
  rw [e4]

end BensonCohomology.CyclicDegeneracy

#print axioms BensonCohomology.CyclicDegeneracy.degeneracy_ge
#print axioms BensonCohomology.CyclicDegeneracy.degeneracy_lt
