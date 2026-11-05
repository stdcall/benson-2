import Mathlib.Order.Basic
import Mathlib.Tactic.Linarith

/-!
# Section 1.8: the relations of the face and degeneracy maps, and the shuffle map

Book: D. J. Benson, *Representations and Cohomology II* (first paperback
edition 1998), printed p. 23, Section 1.8: the `i`th face map
`{0, …, n−1} → {0, …, n}`, `j ↦ j` (`j < i`), `j ↦ j + 1` (`j ≥ i`), and the
`i`th degeneracy map `{0, …, n+1} → {0, …, n}`, `j ↦ j` (`j ≤ i`),
`j ↦ j − 1` (`j > i`); "These maps satisfy the relations
`dᵢdⱼ = dⱼ₋₁dᵢ` (`i < j`), `dᵢsⱼ = sⱼ₋₁dᵢ` (`i < j`), `dᵢsⱼ = 1`
(`i = j` or `j + 1`), `dᵢsⱼ = sⱼdᵢ₋₁` (`i > j + 1`), `sᵢsⱼ = sⱼ₊₁sᵢ`
(`i ≤ j`)".  Printed p. 27, the Eilenberg–Zilber map
`x ⊗ y ↦ Σ ± (s_{ν_q} ⋯ s_{ν_1} x, s_{μ_p} ⋯ s_{μ_1} y)` for `x ∈ X_p`,
`y ∈ Y_q`, over the `(p, q)`-shuffles `(μ, ν)`.

Notation.  `δ i` and `σ i` are the book's face and degeneracy maps of the
category `Δ`, as functions `ℕ → ℕ` (the formulas of p. 23 on all of `ℕ`).
The simplicial operators are contravariant (`dᵢ = δᵢ*`, `sⱼ = σⱼ*`), so
`dᵢdⱼ = dⱼ₋₁dᵢ` is the identity `δⱼ ∘ δᵢ = δᵢ ∘ δⱼ₋₁` of maps of `Δ`, and so
on: `rel_dd`, `rel_ds_lt`, `rel_ds_eq`, `rel_ds_succ`, `rel_ds_gt`,
`rel_ss`.  In the Eilenberg–Zilber map the degeneracy `s_{ν_{k+1}}`
(0-based `ν k`) is applied to a simplex of dimension `p + k`, and `s_m` is
defined on `X_d` only for `m ≤ d`.

* `shuffle_defined`: for a strictly increasing sequence `ν 0 < ⋯ < ν (q−1)`
  with values in `{0, …, p + q − 1}` (the corrected reading of p. 27), every
  `ν k ≤ p + k`: all the degeneracies of the formula are defined.
* `shuffle_printed_undefined`: with values in `{1, …, n}`, `n = p + q`, the
  label `n` lies in `μ` or `ν` and is the last label applied; it is applied
  to an `(n−1)`-simplex: the printed formula is never defined.

Not covered: the sign of the shuffles and the chain map property (checked
in the universal case `Δ[p] × Δ[q]`, `p + q ≤ 6`, in
`checks/sage/chapter-1.py`, section 1.8).
-/

namespace BensonCohomology.SimplicialShuffle

/-- The `i`th face map of `Δ`. -/
def δ (i j : ℕ) : ℕ := if j < i then j else j + 1

/-- The `i`th degeneracy map of `Δ`. -/
def σ (i j : ℕ) : ℕ := if j ≤ i then j else j - 1

theorem rel_dd (i j k : ℕ) (h : i < j) : δ j (δ i k) = δ i (δ (j - 1) k) := by
  unfold δ; split_ifs <;> omega

theorem rel_ds_lt (i j k : ℕ) (h : i < j) : σ j (δ i k) = δ i (σ (j - 1) k) := by
  unfold δ σ; split_ifs <;> omega

theorem rel_ds_eq (j k : ℕ) : σ j (δ j k) = k := by
  unfold δ σ; split_ifs <;> omega

theorem rel_ds_succ (j k : ℕ) : σ j (δ (j + 1) k) = k := by
  unfold δ σ; split_ifs <;> omega

theorem rel_ds_gt (i j k : ℕ) (h : j + 1 < i) : σ j (δ i k) = δ (i - 1) (σ j k) := by
  unfold δ σ; split_ifs <;> omega

theorem rel_ss (i j k : ℕ) (h : i ≤ j) : σ j (σ i k) = σ i (σ (j + 1) k) := by
  unfold σ; split_ifs <;> omega

/-- A strictly increasing sequence gains at least one per step. -/
theorem gain (ν : ℕ → ℕ) (q : ℕ) (hmono : ∀ a b, a < b → b < q → ν a < ν b) :
    ∀ m k, k + m < q → ν k + m ≤ ν (k + m) := by
  intro m
  induction m with
  | zero => intro k _; simp
  | succ m ih =>
    intro k hk
    have h1 := ih k (by omega)
    have h2 := hmono (k + m) (k + m + 1) (by omega) (by omega)
    have : k + (m + 1) = k + m + 1 := by omega
    rw [this]
    omega

/-- With labels in `{0, …, p+q−1}` every degeneracy of the shuffle formula is
defined: `ν k ≤ p + k`. -/
theorem shuffle_defined (p q : ℕ) (ν : ℕ → ℕ)
    (hmono : ∀ a b, a < b → b < q → ν a < ν b) (hbound : ∀ k, k < q → ν k < p + q) :
    ∀ k, k < q → ν k ≤ p + k := by
  intro k hk
  have h := gain ν q hmono (q - 1 - k) k (by omega)
  have hlast := hbound (k + (q - 1 - k)) (by omega)
  omega

/-- With labels in `{1, …, n}` the label `n` is the last one of its list and is
applied to an `(n−1)`-simplex: `s_n` is not defined there. -/
theorem shuffle_printed_undefined (p q : ℕ) (ν : ℕ → ℕ) (hq : 0 < q)
    (hmono : ∀ a b, a < b → b < q → ν a < ν b) (hbound : ∀ k, k < q → ν k ≤ p + q)
    (hn : ∃ k, k < q ∧ ν k = p + q) : p + (q - 1) < ν (q - 1) := by
  obtain ⟨k, hk, hνk⟩ := hn
  rcases Nat.lt_or_ge k (q - 1) with hlt | hge
  · have := hmono k (q - 1) hlt (by omega)
    have := hbound (q - 1) (by omega)
    omega
  · have : k = q - 1 := by omega
    subst this
    omega

end BensonCohomology.SimplicialShuffle

#print axioms BensonCohomology.SimplicialShuffle.rel_dd
#print axioms BensonCohomology.SimplicialShuffle.rel_ds_lt
#print axioms BensonCohomology.SimplicialShuffle.rel_ds_eq
#print axioms BensonCohomology.SimplicialShuffle.rel_ds_succ
#print axioms BensonCohomology.SimplicialShuffle.rel_ds_gt
#print axioms BensonCohomology.SimplicialShuffle.rel_ss
#print axioms BensonCohomology.SimplicialShuffle.shuffle_defined
#print axioms BensonCohomology.SimplicialShuffle.shuffle_printed_undefined
