import Mathlib.LinearAlgebra.Isomorphisms

/-!
# Lemma 3.2.5: `g` induces `Im h / Im f ≅ Im k`

Benson, *Representations and Cohomology II*, Section 3.2, Lemma 3.2.5
(`lem:image-quotient`), used for Theorem 3.2.6 (`th:page-as-image`) and
Theorem 3.2.9 (`th:filtration-quotients`): given a commutative diagram

```
        D
     a↗ |h ↘k
   A --f--> B --g--> C
```

(`h ∘ a = f`, `g ∘ h = k`) with the bottom row exact (`Im f = Ker g`), the
map `g` induces an isomorphism `Im(h) / Im(f) ≅ Im(k)`.

Formalised here, for modules over any ring `R` (abelian groups: `R = ℤ`):

* `range_f_le_range_h`: `Im f ⊆ Im h` (from `h ∘ a = f`), so that
  `Im f` is a submodule of `Im h`; in Lean it is
  `(range f).comap (range h).subtype`, and `comap_range_f` shows that this
  submodule is exactly `Im f` seen inside `Im h`;
* `gOnImage`: `g` restricted to `Im h`; its kernel is `Im f` inside `Im h`
  (`ker_gOnImage`, by exactness) and its range is `Im k`
  (`range_gOnImage`, by `g ∘ h = k`);
* `imageQuotientEquiv`: the isomorphism `Im(h) / Im(f) ≃ Im(k)` (the book's
  proof: `Im h / Im f = Im h / Ker g ≅ Im(g h) = Im k`), and
  `imageQuotientEquiv_mk`: it sends the class of `h(x)` to `k(x)`, i.e. it
  is induced by `g`.

Notation: `A, B, C, D, f, g, h, k` as in the book; `a : A → D` is the
unlabelled arrow.  Not covered: the identification of the diagrams of
Theorems 3.2.6 and 3.2.9 (exactness of the long exact sequences of the
triples and the description of `E_n` by Proposition 3.2.4); these are
checked numerically in `checks/sage/chapter-3a.py`.
-/

namespace BensonCohomology.ImageQuotient

variable {R A B C D : Type*} [Ring R]
  [AddCommGroup A] [Module R A] [AddCommGroup B] [Module R B]
  [AddCommGroup C] [Module R C] [AddCommGroup D] [Module R D]

/-- `Im f ⊆ Im h` when `f = h ∘ a`. -/
theorem range_f_le_range_h (a : A →ₗ[R] D) (f : A →ₗ[R] B) (h : D →ₗ[R] B)
    (ha : h ∘ₗ a = f) : LinearMap.range f ≤ LinearMap.range h := by
  rw [← ha]
  exact LinearMap.range_comp_le_range a h

/-- The submodule `(range f).comap (range h).subtype` of `Im h` is `Im f`:
its image in `B` is `Im f`. -/
theorem comap_range_f (a : A →ₗ[R] D) (f : A →ₗ[R] B) (h : D →ₗ[R] B)
    (ha : h ∘ₗ a = f) :
    ((LinearMap.range f).comap (LinearMap.range h).subtype).map
      (LinearMap.range h).subtype = LinearMap.range f := by
  rw [Submodule.map_comap_subtype]
  exact inf_eq_right.mpr (range_f_le_range_h a f h ha)

/-- `g` restricted to `Im h`. -/
def gOnImage (g : B →ₗ[R] C) (h : D →ₗ[R] B) : LinearMap.range h →ₗ[R] C :=
  g ∘ₗ (LinearMap.range h).subtype

theorem range_gOnImage (g : B →ₗ[R] C) (h : D →ₗ[R] B) (k : D →ₗ[R] C)
    (hk : g ∘ₗ h = k) : LinearMap.range (gOnImage g h) = LinearMap.range k := by
  rw [gOnImage, LinearMap.range_comp, Submodule.range_subtype,
    ← LinearMap.range_comp, hk]

theorem ker_gOnImage (f : A →ₗ[R] B) (g : B →ₗ[R] C) (h : D →ₗ[R] B)
    (hexact : LinearMap.range f = LinearMap.ker g) :
    LinearMap.ker (gOnImage g h) =
      (LinearMap.range f).comap (LinearMap.range h).subtype := by
  rw [gOnImage, LinearMap.ker_comp, hexact]

/-- Lemma 3.2.5: `g` induces `Im(h) / Im(f) ≅ Im(k)`. -/
noncomputable def imageQuotientEquiv (f : A →ₗ[R] B) (g : B →ₗ[R] C)
    (h : D →ₗ[R] B) (k : D →ₗ[R] C) (hk : g ∘ₗ h = k)
    (hexact : LinearMap.range f = LinearMap.ker g) :
    (LinearMap.range h ⧸ (LinearMap.range f).comap (LinearMap.range h).subtype)
      ≃ₗ[R] LinearMap.range k :=
  (Submodule.quotEquivOfEq _ _ (ker_gOnImage f g h hexact)).symm.trans
    ((gOnImage g h).quotKerEquivRange.trans
      (LinearEquiv.ofEq _ _ (range_gOnImage g h k hk)))

/-- The isomorphism is induced by `g`: the class of `h x` goes to `k x`. -/
theorem imageQuotientEquiv_mk (f : A →ₗ[R] B) (g : B →ₗ[R] C)
    (h : D →ₗ[R] B) (k : D →ₗ[R] C) (hk : g ∘ₗ h = k)
    (hexact : LinearMap.range f = LinearMap.ker g) (x : D) :
    ((imageQuotientEquiv f g h k hk hexact
        (Submodule.Quotient.mk ⟨h x, LinearMap.mem_range_self h x⟩) :
          LinearMap.range k) : C) = k x := by
  have h1 : ((imageQuotientEquiv f g h k hk hexact
      (Submodule.Quotient.mk ⟨h x, LinearMap.mem_range_self h x⟩) :
        LinearMap.range k) : C) = g (h x) := by
    rfl
  rw [h1, ← LinearMap.comp_apply, hk]

end BensonCohomology.ImageQuotient

#print axioms BensonCohomology.ImageQuotient.range_f_le_range_h
#print axioms BensonCohomology.ImageQuotient.comap_range_f
#print axioms BensonCohomology.ImageQuotient.range_gOnImage
#print axioms BensonCohomology.ImageQuotient.ker_gOnImage
#print axioms BensonCohomology.ImageQuotient.imageQuotientEquiv
#print axioms BensonCohomology.ImageQuotient.imageQuotientEquiv_mk
