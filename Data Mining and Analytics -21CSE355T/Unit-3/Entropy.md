# 3 Classroom Examples of Entropy in Decision Trees  
(For Data Mining / Machine Learning Class – Focus on How Entropy is Used)

These examples show exactly **how entropy is calculated and why it matters** when building a **Decision Tree** in data mining.  
Teachers usually explain these step-by-step on the board.

## Example 1: Very Pure Class (Low Entropy – Good Split Candidate)

**Dataset (small toy example – target class: Buy Computer?)**

| Age     | Income | Student | Buy_Computer |
|---------|--------|---------|--------------|
| Youth   | High   | Yes     | Yes          |
| Youth   | High   | Yes     | Yes          |
| Youth   | High   | Yes     | Yes          |
| Youth   | High   | Yes     | Yes          |

**Target class distribution** (Buy_Computer = Yes): 4 Yes, 0 No

**Entropy calculation**  
Total samples = 4  
p(Yes) = 4/4 = 1.0  
p(No)  = 0/4 = 0.0  

Entropy(S) = – [p(Yes) log₂ p(Yes) + p(No) log₂ p(No)]  
= – [1.0 × log₂(1.0) + 0 × log₂(0)]  
= – [1 × 0 + 0] = **0**

**What teacher explains**  
- Entropy = 0 → node is **pure** (all samples belong to same class)  
- This is the **best possible situation** after a split  
- No more splitting needed here → leaf node

## Example 2: Completely Mixed / Impure (Maximum Entropy – Bad Split)

**Dataset (another group after possible split)**

| Age     | Income | Student | Buy_Computer |
|---------|--------|---------|--------------|
| Youth   | Low    | No      | Yes          |
| Youth   | Low    | No      | No           |
| Youth   | Low    | No      | Yes          |
| Youth   | Low    | No      | No           |

**Target class distribution**: 2 Yes, 2 No

**Entropy calculation**  
p(Yes) = 2/4 = 0.5  
p(No)  = 2/4 = 0.5  

Entropy(S) = – [0.5 log₂ 0.5 + 0.5 log₂ 0.5]  
= – [0.5 × (–1) + 0.5 × (–1)]  
= – [–0.5 – 0.5] = **1 bit**

**What teacher explains**  
- Entropy = 1 → maximum uncertainty for 2 classes  
- This split is **very bad** because classes are still perfectly mixed  
- Decision tree algorithm will try to avoid splits that leave nodes like this

## Example 3: Real Split Evaluation (Information Gain)

**Full small dataset – before any split**

| ID | Age   | Income | Student | Buy_Computer |
|----|-------|--------|---------|--------------|
| 1  | Youth | High   | No      | No           |
| 2  | Youth | High   | Yes     | Yes          |
| 3  | Middle| High   | No      | Yes          |
| 4  | Old   | Medium | No      | Yes          |
| 5  | Old   | Low    | Yes     | Yes          |
| 6  | Old   | Low    | No      | No           |

**Root entropy (before split)**  
Classes: 4 Yes, 2 No  
p(Yes) = 4/6 ≈ 0.6667, p(No) = 2/6 ≈ 0.3333  

Entropy(S) = – [ (4/6) log₂(4/6) + (2/6) log₂(2/6) ] ≈ **0.918 bits**

**Suppose we split on “Student”**

- Student = Yes → 2 Yes, 0 No → Entropy = **0**  
- Student = No  → 2 Yes, 2 No → Entropy = **1**

**Weighted entropy after split**  
= (2/6) × 0 + (4/6) × 1 = **0.667 bits**

**Information Gain** = Entropy(before) – Entropy(after)  
= 0.918 – 0.667 ≈ **0.251 bits**

**What teacher explains**  
- Higher Information Gain → better attribute to split on  
- Here splitting on “Student” reduces entropy a lot → good split  
- Decision tree chooses the attribute with **highest Information Gain** at each step

## Quick Summary Table – What You Should Remember for Exams

| Situation                  | Entropy Value | Meaning in Decision Tree Context                     |
|----------------------------|---------------|------------------------------------------------------|
| All samples same class     | 0             | Pure node → stop splitting (leaf)                    |
| Classes perfectly balanced | 1 bit         | Maximum impurity for 2 classes → very bad split      |
| Mixed (real dataset)       | 0.5 – 0.95    | Normal starting point – need good splits to reduce   |
| After good split           | Lower than before | Information Gain > 0 → progress in tree building     |

**Key sentence teachers repeat**  
“Decision trees use entropy to measure impurity.  
We choose the split that **gives the highest Information Gain** (biggest reduction in entropy).”
