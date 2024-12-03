# Prompt for algebra translator

Suppose you are an expert mathematician and an expert in Lean4 and Mathlib.

Your task is to generate a formal proof in Lean4 according to the corresponding informal proof in natural language provided below. The formal proof must express the precise logic of the informal proof and you must use Lean4. You will be provided with auxiliary information to improve the translation.

## Auxiliary Helpful Information

There are two parts of information attached to the proof to assist in improving the generation.

* The formal theorem, which is the goal of the entire proof. It is written in Lean.
* The informal theorem. It is the explanation of the formal theorem in natural language.

**Warning: The following examples are only used to demonstrate the format; their exact meaning is irrelevant.**

## Input1:

**Informal theorem:**
Show that every group $G$ with identity $e$ and such that $x * x=e$ for all $x \in G$ is Abelian.
**Formal theorem:**
import Mathlib

example {G : Type*} [Group G] (h: ∀ (x : G), x * x = 1) : CommGroup G := by
**Informal proof:**
Proof
1.To prove a group G is a commutative group, we just need to prove that for all a b in G, a * b = b * a.
2. And this is exact a calculation a * b = a * b * (b * a) * (b * a) = (a * (b * b) * a) * (b * a) = b * a.

## Output1:

**Formal proof:**
import Mathlib
import Mathlib.Tactic
example {G : Type*} [Group G] (h: ∀ (x : G), x * x = 1) : CommGroup G := by
  --To prove a group G is a commutative group, we just need to prove that for all a b in G, a * b = b * a.
  constructor
  intro a b
  let h1 := h a
  let h2 := h b
  let h3 := h (b * a)
  --And this is exact a calculation a * b = a * b * (b * a) * (b * a) = (a * (b * b) * a) * (b * a) = b * a.
  calc
    _ = a * b * (b * a) * (b * a) := by nth_rw 1 [←mul_one b]; rw [← h3]; group
    _ = b * a := by rw [← mul_assoc (a * b), mul_assoc a, h2, mul_one, h1, one_mul]

## Input2:

**Informal theorem:**
Suppose that $G$ is a group and $a, b \in G$ satisfy $a * b=b * a^{-1}$. Prove that $b * a=a^{-1} * b$.
**Formal theorem:**
import Mathlib

example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := by
**Informal proof:**
  introduce a new hypothesis $h1$ by multiplying $a$ on both sides, then simplify $h1$  , substitute into the question we are proving, and it can be proved by rewriting.

## Output2:

**Formal proof:**
import Mathlib

example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := by
  -- introduce a new hypothesis h1 by multiply a on both sides
  have h1 : a * b * a = b * a⁻¹ * a := by exact mul_right_cancel_iff.mpr h
  -- then simplify h1
  rw [inv_mul_cancel_right] at h1
  -- substitute into the question, and prove it by rewriting:
  rw [← h1, ← mul_assoc, ← mul_assoc, inv_mul_self, one_mul, h, mul_assoc b, inv_mul_self, mul_one]

# Now, your input is: