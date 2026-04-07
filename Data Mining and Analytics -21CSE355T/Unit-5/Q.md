# **Unit-5: Outliers and Statistical Approaches in Data Mining**

**Approximate Weightage Distribution:**
* **Outlier Concepts & Challenges:** ~20% (Definitions, types, and the noise vs. outlier debate).
* **Detection Methods:** ~25% (Supervised, Unsupervised, and Semi-supervised frameworks).
* **Statistical Approaches:** ~20% (Z-Score, IQR, and Parametric vs. Non-parametric models).
* **Applications:** ~35% (Recommender Systems, IDS, and Financial Fraud—high-value for 10/16 mark questions).

---

## **Section A: Basic Concepts & Challenges**
1. **Define an Outlier.** Why is it often called "Anomaly Mining" rather than "Noise Mining"?
2. **Describe the three categories of Outliers with real-world examples:**
    * **Global Outliers** (Point Anomalies).
    * **Contextual Outliers** (Conditional Outliers).
    * **Collective Outliers**.
3. **What are the major challenges in Outlier Detection?** Explain why "Normal" behavior is hard to model.
4. **Differentiate between Noise and Outliers.** Why must a data miner be careful not to delete outliers?
5. **Discuss the "Understandability" challenge.** Why is providing a justification for an outlier important?

---

## **Section B: Outlier Detection Methods**
6. **Explain the Supervised approach to outlier detection.** What are its limitations regarding rare classes?
7. **Discuss Unsupervised Outlier Detection.** How does it find anomalies without any prior labels?
8. **What is Semi-supervised Outlier Detection?** Explain the "Normal-only" training strategy.
9. **Compare and contrast Distance-based vs. Density-based outlier detection.**
10. **Explain how Clustering-based methods identify outliers.** (e.g., points that do not belong to any cluster).

---

## **Section C: Statistical Data Mining Approaches**
11. **Explain the General Statistical Approach.** How is the "Probability Distribution" used to flag anomalies?
12. **Differentiate between Parametric and Non-parametric methods.** Provide examples for each.
13. **What is the Z-Score method?** Provide the mathematical formula and explain the significance of the "3-sigma" rule.
14. **Describe the IQR (Interquartile Range) method.** Explain the use of the "Boxplot" for identifying global outliers.
15. **What is Grubb’s Test?** Explain how it identifies a single outlier in a normal distribution.
16. **Explain Univariate vs. Multivariate outliers.** Give an example of a multivariate outlier that appears normal in univariate analysis.



---

## **Section D: Recommender Systems**
17. **Define Recommender Systems.** Explain their importance in modern e-commerce.
18. **Discuss Content-Based Filtering.** How does it use item attributes to make suggestions?
19. **Explain Collaborative Filtering.** Differentiate between:
    * **User-based** similarity.
    * **Item-based** similarity.
20. **Describe Similarity Measures:**
    * **Pearson Correlation Coefficient** formula and its role.
    * **Cosine Similarity** formula and its role.
21. **What is a "Shilling Attack"?** How can collective outlier detection prevent fake rating manipulation?



---

## **Section E: Intrusion Detection & Financial Analysis**
22. **What is an Intrusion Detection System (IDS)?** Differentiate between:
    * **Signature-based** detection.
    * **Anomaly-based** detection.
23. **Discuss the role of Data Mining in IDS.** Mention tasks like Classification and Outlier Detection.
24. **Explain Data Mining for Financial Analysis.** How is it used for:
    * **Credit Card Fraud Detection**?
    * **Money Laundering Detection**?
25. **What are the key challenges in Financial Data Mining?** (e.g., high-speed transactions, privacy, and evolving fraud patterns).

---

# **MCQs on Outliers and Statistical Approaches (Unit 5)**

1. A temperature of 35°C in December in a cold region is an example of:
   A. Global Outlier  **B. Contextual Outlier** C. Collective Outlier D. Noise

2. Which statistical method does NOT assume a Normal Distribution?
   A. Z-Score B. Grubb's Test **C. IQR** D. Linear Regression

3. In a Box Plot, a point is an outlier if it falls outside:
   A. $[Q1, Q3]$ **B. $Q3 + 1.5(IQR)$** C. Mean $\pm 1$ SD D. The Median

4. Which recommendation method focuses on the similarity between items?
   A. Collaborative Filtering **B. Item-Based Filtering** C. User-Based Filtering D. Association Rules

5. "Classifying transactions as Fraud or Normal using a labeled dataset" is:
   **A. Supervised Detection** B. Unsupervised Detection C. Semi-supervised D. Clustering

6. Pearson Correlation measures:
   **A. Linear relationship between users** B. Density of clusters C. Frequency of items D. Noise level

7. Which outlier type involves a sequence of events that is abnormal as a whole?
   A. Point Outlier B. Contextual Outlier **C. Collective Outlier** D. Global Outlier

8. The primary challenge in Anomaly-based IDS is:
   **A. High False Positive rate** B. Inability to detect new attacks C. Slow processing D. Database size

9. "Mean-centering" ratings in item-based filtering is done to:
   **A. Remove user rating bias** B. Increase computation speed C. Handle zero-values D. Predict price

10. A Z-Score of 0 indicates the value is:
    A. An outlier **B. Exactly the mean** C. Far from the mean D. Negative

---

# **Important Long-Answer Questions**

1. **Statistical Outlier Detection (16 marks):** Compare Z-Score and IQR. Show with a numerical example how the Upper and Lower bounds are calculated in IQR.
2. **Recommender Systems Architecture (16 marks):** Explain Collaborative Filtering. Compare User-based and Item-based approaches with a User-Item Matrix example.
3. **Intrusion Detection (10 marks):** Discuss Anomaly-based IDS. Why is Outlier Mining the best tool for identifying "Zero-day" attacks?
4. **Outlier Categories (10 marks):** Define Global, Contextual, and Collective outliers. Provide one distinct real-world application for each.
5. **Data Mining for Finance (16 marks):** Discuss the role of Data Mining in Fraud Detection and Financial Analysis. Explain the importance of statistical modeling in banking.