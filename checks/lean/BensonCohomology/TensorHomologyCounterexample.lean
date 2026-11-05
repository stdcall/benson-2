import Mathlib.LinearAlgebra.TensorProduct.Associator
import Mathlib.Data.ZMod.Basic

/-!
# Proposition 3.4.4 needs `H₀(D)` flat: the counterexample

Benson, *Representations and Cohomology II*, Section 3.4, Proposition 3.4.4
(`prop:tensor-homology`), as printed: for `C` a complex of projective right
`Λ`-modules and `D` a complex of left `Λ`-modules, both concentrated in
non-negative degrees, `D` exact in positive degrees,
`H_*(C ⊗_Λ D) ≅ H_*(C) ⊗_Λ H₀(D)`; in particular, if `C` is also exact in
positive degrees, then so is `C ⊗_Λ D`.  Both claims fail for `Λ = ℤ`,
`C = (C₁ = ℤ --2--> C₀ = ℤ)` and `D = ℤ/2` in degree `0`.  The corrected
proposition adds the hypothesis that `H₀(D)` be flat (`ℤ/2` is not).

Formalised here (`C ⊗ D` has `(C ⊗ D)₁ = ℤ ⊗ ℤ/2`, `(C ⊗ D)₀ = ℤ ⊗ ℤ/2` and
the differential `dC ⊗ 1`; `C₂ = 0`, so `H₁` is the kernel of the
differential, both for `C` and for `C ⊗ D`):

* `ker_dC`: `H₁(C) = Ker(2 : ℤ → ℤ) = 0`, so `C` is exact in positive
  degrees (and `H₁(C) ⊗ ℤ/2` is trivial: `subsingleton_H1C_tensor`);
* `dCD_eq_zero`: `dC ⊗ 1 = 0` on `ℤ ⊗ ℤ/2`, hence `ker_dCD`:
  `H₁(C ⊗ D) = ℤ ⊗ ℤ/2`, which is non-trivial (`nontrivial_H1CD`, via
  `ℤ ⊗ ℤ/2 ≅ ℤ/2`);
* `not_exact`: `C ⊗ D` is not exact in degree `1`;
* `not_iso`: there is no isomorphism `H₁(C ⊗ D) ≅ H₁(C) ⊗ H₀(D)`.

Not covered: the corrected proposition itself (its proof by the spectral
sequence of the double complex `C ⊗_Λ D`, `E²_(p0) = H_p(C ⊗ H₀(D))`, and
flatness); it is checked on random complexes over `ℤ` and over group
algebras in `checks/sage/chapter-3a.py`.
-/

namespace BensonCohomology.TensorHomologyCounterexample

open TensorProduct

/-- The differential `C₁ = ℤ → C₀ = ℤ`, multiplication by `2`. -/
def dC : ℤ →ₗ[ℤ] ℤ := (2 : ℤ) • LinearMap.id

/-- The differential of `C ⊗ D` for `D = ℤ/2` in degree `0`: `dC ⊗ 1`. -/
noncomputable def dCD := LinearMap.rTensor (ZMod 2) dC

/-- `H₁(C) = Ker dC = 0`. -/
theorem ker_dC : LinearMap.ker dC = ⊥ := by
  ext x
  simp [dC]

instance subsingleton_H1C_tensor :
    Subsingleton (LinearMap.ker dC ⊗[ℤ] ZMod 2) := by
  have : Subsingleton (LinearMap.ker dC) := by
    rw [ker_dC]
    infer_instance
  infer_instance

theorem two_smul_zmod (y : ZMod 2) : (2 : ℤ) • y = 0 := by
  fin_cases y <;> rfl

/-- `dC ⊗ 1 = 0`: `(2x) ⊗ y = x ⊗ 2y = 0`. -/
theorem dCD_eq_zero : dCD = 0 := by
  apply TensorProduct.ext'
  intro x y
  rw [LinearMap.zero_apply, dCD, LinearMap.rTensor_tmul, dC,
    LinearMap.smul_apply, LinearMap.id_apply, TensorProduct.smul_tmul,
    two_smul_zmod, TensorProduct.tmul_zero]

/-- `H₁(C ⊗ D) = Ker(dC ⊗ 1)` is all of `ℤ ⊗ ℤ/2`. -/
theorem ker_dCD : LinearMap.ker dCD = ⊤ := by
  rw [dCD_eq_zero, LinearMap.ker_zero]

instance nontrivial_tensor : Nontrivial (ℤ ⊗[ℤ] ZMod 2) :=
  Equiv.nontrivial (TensorProduct.lid ℤ (ZMod 2)).toEquiv

theorem nontrivial_H1CD : Nontrivial (LinearMap.ker dCD) := by
  rw [ker_dCD]
  exact Equiv.nontrivial (Submodule.topEquiv (R := ℤ)
    (M := ℤ ⊗[ℤ] ZMod 2)).toEquiv

/-- `C ⊗ D` is not exact in degree `1` (its boundaries there are `0`). -/
theorem not_exact : LinearMap.ker dCD ≠ ⊥ := by
  rw [ker_dCD]
  exact top_ne_bot

/-- Proposition 3.4.4 as printed fails: `H₁(C ⊗ D) ≇ H₁(C) ⊗ H₀(D)`. -/
theorem not_iso :
    IsEmpty (LinearMap.ker dCD ≃ₗ[ℤ] LinearMap.ker dC ⊗[ℤ] ZMod 2) := by
  constructor
  intro e
  have := nontrivial_H1CD
  obtain ⟨a, b, hab⟩ := exists_pair_ne (LinearMap.ker dCD)
  exact hab (e.injective (Subsingleton.elim _ _))

end BensonCohomology.TensorHomologyCounterexample

#print axioms BensonCohomology.TensorHomologyCounterexample.ker_dC
#print axioms BensonCohomology.TensorHomologyCounterexample.subsingleton_H1C_tensor
#print axioms BensonCohomology.TensorHomologyCounterexample.two_smul_zmod
#print axioms BensonCohomology.TensorHomologyCounterexample.dCD_eq_zero
#print axioms BensonCohomology.TensorHomologyCounterexample.ker_dCD
#print axioms BensonCohomology.TensorHomologyCounterexample.nontrivial_tensor
#print axioms BensonCohomology.TensorHomologyCounterexample.nontrivial_H1CD
#print axioms BensonCohomology.TensorHomologyCounterexample.not_exact
#print axioms BensonCohomology.TensorHomologyCounterexample.not_iso
