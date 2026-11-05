import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.GroupWithZero.Defs

/-!
# Theorem 5.2.2: the final computation `ζ^r = β(x_1) ⋯ β(x_n) . (ζ'_1 ∘ ⋯ ∘ ζ'_n) = 0`

Benson, *Representations and Cohomology II*, Section 5.2, proof of
Theorem 5.2.2 (`th:nilpotent-restriction`, Quillen, Carlson): by the
Quillen–Venkov Theorem 5.2.1 (`th:quillen-venkov`) one has
`ζ^(2 r_i) = β(x_i) . ζ'_i` in `Ext^*_(kG)(M, M)`, and Serre's theorem gives
`β(x_1) ⋯ β(x_n) = 0`; since cup product with `β(x_i)` commutes with Yoneda
products,
`ζ^r = ζ^(2r_1) ∘ ⋯ ∘ ζ^(2r_n) = (β(x_1) . ζ'_1) ∘ ⋯ ∘ (β(x_n) . ζ'_n)
     = β(x_1) ⋯ β(x_n) . (ζ'_1 ∘ ⋯ ∘ ζ'_n) = 0`, `r = 2 ∑ r_i`.

Formalised here in an arbitrary (not necessarily commutative) monoid with
zero `A`, e.g. a ring under multiplication (the book's
`Ext^*_(kG)(M, M)` under Yoneda composition, ungraded), with the elements
`β(x_i) . 1_M` ("cup product with `β(x_i)`") assumed central in `A`:

* `prod_map_mul_of_central`: for a list of pairs `(b_i, z_i)` with every
  `b_i` central, `∏ (b_i z_i) = (∏ b_i) (∏ z_i)` (the order of the `z_i`
  is kept);
* `pow_two_mul_sum`: if `ζ^(2 r_i) = b_i z_i` for every entry `(r_i, b_i,
  z_i)` of the list, then `ζ^(2 ∑ r_i) = ∏ (b_i z_i)`;
* `pow_eq_zero_of_central_factors`: if `ζ^(2 r_i) = b_i z_i` for every
  entry `(r_i, b_i, z_i)` of the list, the `b_i` are central and
  `∏ b_i = 0`, then `ζ^(2 ∑ r_i) = 0`.

Notation: `b_i` = `β(x_i)` acting on `Ext^*(M, M)`, `z_i` = `ζ'_i`,
`r_i` as in the book.  Not covered: the Quillen–Venkov theorem itself and
Serre's theorem (their conclusions are the hypotheses here), the grading
and signs (the `β(x_i)` have even degree), and the reduction to `p`-groups;
the conclusions of both theorems are checked for small groups in
`checks/sage/chapter-5a.py` (Section 5.2).
-/

namespace BensonCohomology.CentralFactorPower

variable {A : Type*} [MonoidWithZero A]

theorem prod_map_mul_of_central (l : List (A × A))
    (h : ∀ p ∈ l, ∀ a : A, Commute p.1 a) :
    (l.map fun p => p.1 * p.2).prod =
      (l.map Prod.fst).prod * (l.map Prod.snd).prod := by
  induction l with
  | nil => simp
  | cons p l ih =>
    have hl : ∀ q ∈ l, ∀ a : A, Commute q.1 a :=
      fun q hq a => h q (List.mem_cons_of_mem p hq) a
    have hB : Commute (l.map Prod.fst).prod p.2 := by
      apply Commute.list_prod_left
      intro y hy
      obtain ⟨q, hq, rfl⟩ := List.mem_map.mp hy
      exact hl q hq p.2
    simp only [List.map_cons, List.prod_cons]
    rw [ih hl]
    simp only [mul_assoc]
    rw [← mul_assoc p.2, ← hB.eq, mul_assoc]

theorem pow_two_mul_sum (ζ : A) (l : List (ℕ × A × A))
    (hfac : ∀ t ∈ l, ζ ^ (2 * t.1) = t.2.1 * t.2.2) :
    ζ ^ (2 * (l.map Prod.fst).sum) = (l.map fun t => t.2.1 * t.2.2).prod := by
  induction l with
  | nil => simp
  | cons t l ih =>
    simp only [List.map_cons, List.sum_cons, List.prod_cons]
    rw [Nat.mul_add, pow_add, hfac t List.mem_cons_self,
      ih (fun u hu => hfac u (List.mem_cons_of_mem t hu))]

theorem pow_eq_zero_of_central_factors (ζ : A) (l : List (ℕ × A × A))
    (hfac : ∀ t ∈ l, ζ ^ (2 * t.1) = t.2.1 * t.2.2)
    (hcen : ∀ t ∈ l, ∀ a : A, Commute t.2.1 a)
    (hprod : (l.map fun t => t.2.1).prod = 0) :
    ζ ^ (2 * (l.map Prod.fst).sum) = 0 := by
  rw [pow_two_mul_sum ζ l hfac]
  have h2 := prod_map_mul_of_central (l.map fun t => t.2)
    (by
      intro p hp a
      obtain ⟨t, ht, rfl⟩ := List.mem_map.mp hp
      exact hcen t ht a)
  simp only [List.map_map] at h2
  rw [show (fun t : ℕ × A × A => t.2.1 * t.2.2) =
      (fun p : A × A => p.1 * p.2) ∘ (fun t => t.2) from rfl, h2]
  have h3 : (l.map (Prod.fst ∘ fun t : ℕ × A × A => t.2)).prod =
      (l.map fun t => t.2.1).prod := rfl
  rw [h3, hprod, zero_mul]

end BensonCohomology.CentralFactorPower

#print axioms BensonCohomology.CentralFactorPower.prod_map_mul_of_central
#print axioms BensonCohomology.CentralFactorPower.pow_two_mul_sum
#print axioms BensonCohomology.CentralFactorPower.pow_eq_zero_of_central_factors
