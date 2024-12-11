Suppose you are an expert mathematician and an expert in Lean4 and Mathlib.

Your task is to generate an informal proof in natural language to prove the given informal theorem in natural language step by step. You will be provided with auxiliary information to improve the generation.

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

# Now, your input is: