# B. Information Gain (ID3 Algorithm) – Readable Component Breakdown

**Formula**  
Gain(S, A) = H(S) − Σ ( |Sᵥ| / |S| ) × H(Sᵥ)  
(for each possible value v of attribute A)

This is the **most important formula** in the ID3 decision tree algorithm.  
It tells us **which attribute is best to split on** right now.

## Readable Pronunciation & Component Breakdown

| Symbol / Part                  | How to read it aloud                                      | Meaning in simple words                                                                 | Notes / Why it matters                                      |
|--------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| **Gain(S, A)**                 | "Information Gain of attribute A on set S"                | How much **uncertainty is reduced** if we split using attribute A                      | Higher gain = better attribute to choose next               |
| **H(S)**                       | "Entropy of the whole set S" or "H of S"                  | Current impurity/uncertainty **before** any split                                      | Starting entropy – we want to reduce this                   |
| **−** (minus)                  | "minus"                                                   | We subtract the average entropy **after** the split                                    | Gain is always ≥ 0 (entropy can only stay same or decrease) |
| **Σ**                          | "sum over all possible values v of A"                     | We do this calculation **for every branch** that attribute A creates                   | —                                                           |
| **v ∈ Values(A)**              | "for each possible value v in the values of attribute A"  | Every category/value that A can take (e.g., Sunny, Overcast, Rain)                     | Number of terms in sum = number of branches                 |
| **|Sᵥ|**                       | "size of subset S sub v" or "number of examples where A = v" | How many records go into this branch                            | —                                                           |
| **|S|**                         | "size of the whole dataset S"                             | Total number of examples before splitting                                              | Used to calculate weight/proportion                        |
| **|Sᵥ| / |S|**                 | "fraction of examples that go to value v"                 | Weight – how important this branch is (proportion of data)                             | Branches with more examples matter more                     |
| **H(Sᵥ)**                      | "entropy of the subset S sub v"                           | Impurity/uncertainty **after** splitting for this particular value v                   | Goal: make each H(Sᵥ) as small as possible                  |
| **(|Sᵥ|/|S|) × H(Sᵥ)**        | "weighted entropy of branch v"                            | Contribution of this branch to the remaining uncertainty                               | We take weighted average of all branch entropies            |
| **whole sum**                  | "sum of weighted entropies after the split"               | Average remaining entropy if we split on A                                             | Lower = better split                                        |

**Natural sentence version (how to say the formula):**  
"Information Gain = original entropy minus the weighted average of the entropies in all the child nodes after splitting on A."

## 3 Classroom-style Examples (Very Common in Exams)

### Example 1: Perfect Split (High Information Gain)

**Before split** (6 examples): 4 Buy_Computer=Yes, 2 No  
→ H(S) = –[(4/6)log₂(4/6) + (2/6)log₂(2/6)] ≈ **0.918 bits**

**Split on attribute "Student"**

- Student = Yes → 3 examples: all Yes → H = **0**  
- Student = No  → 3 examples: 1 Yes, 2 No → H ≈ **0.918**

**Weighted entropy after split**  
= (3/6)×0 + (3/6)×0.918 = **0.459**

**Gain** = 0.918 − 0.459 = **0.459 bits**  
→ Very good split! (almost halves the uncertainty)

### Example 2: Useless Split (Zero Information Gain)

**Split on attribute "ID number"** (assume each example has unique ID 1 to 6)

- Each value of ID → only 1 example → every child node is pure → H(Sᵥ) = **0** for all branches  
- Weighted entropy after split = (1/6)×0 + (1/6)×0 + … = **0**

**Gain** = 0.918 − 0 = **0.918 bits** ? Wait — **No!**

Wait — actually in real ID3:  
Splitting on unique ID creates 6 leaves, each with 1 example → yes H=0 everywhere  
But **Gain would be 0.918** — but ID3 **avoids** such attributes because:

- It creates too many branches  
- In practice we penalize attributes with many values (or use Gain Ratio instead)

But pure calculation → Gain = H(S) when split makes all leaves pure  
→ **Maximum possible gain** = H(S) (perfect separation)

### Example 3: Typical Moderate Split (Most Realistic)

**Split on "Age"** (values: Youth, Middle, Old)

Assume after split:

- Youth   (3 examples): 1 Yes, 2 No → H ≈ **0.918**  
- Middle  (1 example): 1 Yes → H = **0**  
- Old     (2 examples): 2 Yes → H = **0**

**Weighted entropy after split**  
= (3/6)×0.918 + (1/6)×0 + (2/6)×0 = **0.459**

**Gain** = 0.918 − 0.459 = **0.459 bits**

→ Same as "Student" in this toy case — good split

## Quick Summary Table (Exam Favorite)

| Split Quality      | Gain Value       | What it means                              | Decision Tree Action                     |
|--------------------|------------------|--------------------------------------------|------------------------------------------|
| Perfect split      | = H(S)           | All child nodes become pure                | Excellent choice – often chosen          |
| Very good split    | ≈ 0.4 – 0.8      | Big reduction in uncertainty               | Usually selected                         |
| Moderate/useful    | 0.1 – 0.4        | Some improvement                           | May be chosen if no better exists        |
| Useless split      | ≈ 0              | Entropy barely changes                     | Almost never chosen                      |

**Key sentence to remember:**  
"ID3 selects the attribute with the **highest Information Gain** at each step — because it reduces uncertainty the most."

Happy studying, Anirudha!  
You can copy this .md directly into your notes.
