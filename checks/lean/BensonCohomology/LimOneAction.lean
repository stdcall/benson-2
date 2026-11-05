import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Group.Pi.Basic
import Mathlib.Algebra.Group.Hom.Basic
import Mathlib.Tactic.Group
import Mathlib.Tactic.Abel

/-!
# Section 1.9: `lim¹` of an inverse system of groups as an orbit set

Book: D. J. Benson, *Representations and Cohomology II* (first paperback
edition 1998), printed p. 28, Section 1.9: "If `⋯ → G₂ →α₂ G₁ →α₁ G₀` are
groups and homomorphisms, then the group `∏ Gₙ` acts on the set `∏ Gₙ` via
`(g₀, g₁, …)(x₀, x₁, …) = (g₀ x₀ α₁(g₁)⁻¹, g₁ x₁ α₂(g₂)⁻¹, …)` and
`lim¹ Gₙ` is the quotient of the set `∏ Gₙ` by the equivalence relation
defined by this action. It is only a pointed set, and not a group in
general, but if the `Gₙ` are abelian then `lim¹ Gₙ` is an abelian group."
The same definition is Goerss–Jardine, *Simplicial homotopy theory*,
Section VI.2 (before Lemma 2.12).

Notation.  `G n` is `Gₙ`; `α n : G (n+1) →* G n` is the book's `α_{n+1}`;
elements of `∏ Gₙ` are functions `∀ n, G n`.

* `act`, `act_one`, `act_mul`: the formula is a left action.
* `act_one_eq_one_iff`: the stabiliser of `(1, 1, …)` is `lim Gₙ`, the
  compatible sequences.
* `orbitRel`, `LimOne`: the equivalence relation and the pointed set `lim¹`.
* `limOne_trivial_of_surjective`: if every `αₙ` is onto, every element is
  in the orbit of `(1, 1, …)`, so `lim¹ Gₙ` is a point (Goerss–Jardine,
  Lemma VI.2.12 (2); the six-term sequence of p. 28 rests on this kind of
  step).
* Abelian case (additive notation, `β n : A (n+1) →+ A n`): `addAct_eq`
  (`g · x = x + ∂ g` with `∂(g)ₙ = gₙ − β(gₙ₊₁)`) and `addOrbit_iff`: two
  sequences are in one orbit iff their difference lies in the range of `∂`,
  so `lim¹` is the cokernel of `∂`, an abelian group, as for Volume I's
  `lim¹` (the derived functor of the inverse limit, Volume I, Section 4.1).

Not covered: the six-term exact sequence itself and Theorem 1.9.1 (Milnor;
Bousfield–Kan, Chapter IX §3); a consistency check of Theorem 1.9.1 for
`BZ/2` is in `checks/sage/chapter-1.py` (section 1.9).
-/

namespace BensonCohomology.LimOneAction

section NonAbelian

variable {G : ℕ → Type*} [∀ n, Group (G n)] (α : ∀ n, G (n + 1) →* G n)

/-- The action of `∏ Gₙ` on the set `∏ Gₙ` of p. 28. -/
def act (g x : ∀ n, G n) : ∀ n, G n :=
  fun n => g n * x n * (α n (g (n + 1)))⁻¹

theorem act_one (x : ∀ n, G n) : act α 1 x = x := by
  funext n
  simp [act]

theorem act_mul (g h x : ∀ n, G n) : act α (g * h) x = act α g (act α h x) := by
  funext n
  simp only [act, Pi.mul_apply, map_mul, mul_inv_rev]
  group

/-- The stabiliser of `(1, 1, …)` is the inverse limit. -/
theorem act_one_eq_one_iff (g : ∀ n, G n) :
    act α g 1 = 1 ↔ ∀ n, g n = α n (g (n + 1)) := by
  constructor
  · intro h n
    have := congrFun h n
    simp only [act, Pi.one_apply, mul_one] at this
    exact mul_inv_eq_one.1 this
  · intro h
    funext n
    simp only [act, Pi.one_apply, mul_one]
    exact mul_inv_eq_one.2 (h n)

