import Mathlib.Order.Preorder.Finite
import Mathlib.Order.Preorder.Chain
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Proposition 6.9.1 at the level of Euler characteristics, and cones

Benson, *Representations and Cohomology II*, Section 6.9, Proposition 6.9.1
(`prop:lefschetz-invariant-inversion`): for a finite `G`-poset `X`,
`Λ_G(X) = - ∑_{x ∈ X/G} ind_{Stab_G(x), G} Λ~_{Stab_G(x)}((x, -)_X)`.
The book's proof sorts the simplices `x_0 < ⋯ < x_n` of `|X|` by their least
element `x_0`; the simplices with `x_0 = x` are the chains of `(x, -)_X`
with `x` added in front, which shifts the dimension by one.  Taking the
mark at a subgroup `H` (the Euler characteristic of the fixed points, p. 220)
turns the identity into the same identity for the poset `X^H`, so its
content is the following statement about a finite poset `s`:

`χ(s) = ∑_{x ∈ s} (1 - χ((x, -)_s)) = - ∑_{x ∈ s} χ~((x, -)_s)`,

where `χ` is the Euler characteristic of the order complex, computed from
its simplices: `χ(s) = ∑ (-1)^(|c| - 1)` over the non-empty chains `c ⊆ s`.

Formalised here:

* `chains s`: the chains (totally ordered subsets, including `∅`) of `s`;
  `euler s`: `∑_{c ≠ ∅} (-1)^(|c| + 1)`; `upper s x`: `(x, -)_s`;
* `sum_chains_neg_one_pow`: `∑_{c ∈ chains s} (-1)^|c| = 1 - χ(s)` (the
  empty chain contributes `1`);
* `sum_least_eq`: the chains of `s` with least element `x` correspond to
  the chains of `(x, -)_s` by `d ↦ insert x d` (inverse `c ↦ c.erase x`),
  which raises the cardinality by one;
* `euler_eq_sum_upper`: the identity above (Proposition 6.9.1, marks);
* `euler_of_least` and `sum_reduced_upper_of_least`: if `s` has a least
  element (a cone, as `S_p(G) ∪ {1}` with the least element `1`, p. 218),
  then `χ(s) = 1` (the chains with and without the cone point cancel in
  pairs), so `∑_{x ∈ s} χ~((x, -)_s) = -1`.  Applied to `(S_p(G) ∪ {1})^H`
  this is the identity of Theorem 6.9.3 (`th:steinberg-inversion`) at the
  mark of `H`, once `(P, -)^H` is identified with `S_p(N_G(P)/P)^H` by
  Proposition 6.9.2.

Notation: `s` is the book's `X` (or a fixed-point poset `X^H`); the order
complex is described by its chains, as in Section 6.2.  Not covered: the
equivariant form in the Burnside ring (the induction from the stabilisers),
Proposition 6.9.2, and the homotopy statements; the marks of both sides of
Propositions 6.9.1, 6.9.2 and Theorem 6.9.3 are compared for small groups in
`checks/sage/chapter-6b.py`.
-/

namespace BensonCohomology.PosetEulerInversion

open Finset

variable {α : Type*} [PartialOrder α]

open scoped Classical in
/-- The chains of the order complex of `s` (including the empty chain). -/
noncomputable def chains (s : Finset α) : Finset (Finset α) :=
  s.powerset.filter (fun c => IsChain (· ≤ ·) (c : Set α))

open scoped Classical in
/-- The Euler characteristic of the order complex of `s`. -/
noncomputable def euler (s : Finset α) : ℤ :=
  ∑ c ∈ (chains s).filter (fun c => c.Nonempty), (-1 : ℤ) ^ (c.card + 1)

open scoped Classical in
/-- The open upper interval `(x, -)_s`. -/
noncomputable def upper (s : Finset α) (x : α) : Finset α := s.filter (fun y => x < y)

lemma mem_chains {s c : Finset α} :
    c ∈ chains s ↔ c ⊆ s ∧ IsChain (· ≤ ·) (c : Set α) := by
  classical
  simp [chains]

lemma empty_mem_chains (s : Finset α) : (∅ : Finset α) ∈ chains s := by
  rw [mem_chains]
  exact ⟨empty_subset _, by simp [IsChain]⟩

lemma mem_upper {s : Finset α} {x y : α} : y ∈ upper s x ↔ y ∈ s ∧ x < y := by
  classical
  simp [upper]

