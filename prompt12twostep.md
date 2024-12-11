Suppose you are an expert mathematician and an expert in Lean4 and Mathlib.

1. Your task is to generate an informal proof in natural language to prove the given informal theorem in natural language step by step. You will be provided with auxiliary information to improve the translation.
2. Then, generate the formal proof of the theorem. Utilize the informal proof written in the first task. Make sure you follow the principles of formal proving when you generate formal proofs.

## Auxiliary Helpful Information

There are two parts of information to assist in improving the generation.

* The formal theorem, which is the goal of the entire proof. It is written in Lean.
* The informal theorem. It is the explanation of the formal theorem in natural language.

## Principles of Formal Proofs

1. You should write a step of informal proof written in natural language, then write a step of formal proof wriiten in Lean4 corresponding to the informal guidance above.
  Example:
  Do NOT write
  ```lean
  example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := by
    have h1 : a * b * a = b * a⁻¹ * a := by exact mul_right_cancel_iff.mpr h
    rw [inv_mul_cancel_right] at h1
    rw [← h1, ← mul_assoc, ← mul_assoc, inv_mul_self, one_mul, h, mul_assoc b, inv_mul_self, mul_one]  
  ```
  Write
  ```lean
  example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := by
    -- introduce a new hypothesis h1 by multiply a on both sides
    have h1 : a * b * a = b * a⁻¹ * a := by exact mul_right_cancel_iff.mpr h
    -- then simplify h1
    rw [inv_mul_cancel_right] at h1
    -- substitute into the question, and prove it by rewriting:
    rw [← h1, ← mul_assoc, ← mul_assoc, inv_mul_self, one_mul, h, mul_assoc b, inv_mul_self, mul_one]
  ``` instead.

**Warning: The following examples are only used to demonstrate the format; their exact meaning is irrelevant.**

## Input1:

**Informal theorem:**
Show that every group $G$ with identity $e$ and such that $x * x=e$ for all $x \in G$ is Abelian.
**Formal theorem:**
```lean
import Mathlib

example {G : Type*} [Group G] (h: ∀ (x : G), x * x = 1) : CommGroup G := by
```

## Output1:

**Informal proof:**
Proof
1.To prove a group G is a commutative group, we just need to prove that for all a b in G, a * b = b * a.
2. And this is exact a calculation a * b = a * b * (b * a) * (b * a) = (a * (b * b) * a) * (b * a) = b * a.

**Formal proof:**
```lean
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
```

## Input2:

**Informal theorem:**
Suppose that $G$ is a group and $a, b \in G$ satisfy $a * b=b * a^{-1}$. Prove that $b * a=a^{-1} * b$.
**Formal theorem:**
```lean
import Mathlib

example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := sorry
```

## Output2:

**Informal proof:**
Introduce a new hypothesis $h1$ by multiplying $a$ on both sides, then simplify $h1$  , substitute into the question we are proving, and it can be proved by rewriting.

**Formal proof:**
```lean
import Mathlib

example {G : Type*} [Group G] (a b : G) (h : a * b = b * a⁻¹) : b * a = a⁻¹ * b := by
  -- introduce a new hypothesis h1 by multiply a on both sides
  have h1 : a * b * a = b * a⁻¹ * a := by exact mul_right_cancel_iff.mpr h
  -- then simplify h1
  rw [inv_mul_cancel_right] at h1
  -- substitute into the question, and prove it by rewriting:
  rw [← h1, ← mul_assoc, ← mul_assoc, inv_mul_self, one_mul, h, mul_assoc b, inv_mul_self, mul_one]
```

# Now, your input is: