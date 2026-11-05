import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Group.Pi.Basic
import Mathlib.Algebra.Group.TypeTags.Basic
import Mathlib.Algebra.Group.Int.Defs
import Mathlib.Algebra.Group.PUnit

/-!
# Theorem 1.4.3 (Whitehead), its proof: the exact sequence of the mapping cylinder

Book: D. J. Benson, *Representations and Cohomology II* (first paperback
edition 1998), printed p. 12, proof of Theorem 1.4.3: "By the above long
exact sequence, (A) is equivalent to the statement that `π_i(M_f, X, x₀) = 0`
for `i ≤ n`, and (B) is equivalent to the statement that `H_i(M_f, X) = 0`
for `i ≤ n`."  The book prints `i < n` twice; this file proves the
equivalence with `i ≤ n` and refutes it with `i < n`.

Notation.  A segment of the long exact sequence of p. 11
`⋯ → A (i+1) →∂ B i →f C i →j A i → ⋯` is a `LongExact` structure:
`B i = π_i(X, x₀)` and `C i = π_i(Y, y₀)` are groups, `f i = f_*` are
homomorphisms, `A i = π_i(M_f, X, x₀)` (`i ≥ 1`) are pointed sets with base
point `base i`, `j` and `∂` are maps of pointed sets; exactness is "kernel =
image" at `C i` (`i ≥ 1`), at `A (i+1)` and at `B i`, as in the Remark after
Proposition 1.2.7.  The same structure with abelian groups `A i` gives the
homology statement (B).  (A) is stated without the degree-zero condition
"`f_*` onto on `π₀`", which is automatic for the path connected `X`, `Y`
of the theorem and is not a consequence of the vanishing of the `A i`.

* `exact_step`: in `A (i+1) →∂ B i →f C i →j A i`, if `f i` is onto and `f`
  has trivial kernel in degree `i - 1`, then `A i` is trivial; conversely.
* `whitehead_exact`: (A) `⇔` `A i` trivial for `1 ≤ i ≤ n` (the corrected
  reading).
* `printed_fails`: the printed reading (`1 ≤ i < n`) fails already for
  `n = 1` (the sequence of `f : point → S¹`: `B = 1`, `C = A = ℤ`).

Not covered: the construction of the long exact sequences, the mapping
cylinder and the relative Hurewicz theorem used afterwards; the homology
half is checked on examples in `checks/sage/chapter-1.py` (section 1.4).
-/

namespace BensonCohomology.WhiteheadExactness

/-- A long exact sequence `⋯ → A (i+1) → B i → C i → A i → ⋯` with groups
`B i`, `C i`, homomorphisms `f i` and pointed sets `A i` (`i ≥ 1`). -/
structure LongExact where
  B : ℕ → Type
  C : ℕ → Type
  A : ℕ → Type
  [gB : ∀ i, Group (B i)]
  [gC : ∀ i, Group (C i)]
  base : ∀ i, A i
  f : ∀ i, B i →* C i
  j : ∀ i, C i → A i
  d : ∀ i, A (i + 1) → B i
  exact_C : ∀ i, 1 ≤ i → ∀ c, j i c = base i ↔ ∃ b, f i b = c
  exact_A : ∀ i, ∀ a, d i a = 1 ↔ ∃ c, j (i + 1) c = a
  exact_B : ∀ i, ∀ b, f i b = 1 ↔ ∃ a, d i a = b

attribute [instance] LongExact.gB LongExact.gC

variable (S : LongExact)

/-- The base point of `A (i+1)` goes to `1`. -/
theorem d_base (i : ℕ) : S.d i (S.base (i + 1)) = 1 := by
  rw [S.exact_A]
  refine ⟨1, ?_⟩
  exact (S.exact_C (i + 1) (Nat.succ_pos i) 1).2 ⟨1, map_one _⟩

/-- A homomorphism with trivial kernel is injective. -/
theorem injective_of_ker {G H : Type} [Group G] [Group H] (φ : G →* H)
    (h : ∀ g, φ g = 1 → g = 1) : Function.Injective φ := by
  intro x y hxy
  have : φ (x * y⁻¹) = 1 := by rw [map_mul, map_inv, hxy, mul_inv_cancel]
  have := h _ this
  calc x = x * y⁻¹ * y := by rw [inv_mul_cancel_right]
    _ = y := by rw [this, one_mul]

/-- One step: `f i` onto and `f (i-1)` with trivial kernel give `A i = *`. -/
theorem exact_step (i : ℕ) (hon : Function.Surjective (S.f (i + 1)))
    (hker : ∀ b, S.f i b = 1 → b = 1) (a : S.A (i + 1)) : a = S.base (i + 1) := by
  have h1 : S.f i (S.d i a) = 1 := (S.exact_B i _).2 ⟨a, rfl⟩
  have h2 : S.d i a = 1 := hker _ h1
  obtain ⟨c, hc⟩ := (S.exact_A i a).1 h2
  obtain ⟨b, hb⟩ := hon c
  rw [← hc]
  exact (S.exact_C (i + 1) (Nat.succ_pos i) c).2 ⟨b, hb⟩

/-- The converse step: `A (i+1) = *` makes `f (i+1)` onto and `f i` injective. -/
theorem exact_step_converse (i : ℕ) (htriv : ∀ a : S.A (i + 1), a = S.base (i + 1)) :
    Function.Surjective (S.f (i + 1)) ∧ Function.Injective (S.f i) := by
  constructor
  · intro c
    obtain ⟨b, hb⟩ := (S.exact_C (i + 1) (Nat.succ_pos i) c).1 (htriv _)
    exact ⟨b, hb⟩
  · apply injective_of_ker
    intro b hb
    obtain ⟨a, ha⟩ := (S.exact_B i b).1 hb
    rw [← ha, htriv a, d_base]

/-- The corrected proof of Theorem 1.4.3: (A) `f_*` injective for `i < n` and
onto for `1 ≤ i ≤ n` iff `A i = π_i(M_f, X, x₀)` is trivial for `1 ≤ i ≤ n`. -/
theorem whitehead_exact (n : ℕ) :
    ((∀ i, i < n → Function.Injective (S.f i)) ∧
      (∀ i, 1 ≤ i → i ≤ n → Function.Surjective (S.f i))) ↔
    ∀ i, 1 ≤ i → i ≤ n → ∀ a : S.A i, a = S.base i := by
  constructor
  · rintro ⟨hinj, hsurj⟩ i hi1 hin a
    obtain ⟨k, rfl⟩ : ∃ k, i = k + 1 := ⟨i - 1, by omega⟩
    refine exact_step S k (hsurj _ hi1 hin) ?_ a
    intro b hb
    exact hinj k (by omega) (hb.trans (map_one _).symm)
  · intro h
    refine ⟨fun i hi => ?_, fun i hi1 hin => ?_⟩
    · exact (exact_step_converse S i (h (i + 1) (by omega) (by omega))).2
    · obtain ⟨k, rfl⟩ : ∃ k, i = k + 1 := ⟨i - 1, by omega⟩
      exact (exact_step_converse S k (h (k + 1) hi1 hin)).1

/-- The sequence of `f : point → S¹` in degrees `≥ 0`: `B i = 1`,
`C i = A i = ℤ` (written multiplicatively), `j = id`, `∂ = 1`. -/
def pointToCircle : LongExact where
  B := fun _ => PUnit
  C := fun _ => Multiplicative ℤ
  A := fun _ => Multiplicative ℤ
  base := fun _ => 1
  f := fun _ => 1
  j := fun _ c => c
  d := fun _ _ => 1
  exact_C := by
    intro i _ c
    constructor
    · intro h
      exact ⟨PUnit.unit, h.symm⟩
    · rintro ⟨b, hb⟩
      exact hb.symm
  exact_A := by
    intro i a
    exact ⟨fun _ => ⟨a, rfl⟩, fun _ => rfl⟩
  exact_B := by
    intro i b
    exact ⟨fun _ => ⟨1, rfl⟩, fun _ => rfl⟩

/-- The printed reading of the proof ("for `i < n`") is false: for `n = 1`
the condition on the `A i` is empty, but `f₁ : 1 → ℤ` is not onto. -/
theorem printed_fails :
    ¬ ∀ (S : LongExact) (n : ℕ),
      ((∀ i, i < n → Function.Injective (S.f i)) ∧
        (∀ i, 1 ≤ i → i ≤ n → Function.Surjective (S.f i))) ↔
      ∀ i, 1 ≤ i → i < n → ∀ a : S.A i, a = S.base i := by
  intro h
  have := (h pointToCircle 1).2 (fun i h1 h2 => absurd h2 (by omega))
  obtain ⟨b, hb⟩ := this.2 1 (Nat.le_refl 1) (Nat.le_refl 1) (Multiplicative.ofAdd (1 : ℤ))
  have h1 : (1 : Multiplicative ℤ) = Multiplicative.ofAdd (1 : ℤ) := hb
  have h2 : (0 : ℤ) = 1 := congrArg Multiplicative.toAdd h1
  exact absurd h2 (by decide)

end BensonCohomology.WhiteheadExactness

#print axioms BensonCohomology.WhiteheadExactness.exact_step
#print axioms BensonCohomology.WhiteheadExactness.exact_step_converse
#print axioms BensonCohomology.WhiteheadExactness.whitehead_exact
#print axioms BensonCohomology.WhiteheadExactness.printed_fails
