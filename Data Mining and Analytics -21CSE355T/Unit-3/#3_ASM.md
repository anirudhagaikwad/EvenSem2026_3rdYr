# Attribute Selection Measures (ASM)

### **The Mathematical Philosophy**
In data mining, we are constantly fighting **Entropy** (disorder). When we build a decision tree, we are trying to organize a messy pile of data into "pure" categories. **Attribute Selection Measures** are the mathematical tools that tell us which "surgical cut" (split) will remove the most messiness from our data.

> **Core Idea:** Every split in a decision tree is a question. ASMs help us find the *best question to ask* at each node — the one that separates classes most cleanly.

---

## **1. Information Gain: The Logic of Reduction**
Information Gain is the primary measure used in the ID3 algorithm. It is based on the idea that the "information" in a message is proportional to how much it surprises us.


### **The Calculation Flow:**
1. **Total Entropy ($Info(D)$):** First, we measure the "chaos" of the target class (e.g., how many people said 'Yes' vs 'No' to a loan).
   $$Info(D) = -\sum_{i=1}^{m} p_i \log_2(p_i)$$

2. **Feature Entropy ($Info_A(D)$):** We then calculate what the chaos *would be* if we split the data using Attribute A. We take the weighted average of the entropy of each resulting group.
   $$Info_A(D) = \sum_{j=1}^{v} \frac{|D_j|}{|D|} \times Info(D_j)$$

3. **The Gain:** The difference between the original entropy and the new entropy is our "Gain."
   $$Gain(A) = Info(D) - Info_A(D)$$


### **Worked Example — Information Gain**

**Dataset:** 14 days of Tennis data. Target: Play? (Yes=9, No=5)

$$Info(D) = -\frac{9}{14}\log_2\frac{9}{14} - \frac{5}{14}\log_2\frac{5}{14} \approx 0.940$$

**Attribute: Outlook** (Sunny=5, Overcast=4, Rain=5)

| Branch | Yes | No | Entropy |
|:---|:---|:---|:---|
| Sunny | 2 | 3 | 0.971 |
| Overcast | 4 | 0 | 0.000 |
| Rain | 3 | 2 | 0.971 |

$$Info_{Outlook}(D) = \frac{5}{14}(0.971) + \frac{4}{14}(0) + \frac{5}{14}(0.971) \approx 0.694$$

$$Gain(Outlook) = 0.940 - 0.694 = \mathbf{0.246}$$

### **Properties of Information Gain**
* Always **non-negative** — splitting can never increase entropy on average.
* Equals **zero** when the attribute provides no useful separation.
* Equals $Info(D)$ (maximum) when every branch is perfectly pure.
* **Additive:** gains from independent splits can be summed.

---

## **2. Gain Ratio: The "Fairness" Correction**
A major problem with Information Gain is that it is **Biased**.
* **The "ID" Problem:** If an attribute has a unique value for every record (like `Roll_Number` or `Email`), Information Gain will think it's a perfect split (Entropy = 0) even though that attribute has no predictive power for new data.
* **The Solution:** Gain Ratio penalizes these "unfair" attributes by incorporating **Split Information**.

**Split Information Formula:** This measures how "spread out" the data becomes after a split. If a split produces many small, uniform groups, this value becomes very high.
$$SplitInfo_A(D) = -\sum_{j=1}^{v} \frac{|D_j|}{|D|} \log_2 \left( \frac{|D_j|}{|D|} \right)$$

**The Correction:**
$$GainRatio(A) = \frac{Gain(A)}{SplitInfo_A(D)}$$

### **Worked Example — Gain Ratio**

Continuing from the Tennis example above for **Outlook**:

$$SplitInfo_{Outlook}(D) = -\frac{5}{14}\log_2\frac{5}{14} - \frac{4}{14}\log_2\frac{4}{14} - \frac{5}{14}\log_2\frac{5}{14} \approx 1.577$$

$$GainRatio(Outlook) = \frac{0.246}{1.577} \approx \mathbf{0.156}$$

Now compare to a hypothetical **ID attribute** (14 unique values, one per record):
* $Gain(ID) \approx 0.940$ ← looks amazing to ID3!
* $SplitInfo(ID) = \log_2(14) \approx 3.807$ ← huge penalty
* $GainRatio(ID) = \frac{0.940}{3.807} \approx 0.247$ ← brought back down to earth