/-- The empty chain contributes `1`: `∑_{c ∈ chains s} (-1)^|c| = 1 - χ(s)`. -/
theorem sum_chains_neg_one_pow (s : Finset α) :
    ∑ c ∈ chains s, (-1 : ℤ) ^ c.card = 1 - euler s := by
  classical
  rw [euler, ← sum_filter_add_sum_filter_not (chains s) (fun c => c.Nonempty)]
  have hne : (chains s).filter (fun c => ¬ c.Nonempty) = {∅} := by
    ext c
    simp only [mem_filter, not_nonempty_iff_eq_empty, mem_singleton]
    constructor
    · rintro ⟨-, rfl⟩
      rfl
    · rintro rfl
      exact ⟨empty_mem_chains s, rfl⟩
  rw [hne, sum_singleton, card_empty, pow_zero]
  have : ∀ c ∈ (chains s).filter (fun c => c.Nonempty),
      (-1 : ℤ) ^ c.card = - (-1 : ℤ) ^ (c.card + 1) := by
    intro c _
    ring
  rw [sum_congr rfl this, sum_neg_distrib]
  ring

/-- A non-empty finite chain has a least element. -/
lemma exists_least {c : Finset α} (hc : IsChain (· ≤ ·) (c : Set α)) (hne : c.Nonempty) :
    ∃ x ∈ c, ∀ y ∈ c, x ≤ y := by
  obtain ⟨x, hx⟩ := c.exists_minimal hne
  refine ⟨x, hx.1, fun y hy => ?_⟩
  by_cases hxy : x = y
  · exact hxy ▸ le_rfl
  · rcases hc hx.1 hy hxy with h | h
    · exact h
    · exact hx.2 hy h

