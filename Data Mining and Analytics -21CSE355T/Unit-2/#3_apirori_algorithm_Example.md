**Detailed Step-by-Step Example of Apriori Algorithm for Market Basket Analysis**

# **Example 1**
Let's use a classic grocery store dataset with **10 transactions** (T1 to T10) to make it realistic.

**Items**:
- Beetroot (B)
- Bread (Br)
- Diapers (D)
- Eggs (E)
- Milk (M)

**Min Support** = 0.3 (appears in at least 3 out of 10 transactions = 30%)  
**Min Confidence** = 0.6 (60%)

**Transaction Dataset**

| TID | Items                  |
|-----|------------------------|
| T1  | {B, D, M}              |
| T2  | {Br, D}                |
| T3  | {B, Br, D, M}          |
| T4  | {Br, E}                |
| T5  | {B, D, M}              |
| T6  | {Br, D}                |
| T7  | {B, Br, D, E, M}       |
| T8  | {B, M}                 |
| T9  | {Br, D, M}             |
| T10 | {B, Br, D}             |

**Total transactions (N)** = 10

## Step 1 ➜ : Frequent 1-Itemsets (L1)

Scan all transactions and count frequency for each item.

| Item | Support (Frequency) | Support (%) |
|------|----------------------|-------------|
| B    | 6                    | 60%         |
| Br   | 7                    | 70%         |
| D    | 7                    | 70%         |
| E    | 2                    | 20%         |
| M    | 6                    | 60%         |

**Frequent 1-itemsets (L1)**: {B}, {Br}, {D}, {M} (all ≥ 0.3)  
**Pruned**: {E} (0.2 < 0.3)

**How support is calculated**  
Support({X}) = (number of transactions containing X) / Total transactions  
Example: Support(B) = 6 / 10 = 0.6 (60%)

## Step 2 ➜ : Candidate & Frequent 2-Itemsets (C2 → L2)

Generate all possible pairs from L1 (sorted alphabetically), then count support.

| Candidate Item Set | Support (Frequency) | Support (%) |
|--------------------|----------------------|-------------|
| {B, Br}            | 3                    | 30%         |
| {B, D}             | 5                    | 50%         |
| {B, M}             | 5                    | 50%         |
| {Br, D}            | 6                    | 60%         |
| {Br, M}            | 3                    | 30%         |
| {D, M}             | 4                    | 40%         |

**All candidates ≥ 0.3**, so **Frequent 2-itemsets (L2)** = all of the above.

**How support for 2-itemsets is calculated**  
Support({X, Y}) = (number of transactions containing both X and Y) / Total transactions  
Example: Support({B, D}) = 5 / 10 = 0.5 (50%)

## Step 3 ➜ : Candidate & Frequent 3-Itemsets (C3 → L3)

Generate candidates by joining frequent 2-itemsets (must share first k-1 = 1 item), prune using Apriori property, then count support.

| Candidate Item Set | Support (Frequency) | Support (%) | Frequent? (≥ 0.3) |
|--------------------|----------------------|-------------|-------------------|
| {B, Br, D}         | 3                    | 30%         | Yes               |
| {B, Br, M}         | 1                    | 10%         | No                |
| {B, D, M}          | 3                    | 30%         | Yes               |
| {Br, D, M}         | 2                    | 20%         | No                |

**Frequent 3-itemsets (L3)**: {B, Br, D}, {B, D, M}

**How support for 3-itemsets is calculated**  
Support({X, Y, Z}) = (number of transactions containing all three items) / Total transactions  
Example: Support({B, D, M}) = 3 / 10 = 0.3 (30%)

## Step 4 ➜ : Candidate 4-Itemsets

Join L3 items: {B, Br, D} and {B, D, M}  
→ Possible join would require sharing first 2 items (sorted): {B, Br} vs {B, D} → different → **no join possible**.  
**No 4-itemset candidates**. Algorithm stops here.

## Step 5 ➜ : Strong Association Rules

Generate rules from frequent itemsets (mainly L2 and L3) with **confidence ≥ 60%**.

| Antecedent (If)     | Consequent (Then) | Confidence (%) | Support of Rule (%) | Notes                          |
|---------------------|-------------------|----------------|---------------------|--------------------------------|
| {B}                 | {D}               | 83.3%          | 50%                 | From {B, D}                    |
| {D}                 | {B}               | 71.4%          | 50%                 | From {B, D}                    |
| {B, Br}             | {D}               | 100%           | 30%                 | Very strong rule               |
| {B, D}              | {Br}              | 60%            | 30%                 | Borderline strong              |
| {B, D}              | {M}               | 60%            | 30%                 | From {B, D, M}                 |
| {D, M}              | {B}               | 75%            | 30%                 | From {B, D, M}                 |

**How confidence is calculated**  
Confidence(X → Y) = Support(X ∪ Y) / Support(X) × 100%  

Examples:  
1. {B} → {D}  
   Conf = Support({B, D}) / Support({B}) = 0.5 / 0.6 ≈ **83.3%**

2. {B, Br} → {D}  
   Conf = Support({B, Br, D}) / Support({B, Br}) = 0.3 / 0.3 = **100%**

3. {D} → {B}  
   Conf = 0.5 / 0.7 ≈ **71.4%**