### **Important Nuance in C4.5**
C4.5 does **not** simply pick the attribute with the highest Gain Ratio outright. It:
1. Computes the **average Information Gain** across all attributes.
2. Only considers attributes with **above-average gain**.
3. Among those, picks the one with the **highest Gain Ratio**.

This prevents Gain Ratio from unfairly penalizing attributes that split into just two branches (low SplitInfo → artificially high ratio).

---

## **3. Gini Index: The Computational Powerhouse**
The Gini Index is the default for modern data science (used in CART) because it is **Computationally Efficient**. It avoids complex logarithms ($\log_2$), which makes it significantly faster to calculate on massive datasets.

### **Geometric Interpretation:**
The Gini Index represents the probability that a randomly chosen element from the set would be incorrectly classified if it was randomly labeled according to the distribution of labels in the subset.
$$Gini(D) = 1 - \sum_{i=1}^{m} p_i^2$$


* **Maximum Impurity:** $0.5$ (For a 2-class problem where classes are equally mixed).
* **Minimum Impurity:** $0$ (When the node is perfectly pure).

### **Gini for a Binary Split**
For CART, which always splits into exactly two groups ($D_1$ and $D_2$):
$$Gini_A(D) = \frac{|D_1|}{|D|} Gini(D_1) + \frac{|D_2|}{|D|} Gini(D_2)$$

The **Gini Gain** (reduction in impurity) for a split is:
$$\Delta Gini(A) = Gini(D) - Gini_A(D)$$

**The attribute with the lowest $Gini_A(D)$ (highest $\Delta Gini$) is selected.**

### **Worked Example — Gini Index**

Using the Tennis dataset. Target: Play? (Yes=9, No=5, $n=14$)

$$Gini(D) = 1 - \left[\left(\frac{9}{14}\right)^2 + \left(\frac{5}{14}\right)^2\right] = 1 - [0.413 + 0.128] \approx 0.459$$

**Attribute: Humidity** (High=7, Normal=7)
* High: Yes=3, No=4 → $Gini = 1 - [(3/7)^2 + (4/7)^2] \approx 0.490$
* Normal: Yes=6, No=1 → $Gini = 1 - [(6/7)^2 + (1/7)^2] \approx 0.245$

$$Gini_{Humidity}(D) = \frac{7}{14}(0.490) + \frac{7}{14}(0.245) \approx \mathbf{0.368}$$

$$\Delta Gini(Humidity) = 0.459 - 0.368 = \mathbf{0.091}$$

---

## **4. Side-by-Side Numerical Comparison**

Using the Tennis dataset for attribute **Outlook**:

| Measure | Formula | Value |
|:---|:---|:---|
| Information Gain | $Gain(Outlook)$ | 0.246 |
| Split Information | $SplitInfo(Outlook)$ | 1.577 |
| Gain Ratio | $GainRatio(Outlook)$ | 0.156 |
| Gini (parent) | $Gini(D)$ | 0.459 |
| Gini (after split) | $Gini_{Outlook}(D)$ | 0.343 |
| Gini Gain | $\Delta Gini(Outlook)$ | 0.116 |

All three measures agree: **Outlook** is the best first split in the Tennis dataset.

---

## **5. Detailed Comparison for Theory Exams**

| Feature | Information Gain | Gain Ratio | Gini Index |
| :--- | :--- | :--- | :--- |
| **Origin** | Information Theory | Information Theory | Economics/Statistics |
| **Algorithm** | ID3 | C4.5, C5.0 | CART |
| **Complexity** | High (Logarithmic) | Very High (Logarithmic) | Low (Algebraic) |
| **Split Style** | Multi-way | Multi-way | Strictly Binary |
| **Bias** | Prefers many-valued attributes | Prefers unbalanced splits | Favors larger partitions |
| **Handles Missing Values** | ❌ No | ✅ Yes | ✅ Yes (surrogates) |
| **Handles Continuous Attrs** | ❌ No | ✅ Yes | ✅ Yes |
| **Range** | $[0, \log_2 c]$ | $[0, 1]$ | $[0, 0.5]$ for binary |
| **Speed** | Moderate | Moderate | Fast |

---