/-- The equivalence relation "in the same orbit". -/
def orbitRel : Setoid (∀ n, G n) where
  r x y := ∃ g, act α g x = y
  iseqv := by
    refine ⟨fun x => ⟨1, act_one α x⟩, ?_, ?_⟩
    · rintro x y ⟨g, rfl⟩
      refine ⟨g⁻¹, ?_⟩
      rw [← act_mul, inv_mul_cancel, act_one]
    · rintro x y z ⟨g, rfl⟩ ⟨h, rfl⟩
      exact ⟨h * g, act_mul α h g x⟩

/-- `lim¹ Gₙ`, a pointed set with base point the class of `(1, 1, …)`. -/
def LimOne := Quotient (orbitRel α)

/-- The sequence `g₀ = 1`, `gₙ₊₁` a preimage of `gₙ xₙ` under `αₙ`. -/
noncomputable def killer (hα : ∀ n, Function.Surjective (α n)) (x : ∀ n, G n) :
    (n : ℕ) → G n
  | 0 => 1
  | n + 1 => Classical.choose (hα n (killer hα x n * x n))

/-- If every `αₙ` is onto, then every `x` is in the orbit of `1`. -/
theorem limOne_trivial_of_surjective (hα : ∀ n, Function.Surjective (α n))
    (x : ∀ n, G n) : ∃ g, act α g x = 1 := by
  refine ⟨killer α hα x, ?_⟩
  funext n
  have h : α n (killer α hα x (n + 1)) = killer α hα x n * x n :=
    Classical.choose_spec (hα n (killer α hα x n * x n))
  simp only [act, Pi.one_apply, h, mul_inv_cancel]

end NonAbelian

section Abelian

variable {A : ℕ → Type*} [∀ n, AddCommGroup (A n)] (β : ∀ n, A (n + 1) →+ A n)

/-- The action in additive notation: `g · x = (gₙ + xₙ − β(gₙ₊₁))ₙ`. -/
def addAct (g x : ∀ n, A n) : ∀ n, A n :=
  fun n => g n + x n - β n (g (n + 1))

/-- `∂(g)ₙ = gₙ − β(gₙ₊₁)`, a homomorphism `∏ Aₙ → ∏ Aₙ`. -/
def boundary : (∀ n, A n) →+ (∀ n, A n) where
  toFun g n := g n - β n (g (n + 1))
  map_zero' := by
    funext n
    simp
  map_add' g h := by
    funext n
    simp only [Pi.add_apply, map_add]
    abel

theorem addAct_eq (g x : ∀ n, A n) : addAct β g x = x + boundary β g := by
  funext n
  simp only [addAct, boundary, AddMonoidHom.coe_mk, ZeroHom.coe_mk, Pi.add_apply]
  abel

/-- In the abelian case the orbits are the cosets of the range of `∂`:
`lim¹ Aₙ` is the cokernel of `∂`. -/
theorem addOrbit_iff (x y : ∀ n, A n) :
    (∃ g, addAct β g x = y) ↔ ∃ g, boundary β g = y - x := by
  constructor
  · rintro ⟨g, rfl⟩
    refine ⟨g, ?_⟩
    rw [addAct_eq]
    abel
  · rintro ⟨g, hg⟩
    refine ⟨g, ?_⟩
    rw [addAct_eq, hg]
    abel

end Abelian

end BensonCohomology.LimOneAction

#print axioms BensonCohomology.LimOneAction.act_one
#print axioms BensonCohomology.LimOneAction.act_mul
#print axioms BensonCohomology.LimOneAction.act_one_eq_one_iff
#print axioms BensonCohomology.LimOneAction.limOne_trivial_of_surjective
#print axioms BensonCohomology.LimOneAction.addAct_eq
#print axioms BensonCohomology.LimOneAction.addOrbit_iff