## Business Insights & Recommendations
Based on the strong rules:
- **Diapers (D) and Beetroot (B)** are very frequently bought together → Place them near each other or create "family shopping" bundles (B + D).
- When a customer buys **Beetroot + Bread**, they **always** buy **Diapers** (100% confidence) → Powerful cross-sell opportunity.
- **Milk (M)** is strongly associated with **Beetroot + Diapers** → Suggest Milk when someone adds B and D to cart.
- Avoid promoting **Eggs** aggressively — very low frequency and no strong associations.

This pattern is classic in retail analytics (famously linked to the "diapers + beer" urban legend — here diapers + beetroot/milk).

---

# Example 2

Let’s try to understand the Apriori algorithm implementation using an example.  
In this example, we will use a **minimum support threshold of 3**.  
This means an itemset must appear in **at least three transactions** to be considered frequent.

**Total transactions (N)** = 11

### Transaction Dataset

| TID  | Items                        |
|------|------------------------------|
| T1   | {milk, bread}                |
| T2   | {bread, sugar}               |
| T3   | {bread, butter}              |
| T4   | {milk, bread, sugar}         |
| T5   | {milk, bread, butter}        |
| T6   | {milk, bread, butter}        |
| T7   | {milk, sugar}                |
| T8   | {milk, sugar}                |
| T9   | {sugar, butter}              |
| T10  | {milk, sugar, butter}        |
| T11  | {milk, bread, butter}        |

## Step 1 ➜ Frequent 1-Itemsets (L1)
Let’s calculate support for each item present in the dataset.

| Item   | Support (Frequency) | Support (%) |
|--------|----------------------|-------------|
| milk   | 8                    | 72.7%       |
| bread  | 7                    | 63.6%       |
| sugar  | 5                    | 45.5%       |
| butter | 7                    | 63.6%       |

**Frequent 1-itemsets (L1)**: {milk}, {bread}, {sugar}, {butter} (all ≥ 3)

**How support is calculated**  
Support({X}) = (number of transactions containing X) / Total transactions  
(Here shown as absolute frequency; percentage = frequency / 11 × 100)

## Step 2 ➜ Candidate & Frequent 2-Itemsets (C2 → L2)
Generate all possible pairs from L1, then count support.

| Candidate Item Set     | Support (Frequency) | Support (%) |
|------------------------|----------------------|-------------|
| {milk, bread}          | 5                    | 45.5%       |
| {milk, sugar}          | 3                    | 27.3%       |
| {milk, butter}         | 5                    | 45.5%       |
| {bread, sugar}         | 2                    | 18.2%       |
| {bread, butter}        | 3                    | 27.3%       |
| {sugar, butter}        | 2                    | 18.2%       |

**Frequent 2-itemsets (L2)** (support ≥ 3):  
{milk, bread}, {milk, sugar}, {milk, butter}, {bread, butter}

**How support for 2-itemsets is calculated**  
Support({X, Y}) = number of transactions that contain **both** X and Y  
Count how many TIDs include the exact pair (regardless of other items).

## Step 3 ➜ Candidate & Frequent 3-Itemsets (C3 → L3)
Generate candidates from frequent 2-itemsets, then count support.

| Candidate Item Set          | Support (Frequency) | Support (%) |
|-----------------------------|----------------------|-------------|
| {milk, bread, sugar}        | 1                    | 9.1%        |
| {milk, bread, butter}       | 3                    | 27.3%       |
| {milk, sugar, butter}       | 1                    | 9.1%        |

**Frequent 3-itemsets (L3)** (support ≥ 3):  
{milk, bread, butter}

**How support for 3-itemsets is calculated**  
Support({X, Y, Z}) = number of transactions containing **all three** items X, Y, and Z simultaneously.

## Step 4 ➜ Candidate 4-Itemsets
Join frequent 3-itemsets:  
Only one frequent 3-itemset exists → **no join possible** → **no 4-itemset candidates**.

## Step 5 ➜ Strong Association Rules
Generate rules from frequent itemsets (mainly from L2 and L3) with reasonable confidence.

| Antecedent (If)       | Consequent (Then)     | Confidence (%) | Support of Rule (Frequency) |
|-----------------------|-----------------------|----------------|-----------------------------|
| {milk, bread}         | {butter}              | 60%            | 3                           |
| {bread, butter}       | {milk}                | 100%           | 3                           |
| {milk, butter}        | {bread}               | 60%            | 3                           |

**How confidence is calculated**  
Confidence(X → Y) = Support(X ∪ Y) / Support(X) × 100%

**Examples**:  
1. {milk, bread} → {butter}  
   Confidence = Support({milk, bread, butter}) / Support({milk, bread}) = 3 / 5 = **60%**

2. {bread, butter} → {milk}  
   Confidence = Support({milk, bread, butter}) / Support({bread, butter}) = 3 / 3 = **100%**

3. {milk, butter} → {bread}  
   Confidence = Support({milk, bread, butter}) / Support({milk, butter}) = 3 / 5 = **60%**

**Note**: The "Support of Rule" column shows the support of the complete itemset (antecedent + consequent).

## Business Insights & Recommendations
Based on the strong association rules above, retailers can:
- Place **butter** near **milk and bread** aisles (high co-occurrence)
- When a customer buys **bread and butter**, strongly recommend or bundle **milk** (100% confidence — very powerful cross-sell)
- Promote bundles like **milk + bread + butter** together
- Use these patterns for personalized recommendations, shelf optimization, and targeted promotions