## **6. Entropy vs. Gini: When Do They Differ?**

In practice, both measures almost always select the **same attribute**. They differ mainly at edge cases:

| Scenario | Entropy Behaviour | Gini Behaviour |
|:---|:---|:---|
| Near-pure node (95%/5%) | Very sensitive — still penalizes | Less sensitive — nearly 0 |
| Equal classes (50%/50%) | Max = 1.0 | Max = 0.5 |
| Multiple classes | Scales with $\log_2 c$ | Always $\leq (c-1)/c$ |
| Outlier class (1 sample) | Penalizes slightly | Almost ignores it |

> **Rule of Thumb:** Use Entropy when interpretability and information-theoretic grounding matter. Use Gini when speed on large datasets is a priority.

---

## **7. Summary Checklist for Selection**
Selection of the correct measure depends on the dataset characteristics:
* **Information Gain:** Best if you have categorical data with a small, balanced number of values per attribute.
* **Gain Ratio:** Essential if your data contains attributes with many unique values (like Zip Codes or Dates) to avoid misleadingly high gain.
* **Gini Index:** Best for high-performance systems and large-scale big data where binary trees (strictly two branches) are preferred.


---

## **8. Advanced Considerations: Attribute Selection Limits**
In practice, selecting an attribute is only half the battle. We must also consider:
* **Minimum Leaf Size:** If a split results in a group with only 1 or 2 members, it might be statistically insignificant.
* **Max Depth:** Deep trees tend to use attributes that provide very tiny gains, leading to overfitting.
* **Continuous Attributes:** For numeric data (like 'Temperature'), the algorithm must find a "split point" (e.g., Temperature > 30°C) by testing multiple thresholds and calculating the ASM for each.

### **Finding the Best Split Point for Continuous Attributes**

For a numeric attribute with values $\{v_1, v_2, ..., v_n\}$ (sorted):
1. Compute candidate thresholds: midpoints between consecutive values $\rightarrow \frac{v_i + v_{i+1}}{2}$
2. Evaluate the ASM (Gain / Gini) for each threshold as a binary split.
3. Select the threshold that maximizes gain / minimizes Gini.

**Example:** Temperature = {64, 65, 68, 69, 70, 71, 72, 75, 80, 83, 85}
* Candidates: 64.5, 66.5, 68.5, 69.5, 70.5, 71.5, 73.5, 77.5, 81.5, 84.0
* Each is evaluated and the best threshold (e.g., Temperature ≤ 71.5) is selected.

This makes continuous attribute handling $O(n \log n)$ per attribute (due to sorting).

---

## **9. Chi-Square Test: A Statistical Alternative**

The **CHAID (Chi-squared Automatic Interaction Detector)** algorithm uses the **Chi-Square statistic** instead of entropy or Gini to select attributes.

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

Where $O$ = observed frequency and $E$ = expected frequency under independence.

* **High $\chi^2$** → the attribute and target class are strongly dependent → good split.
* **Low $\chi^2$** → independence → poor split.

| Measure | Statistical Basis | Handles Multi-class | Produces |
|:---|:---|:---|:---|
| Information Gain | Shannon Entropy | ✅ Yes | Multi-way tree |
| Gain Ratio | Normalized Entropy | ✅ Yes | Multi-way tree |
| Gini Index | Probability theory | ✅ Yes | Binary tree |
| Chi-Square | Hypothesis testing | ✅ Yes | Multi-way tree |

---

## **10. Quick Formula Reference Card**

| Measure | Formula | Select When |
|:---|:---|:---|
| **Entropy** | $-\sum p_i \log_2 p_i$ | Base measure for all IG calculations |
| **Information Gain** | $Info(D) - Info_A(D)$ | Highest value wins |
| **Split Info** | $-\sum \frac{\|D_j\|}{\|D\|} \log_2 \frac{\|D_j\|}{\|D\|}$ | Used to normalize Gain |
| **Gain Ratio** | $\frac{Gain(A)}{SplitInfo_A(D)}$ | Highest value wins |
| **Gini (node)** | $1 - \sum p_i^2$ | Lowest after split wins |
| **Gini (split)** | $\frac{\|D_1\|}{\|D\|}Gini(D_1) + \frac{\|D_2\|}{\|D\|}Gini(D_2)$ | Lowest value wins |