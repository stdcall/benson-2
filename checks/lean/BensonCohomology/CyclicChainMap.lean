import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Module.Defs
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Module
import Mathlib.Tactic.LinearCombination

/-!
# The map from `B_*(Λ)` to the cyclic double complex `CC_*(Λ)`

Section 2.13, p. 84: "There is an injective map of complexes
`B_*(Λ) → CC_*(Λ)` given by sending an element `x` in degree `(i, j)` to the
sum of `x` in degree `(2i, j - i)` and `(-1)^n s_n N x` in degree
`(2i - 1, j - i + 1)`" (the printed second place `(2i, j - i - 1)` has the
wrong total degree).  Here `n = j - i` is the Hochschild degree of `x`.  We
check the chain map property component by component.

Notation.  `A n` is `Λ^(⊗(n+1))` in Hochschild degree `n`; `b n, b' n :
A (n+1) → A n` are the differentials of p. 80, `s n : A n → A (n+1)` appends
`1`, `N n, ε n : A n → A n` are the operators of p. 81, and
`B n = (-1)^n ε_(n+1) s_n N_n : A n → A (n+1)` (p. 83).  In `CC_*(Λ)` the
even columns carry `b`, the odd ones `-b'`; `ε` goes from an odd column to the
even column on its left and `N` from an even column (≥ 2) to the odd one on its
left.  For `x` in column `i ≥ 1` of `B_*(Λ)` the total differential of `B_*`
is `b x + B x` (columns `i` and `i - 1`), and the image of `x` has the
components `x` (column `2i`) and `(-1)^n s N x` (column `2i - 1`).

Hypotheses (the identities of p. 81 and p. 73, checked in
`checks/sage/chapter-2b.py`; the last one is
`AcyclicHochschildContraction.contraction` in the indexing of p. 80):
* `hbN : b' ∘ N = N ∘ b`, `hNε : N ∘ ε = 0`,
* `hs : b'_n ∘ s_n = s_(n-1) ∘ b'_(n-1) + (-1)^n id` on `A n` (`n ≥ 1`), and
  `b'_0 ∘ s_0 = id` on `A 0`.

* `component_odd`: column `2i - 1` of `d(f x)` equals that of `f(d x)`:
  `N x - (-1)^n b'(s(N x)) = (-1)^(n-1) s(N(b x))` (`n ≥ 1`), and
  `N x - b'(s(N x)) = 0` (`n = 0`, `component_odd_zero`).
* `component_even`: column `2i - 2`: `ε((-1)^n s N x) = B x` (definition).
* `component_low`: column `2i - 3`: `(-1)^(n+1) s(N(B x)) = 0` (from `N ε = 0`).
The component in column `2i` is `b x` on both sides.

Not covered: the injectivity and the homology equivalence of the map, the
identities used as hypotheses (checked numerically), the double complex
`CC_*(Λ)` itself (its sign conventions are those printed on p. 81).
-/

namespace BensonCohomology.CyclicChainMap

variable (A : ℕ → Type*) [∀ n, AddCommGroup (A n)]
variable (b b' : ∀ n, A (n + 1) →+ A n) (s : ∀ n, A n →+ A (n + 1))
variable (N ε : ∀ n, A n →+ A n)

/-- Connes' operator `B = (-1)^n ε s N`. -/
def Bop (n : ℕ) (x : A n) : A (n + 1) := ((-1 : ℤ) ^ n) • ε (n + 1) (s n (N n x))

/-- Column `2i - 1`, Hochschild degree `n + 1 ≥ 1`. -/
theorem component_odd
    (hbN : ∀ n (y : A (n + 1)), b' n (N (n + 1) y) = N n (b n y))
    (hs : ∀ n (y : A (n + 1)), b' (n + 1) (s (n + 1) y) =
      s n (b' n y) + ((-1 : ℤ) ^ (n + 1)) • y)
    (n : ℕ) (x : A (n + 1)) :
    N (n + 1) x - ((-1 : ℤ) ^ (n + 1)) • b' (n + 1) (s (n + 1) (N (n + 1) x)) =
      ((-1 : ℤ) ^ n) • s n (N n (b n x)) := by
  have h : (-1 : ℤ) ^ (n * 2) = 1 := by
    rw [mul_comm, pow_mul]; norm_num
  rw [hs, hbN]
  match_scalars
  · ring_nf; simp [h]
  · ring

/-- Column `2i - 1`, Hochschild degree `0`. -/
theorem component_odd_zero (hs0 : ∀ y : A 0, b' 0 (s 0 y) = y) (x : A 0) :
    N 0 x - ((-1 : ℤ) ^ 0) • b' 0 (s 0 (N 0 x)) = 0 := by
  rw [hs0, pow_zero]
  module

/-- Column `2i - 2`: the horizontal map `ε` of the odd column applied to
`(-1)^n s N x` is `B x`. -/
theorem component_even (n : ℕ) (x : A n) :
    ε (n + 1) (((-1 : ℤ) ^ n) • s n (N n x)) = Bop A s N ε n x := by
  unfold Bop
  rw [map_zsmul]

/-- Column `2i - 3`: the image of `B x` has no component there, because
`N ε = 0`. -/
theorem component_low (hNε : ∀ n (y : A n), N n (ε n y) = 0) (n : ℕ) (x : A n) :
    ((-1 : ℤ) ^ (n + 1)) • s (n + 1) (N (n + 1) (Bop A s N ε n x)) = 0 := by
  unfold Bop
  rw [map_zsmul, hNε, smul_zero, map_zero, smul_zero]

end BensonCohomology.CyclicChainMap

#print axioms BensonCohomology.CyclicChainMap.component_odd
#print axioms BensonCohomology.CyclicChainMap.component_odd_zero
#print axioms BensonCohomology.CyclicChainMap.component_even
#print axioms BensonCohomology.CyclicChainMap.component_low
