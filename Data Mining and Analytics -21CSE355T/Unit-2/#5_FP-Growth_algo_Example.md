# FP-Growth Algorithm – Step-by-Step with Example
Let’s understand with an example how the FP Growth algorithm in data mining can be used to mine frequent itemsets. Suppose we have a dataset of transactions as shown below:

**Dataset (5 transactions):**

| TID | Items                        |
|-----|------------------------------|
| T1  | M, N, O, E, K, Y             |
| T2  | D, O, E, N, Y, K             |
| T3  | K, A, M, E                   |
| T4  | M, C, U, Y, K                |
| T5  | C, O, K, O, E, I             |

**Minimum support threshold**: 3 (min_sup = 3)

## Step 1: First Database Scan – Count item frequencies

Count how many times each item appears across all transactions.

| Item | Frequency | Frequent? (≥ 3) |
|------|-----------|------------------|
| K    | 5         | Yes              |
| E    | 4         | Yes              |
| M    | 3         | Yes              |
| O    | 3         | Yes              |
| Y    | 3         | Yes              |
| N    | 2         | No               |
| C    | 2         | No               |
| A    | 1         | No               |
| D    | 1         | No               |
| I    | 1         | No               |
| U    | 1         | No               |

**Frequent 1-itemsets**: {K:5}, {E:4}, {M:3}, {O:3}, {Y:3}

## Step 2: Sort frequent items by descending frequency

Order: **K > E > M > O > Y**

Rewrite each transaction using **only frequent items** and in the sorted order:

| TID | Original               | Filtered & Sorted       |
|-----|------------------------|--------------------------|
| T1  | M N O E K Y            | **K E M O Y**            |
| T2  | D O E N Y K            | **K E O Y**              |
| T3  | K A M E                | **K E M**                |
| T4  | M C U Y K              | **K M Y**                |
| T5  | C O K O E I            | **K E O**                |

## Step 3: Second Database Scan – Build FP-Tree

Create the FP-tree by inserting the sorted transactions one by one.

**Resulting FP-Tree** (text representation):

```
Root (5)
└── K (5)
    ├── E (4)
    │   ├── M (2)
    │   │   └── O (1)
    │   │       └── Y (1)
    │   └── O (2)
    │       └── Y (1)
    └── M (1)
        └── Y (1)
```

**Header table** (with node-links):

- K → K(5)
- E → E(4)
- M → M(2) ↔ M(1)
- O → O(1) ↔ O(2)
- Y → Y(1) ↔ Y(1) ↔ Y(1)

## Step 4: Mine Frequent Itemsets (Conditional Pattern Base Mining)

Start from the bottom of the header table (Y → O → M → E → K) and recursively mine.

### 4.1 Mining for Y (support = 3)

Conditional pattern bases for Y:

- K E M O : Y (1)
- K E O   : Y (1)
- K M     : Y (1)

→ Conditional FP-tree yields: **{K,Y}** (3)

### 4.2 Mining for O (support = 3)

Conditional pattern bases:

- K E M O (1)
- K E O   (1)

→ Frequencies: K:2, E:2 → no new itemsets ≥ 3

### 4.3 Mining for M (support = 3)

Conditional pattern bases:

- K E M (2)
- K M    (1)

→ Frequencies: K:3, E:2 → **{K,M}** (3)

### 4.4 Mining for E (support = 4)

Conditional pattern bases:

- K E M O Y (1)
- K E O Y   (1)
- K E M     (1)
- K E O     (1)

→ Frequencies: K:4 → **{K,E}** (4)

### 4.5 Mining for K (support = 5)

No conditional pattern base needed → already frequent alone

## Final Frequent Itemsets (min_sup = 3)

**1-itemsets**  
K(5), E(4), M(3), O(3), Y(3)

**2-itemsets**  
{K,E}(4), {K,M}(3), {K,Y}(3)

**3+-itemsets**  
None in this example

**Summary**: FP-Growth found all frequent patterns by building a compact tree and mining conditional patterns — without generating candidates and with only **two database scans**.


