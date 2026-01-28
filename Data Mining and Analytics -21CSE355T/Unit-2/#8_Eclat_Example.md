# ECLAT Algorithm – Step-by-Step Example

**ECLAT** (Equivalence Class Clustering and bottom-up Lattice Traversal) is a fast algorithm for mining frequent itemsets. It uses a **vertical data format** (tidsets = lists of transaction IDs where each item appears) and computes support via fast **set intersections** — no repeated database scans after the initial step.

**Dataset** (Boolean matrix representation):

| TID | Bread | Butter | Milk | Coke | Jam |
|-----|-------|--------|------|------|-----|
| T1  | 1     | 1      | 0    | 0    | 1   |
| T2  | 0     | 1      | 0    | 1    | 0   |
| T3  | 0     | 1      | 1    | 0    | 0   |
| T4  | 1     | 1      | 0    | 1    | 0   |
| T5  | 1     | 0      | 1    | 0    | 0   |
| T6  | 0     | 1      | 1    | 0    | 0   |
| T7  | 1     | 0      | 1    | 0    | 0   |
| T8  | 1     | 1      | 1    | 0    | 1   |
| T9  | 1     | 1      | 1    | 0    | 0   |

**Minimum support (min_sup)** = 2 (an itemset must appear in at least 2 transactions)

## Step 1: Create Tidsets for Single Items (1-itemsets)

Scan the dataset once and build a vertical representation — for each item, list the transaction IDs (TIDs) where it appears (1 = present).

| Item   | Tidset                  | Support (size of tidset) | Frequent? (≥ 2) |
|--------|-------------------------|---------------------------|-----------------|
| Bread  | {T1, T4, T5, T7, T8, T9} | 6                         | Yes             |
| Butter | {T1, T2, T3, T4, T6, T8, T9} | 7                     | Yes             |
| Milk   | {T3, T5, T6, T7, T8, T9} | 6                         | Yes             |
| Coke   | {T2, T4}                | 2                         | Yes             |
| Jam    | {T1, T8}                | 2                         | Yes             |

**Frequent 1-itemsets**: All items above (since min_sup = 2)

## Step 2: Generate 2-itemsets by Intersecting Tidsets

Combine pairs of frequent 1-itemsets and compute support by taking the **intersection** of their tidsets. Only keep those with support ≥ 2.

| Itemset            | Tidset Intersection              | Support | Frequent? |
|--------------------|----------------------------------|---------|-----------|
| {Bread, Butter}    | {T1,T4,T5,T7,T8,T9} ∩ {T1,T2,T3,T4,T6,T8,T9} = {T1, T4, T8, T9} | 4       | Yes       |
| {Bread, Milk}      | {T1,T4,T5,T7,T8,T9} ∩ {T3,T5,T6,T7,T8,T9} = {T5, T7, T8, T9}   | 4       | Yes       |
| {Bread, Coke}      | {T1,T4,T5,T7,T8,T9} ∩ {T2,T4} = {T4}                            | 1       | No        |
| {Bread, Jam}       | {T1,T4,T5,T7,T8,T9} ∩ {T1,T8} = {T1, T8}                        | 2       | Yes       |
| {Butter, Milk}     | {T1,T2,T3,T4,T6,T8,T9} ∩ {T3,T5,T6,T7,T8,T9} = {T3, T6, T8, T9} | 4       | Yes       |
| {Butter, Coke}     | {T1,T2,T3,T4,T6,T8,T9} ∩ {T2,T4} = {T2, T4}                     | 2       | Yes       |
| {Butter, Jam}      | {T1,T2,T3,T4,T6,T8,T9} ∩ {T1,T8} = {T1, T8}                     | 2       | Yes       |
| {Milk, Coke}       | {T3,T5,T6,T7,T8,T9} ∩ {T2,T4} = {}                              | 0       | No        |
| {Milk, Jam}        | {T3,T5,T6,T7,T8,T9} ∩ {T1,T8} = {T8}                            | 1       | No        |
| {Coke, Jam}        | {T2,T4} ∩ {T1,T8} = {}                                          | 0       | No        |

**Frequent 2-itemsets**: {Bread,Butter}(4), {Bread,Milk}(4), {Bread,Jam}(2), {Butter,Milk}(4), {Butter,Coke}(2), {Butter,Jam}(2)

## Step 3: Generate Larger Itemsets Recursively (k = 3, k = 4, …)

Continue combining compatible frequent itemsets (prefix-sharing) and intersect their tidsets.

**For k = 3** (examples of combinations):

| Itemset                  | Tidset Intersection                                      | Support | Frequent? |
|--------------------------|----------------------------------------------------------|---------|-----------|
| {Bread, Butter, Milk}    | {T1,T4,T8,T9} ∩ {T5,T7,T8,T9} = {T8, T9}                | 2       | Yes       |
| {Bread, Butter, Jam}     | {T1,T4,T8,T9} ∩ {T1,T8} = {T1, T8}                      | 2       | Yes       |
| {Bread, Butter, Coke}    | {T1,T4,T8,T9} ∩ {T2,T4} = {T4}                          | 1       | No        |
| {Butter, Milk, Jam}      | {T3,T6,T8,T9} ∩ {T1,T8} = {T8}                          | 1       | No        |
| {Bread, Milk, Jam}       | {T5,T7,T8,T9} ∩ {T1,T8} = {T8}                          | 1       | No        |

**Frequent 3-itemsets**: {Bread,Butter,Milk}(2), {Bread,Butter,Jam}(2)

**For k = 4**:

| Itemset                        | Tidset Intersection                  | Support | Frequent? |
|--------------------------------|--------------------------------------|---------|-----------|
| {Bread, Butter, Milk, Jam}     | {T8,T9} ∩ {T1,T8} = {T8}            | 1       | No        |

No frequent 4-itemsets (support < 2).

## Step 4: Stop Condition

The recursion stops when:
- No more combinations can be made, or
- No new itemset has support ≥ min_sup

Here we stop at k = 4.

## Final Frequent Itemsets (min_sup = 2)

- **1-itemsets**: Bread(6), Butter(7), Milk(6), Coke(2), Jam(2)
- **2-itemsets**: {Bread,Butter}(4), {Bread,Milk}(4), {Bread,Jam}(2), {Butter,Milk}(4), {Butter,Coke}(2), {Butter,Jam}(2)
- **3-itemsets**: {Bread,Butter,Milk}(2), {Bread,Butter,Jam}(2)
- **4+-itemsets**: None

## Summary – Why ECLAT is Efficient

- Only **one database scan** to build tidsets.
- Support calculation = fast **set intersection** (no full scan).
- No candidate generation explosion like Apriori.
- Best for sparse datasets or when tidsets fit in memory.

You can now use these frequent itemsets to generate association rules (e.g., Bread → Butter, confidence = 4/6 ≈ 67%).