/-- At most one least element. -/
lemma least_unique {c : Finset α} {x x' : α} (hx : x ∈ c ∧ ∀ y ∈ c, x ≤ y)
    (hx' : x' ∈ c ∧ ∀ y ∈ c, x' ≤ y) : x = x' :=
  le_antisymm (hx.2 x' hx'.1) (hx'.2 x hx.1)

open scoped Classical in
/-- For fixed `x ∈ s`, the chains of `(x, -)_s` correspond to the chains of `s`
with least element `x` by `d ↦ insert x d`, and the sign `(-1)^|d|` becomes
`(-1)^(|c| + 1)`. -/
lemma sum_least_eq (s : Finset α) {x : α} (hx : x ∈ s) :
    ∑ c ∈ (chains s).filter (fun c => x ∈ c ∧ ∀ y ∈ c, x ≤ y), (-1 : ℤ) ^ (c.card + 1) =
      ∑ d ∈ chains (upper s x), (-1 : ℤ) ^ d.card := by
  symm
  refine sum_nbij' (fun d => insert x d) (fun c => c.erase x) ?_ ?_ ?_ ?_ ?_
  · intro d hd
    rw [mem_chains] at hd
    have hxd : ∀ y ∈ d, x < y := fun y hy => (mem_upper.mp (hd.1 hy)).2
    rw [mem_filter, mem_chains]
    refine ⟨⟨insert_subset hx (fun y hy => (mem_upper.mp (hd.1 hy)).1), ?_⟩,
      mem_insert_self _ _, ?_⟩
    · rw [coe_insert]
      exact hd.2.insert (fun b hb _ => Or.inl (hxd b hb).le)
    · intro y hy
      rcases mem_insert.mp hy with rfl | hy
      · exact le_rfl
      · exact (hxd y hy).le
  · intro c hc
    rw [mem_filter, mem_chains] at hc
    rw [mem_chains]
    refine ⟨fun y hy => ?_, hc.1.2.mono (by simp)⟩
    rw [mem_upper]
    obtain ⟨hyx, hyc⟩ := mem_erase.mp hy
    exact ⟨hc.1.1 hyc, lt_of_le_of_ne (hc.2.2 y hyc) (Ne.symm hyx)⟩
  · intro d hd
    rw [mem_chains] at hd
    have hxd : x ∉ d := fun h => lt_irrefl x (mem_upper.mp (hd.1 h)).2
    exact erase_insert hxd
  · intro c hc
    rw [mem_filter] at hc
    exact insert_erase hc.2.1
  · intro d hd
    rw [mem_chains] at hd
    have hxd : x ∉ d := fun h => lt_irrefl x (mem_upper.mp (hd.1 h)).2
    rw [card_insert_of_notMem hxd]
    ring

/-- **Proposition 6.9.1, marks**: `χ(s) = ∑_{x ∈ s} (1 - χ((x, -)_s))`. -/
theorem euler_eq_sum_upper (s : Finset α) :
    euler s = ∑ x ∈ s, (1 - euler (upper s x)) := by
  classical
  have step : ∀ c ∈ (chains s).filter (fun c => c.Nonempty),
      (-1 : ℤ) ^ (c.card + 1) =
        ∑ x ∈ s, if x ∈ c ∧ ∀ y ∈ c, x ≤ y then (-1 : ℤ) ^ (c.card + 1) else 0 := by
    intro c hc
    rw [mem_filter, mem_chains] at hc
    obtain ⟨x, hxc, hx⟩ := exists_least hc.1.2 hc.2
    rw [sum_eq_single x]
    · rw [ite_eq_left_of_eq_true _ _ (eq_true ⟨hxc, hx⟩)]
    · intro b _ hb
      refine ite_eq_right_of_eq_false _ _ (eq_false (fun hb' => ?_))
      exact hb (least_unique hb' ⟨hxc, hx⟩)
    · intro hxs
      exact absurd (hc.1.1 hxc) hxs
  rw [euler, sum_congr rfl step, sum_comm]
  refine sum_congr rfl (fun x hx => ?_)
  rw [← sum_chains_neg_one_pow, ← sum_least_eq s hx, sum_ite, sum_const_zero, add_zero,
    filter_filter]
  refine sum_congr ?_ (fun _ _ => rfl)
  ext c
  simp only [mem_filter]
  constructor
  · rintro ⟨hc, -, h⟩
    exact ⟨hc, h⟩
  · rintro ⟨hc, h⟩
    exact ⟨hc, ⟨x, h.1⟩, h⟩

/-- **Cones**: if `b ∈ s` is a least element of `s`, the chains with and without
`b` cancel in pairs, so `∑_{c ∈ chains s} (-1)^|c| = 0`. -/
theorem sum_chains_eq_zero_of_least (s : Finset α) {b : α} (hb : b ∈ s)
    (hleast : ∀ y ∈ s, b ≤ y) :
    ∑ c ∈ chains s, (-1 : ℤ) ^ c.card = 0 := by
  classical
  let g : Finset α → Finset α := fun c => if b ∈ c then c.erase b else insert b c
  refine sum_involution (fun c _ => g c) ?_ ?_ ?_ ?_
  · intro c _
    by_cases h : b ∈ c
    · simp only [g, h, ↓reduceIte]
      rw [← card_erase_add_one h, pow_succ]
      ring
    · simp only [g, h, ↓reduceIte, card_insert_of_notMem h, pow_succ]
      ring
  · intro c _ _ hgc
    by_cases h : b ∈ c
    · have h1 : g c = c.erase b := by simp only [g, h, ↓reduceIte]
      rw [h1] at hgc
      have h2 : b ∈ c.erase b := by rw [hgc]; exact h
      exact notMem_erase b c h2
    · have h1 : g c = insert b c := by simp only [g, h, ↓reduceIte]
      rw [h1] at hgc
      exact h (hgc ▸ mem_insert_self b c)
  · intro c hc
    rw [mem_chains] at hc ⊢
    by_cases h : b ∈ c
    · simp only [g, h, ↓reduceIte]
      exact ⟨(erase_subset b c).trans hc.1, hc.2.mono (by simp)⟩
    · simp only [g, h, ↓reduceIte]
      refine ⟨insert_subset hb hc.1, ?_⟩
      rw [coe_insert]
      exact hc.2.insert (fun y hy _ => Or.inl (hleast y (hc.1 hy)))
  · intro c _
    by_cases h : b ∈ c
    · simp [g, h]
    · simp [g, h]

/-- A poset with a least element has Euler characteristic `1`. -/
theorem euler_of_least (s : Finset α) {b : α} (hb : b ∈ s) (hleast : ∀ y ∈ s, b ≤ y) :
    euler s = 1 := by
  have h := sum_chains_neg_one_pow s
  rw [sum_chains_eq_zero_of_least s hb hleast] at h
  linarith

/-- **Theorem 6.9.3, marks**: for a poset with a least element (such as
`(S_p(G) ∪ {1})^H`), `∑_{x ∈ s} χ~((x, -)_s) = -1`, that is
`1 = - ∑_x χ~((x, -)_s)`. -/
theorem sum_reduced_upper_of_least (s : Finset α) {b : α} (hb : b ∈ s)
    (hleast : ∀ y ∈ s, b ≤ y) :
    ∑ x ∈ s, (euler (upper s x) - 1) = -1 := by
  have h := euler_eq_sum_upper s
  rw [euler_of_least s hb hleast] at h
  have : ∑ x ∈ s, (euler (upper s x) - 1) = - ∑ x ∈ s, (1 - euler (upper s x)) := by
    rw [← sum_neg_distrib]
    exact sum_congr rfl (fun x _ => by ring)
  rw [this, ← h]

end BensonCohomology.PosetEulerInversion

#print axioms BensonCohomology.PosetEulerInversion.euler_eq_sum_upper
#print axioms BensonCohomology.PosetEulerInversion.euler_of_least
#print axioms BensonCohomology.PosetEulerInversion.sum_reduced_upper_of_least
