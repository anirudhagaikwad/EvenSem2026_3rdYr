# Unit-4: Cluster Analysis 

**Approximate Weightage Distribution:**
- **Partitioning Methods (K-Means/K-Medoids):** ~25% (Compulsory numerical or 10-mark descriptive).
- **Hierarchical Methods (Agglomerative/Divisive):** ~20% (Dendrogram and Linkage questions).
- **Density & Grid-Based (DBSCAN/STING/CLIQUE):** ~30% (Highest weightage for "Explain with diagram" questions).
- **Evaluation & Advanced Techniques (BIRCH/Evaluation):** ~25% (Metrics and scalability).

---

## **Section A: Introduction & Partitioning Methods**
1. **Define Cluster Analysis.** What are the requirements of a good clustering algorithm?
2. **Explain Partitioning Methods.** List the two main requirements for a valid partitioning.
3. **Describe the K-Means algorithm in detail.** Provide the step-by-step iterative process.
4. **What is K-Medoids?** Why is it considered more robust than K-Means?
5. **Differentiate between a Centroid and a Medoid.**
6. **What is the "Elbow Method"?** How is it used to determine the optimal value of $k$?



---

## **Section B: Hierarchical Methods**
7. **Explain Hierarchical Clustering.** Differentiate between Agglomerative and Divisive approaches.
8. **What is a Dendrogram?** Explain its role in visualizing hierarchical relationships.
9. **Describe the following linkage metrics with diagrams:**
    * Single Linkage (Nearest Neighbor)
    * Complete Linkage (Farthest Neighbor)
    * Average Linkage
10. **What are the limitations of hierarchical clustering?** Why is it considered "irreversible"?



---

## **Section C: Density, Grid, and Model-Based Methods**
11. **Explain the core concept of DBSCAN.** Define Core points, Border points, and Noise.
12. **Describe the two parameters of DBSCAN:** Epsilon ($\epsilon$) and MinPts.
13. **What is BIRCH?** Explain the Clustering Feature (CF) and the structure of a CF-Tree.
14. **Discuss the STING algorithm.** How does it use a hierarchical grid for statistical queries?
15. **What is CLIQUE?** Explain how it handles high-dimensional data using subspace clustering.
16. **Explain Probabilistic Model-Based Clustering.** How does it differ from "hard" clustering?



---

## **Section D: Evaluation of Clustering**
17. **Why is cluster evaluation necessary?** List the three main categories of evaluation.
18. **Explain Internal vs. External evaluation metrics.**
19. **Define the Silhouette Coefficient.** What does a score of +1, 0, or -1 indicate?
20. **What are Cohesion and Separation?** How are they used to measure cluster quality?

---

# **MCQs on Cluster Analysis (Unit 4)**

1. Which algorithm is most sensitive to outliers?
   **A. K-Means** B. K-Medoids  C. DBSCAN  D. BIRCH

2. A Dendrogram is used in which type of clustering?
   A. Partitioning  **B. Hierarchical** C. Density-based  D. Grid-based

3. Which parameter in DBSCAN defines the scanning radius?
   **A. Epsilon** B. MinPts  C. K  D. Threshold

4. Which algorithm is specifically designed for very large datasets (Big Data)?
   A. K-Means  B. PAM  **C. BIRCH** D. AGNES

5. In STING, what does 'n' represent in a grid cell?
   **A. Number of points** B. Mean  C. Standard Deviation  D. Distribution

6. Hard clustering means an object belongs to:
   **A. Exactly one cluster** B. Multiple clusters  C. Zero clusters  D. A probability distribution

7. The "Chaining Effect" is a common problem in:
   **A. Single Linkage** B. Complete Linkage  C. K-Means  D. CLIQUE

8. Which metric measures how similar an object is to its own cluster compared to others?
   A. SSE  **B. Silhouette Score** C. Entropy  D. Gini Index

9. CLIQUE is a hybrid of which two methods?
   **A. Grid and Density** B. Partitioning and Hierarchical  C. Model and Density  D. Grid and Model

10. Which algorithm uses the "Medoid" as a representative object?
    A. K-Means  **B. PAM** C. DBSCAN  D. STING

---

# **Mixed / Important Long-Answer Questions (10/16 Marks)**

1. **Partitioning vs. Hierarchical:** Compare K-Means and Agglomerative Hierarchical clustering in terms of complexity, data size, and cluster shape. (10 marks)
2. **DBSCAN Deep Dive:** Explain the concepts of density-reachability and density-connectivity with suitable diagrams. (16 marks)
3. **Big Data Clustering:** Discuss the BIRCH algorithm, explaining its four phases and why it is memory efficient. (16 marks)
4. **Grid-Based Methods:** Compare STING and CLIQUE. Why is CLIQUE preferred for high-dimensional data? (10 marks)
5. **Numerical Problem:** Given a set of 1D or 2D points and initial centroids, perform one iteration of the K-Means algorithm. (16 marks)

---

**Preparation Tips for Exam:**
* **Diagrams are Compulsory:** For questions on DBSCAN, Hierarchical (Dendrogram), or Grid-based methods, you **must** draw the diagrams to get full marks.
* **Comparison Tables:** Use the tables provided in the study guide for K-Means vs. K-Medoids and Agglomerative vs. Divisive.
* **Memorize Parameters:** Know exactly what $\epsilon$, MinPts, Threshold ($T$), and Branching Factor ($B$) mean.
* **Real-World Examples:** Use "Customer Segmentation" for K-Means and "Satellite Mapping" for STING to illustrate your points.


### Part A: Theory Questions (1–30)

1. Define Cluster Analysis. Why is it considered an unsupervised learning technique?

2. List and briefly explain the major categories of clustering methods covered in UNIT-4.

3. Explain Partitioning Methods in cluster analysis. Name any two standard algorithms under this category.

4. Describe the complete steps of the K-Means partitioning algorithm. Mention two major limitations.

5. Differentiate between K-Means and K-Medoids clustering algorithms.

6. What are Hierarchical Methods? Differentiate clearly between Agglomerative and Divisive Hierarchical Clustering.

7. Explain the step-by-step process of Agglomerative Hierarchical Clustering.

8. Define a Dendrogram. How does it help in choosing the optimal number of clusters?

9. Explain Probabilistic Model-based Clustering. How does it differ from partitioning and hierarchical methods?

10. Describe the BIRCH clustering technique and its two-phase approach. State its main advantage for large datasets.

11. Explain the DBSCAN clustering algorithm. Define the terms: core point, border point, and noise point with suitable examples.

12. What are the two input parameters of DBSCAN? Explain how changing Eps and MinPts affects the clustering result.

13. Describe the STING (Statistical Information Grid) clustering technique. Mention its key characteristics.

14. Explain the CLIQUE clustering algorithm. Why is it suitable for subspace clustering?

15. Compare and contrast DBSCAN (density-based) with STING and CLIQUE (grid-based) techniques.

16. What are the major challenges in cluster analysis? Give at least three challenges.

17. Discuss the evaluation of clustering techniques. Differentiate between internal and external evaluation measures.

18. Explain the Silhouette Coefficient for cluster validation. Write its formula and interpretation.

19. Describe the Davies-Bouldin Index. When is it preferred for evaluating clusters?

20. Explain the Elbow Method for determining the optimal number of clusters in partitioning methods.

21. How does the choice of distance metric (Euclidean, Manhattan, etc.) affect clustering results?

22. Discuss the scalability issues in clustering large datasets and how BIRCH addresses them.

23. Explain the concept of density-reachability and density-connectivity used in DBSCAN.

24. Compare the advantages and disadvantages of Hierarchical Clustering versus Partitioning Methods.

25. What is the difference between hard clustering and soft clustering? Which method in UNIT-4 falls under soft clustering?

26. Describe how Probabilistic Model-based Clustering handles uncertainty in cluster assignment.

27. Explain the working of the CLIQUE algorithm in high-dimensional data.

28. List three limitations of the DBSCAN clustering technique.

29. How can BIRCH, STING, and CLIQUE handle very large databases efficiently?

30. What are the key differences between density-based clustering and model-based clustering as per the syllabus?

---

### Part B: Numerical Problems (31–50)

**31. (K-Means – Partitioning)**  
Given 2D points: A(1,1), B(2,1), C(1,3), D(5,5), E(6,5), F(5,7).  
Apply K-Means with **K=2**. Initialize centroids as C₁ = A(1,1) and C₂ = D(5,5).  
Perform **two full iterations**. Find the final clusters, updated centroids, and the Sum of Squared Errors (SSE).

**32. (K-Means – Partitioning)**  
Points: P1(0,0), P2(0,2), P3(2,0), P4(8,8), P5(8,10), P6(10,8).  
K=2, initial centroids = P1(0,0) and P4(8,8).  
Perform iterations until convergence. Report final clusters and SSE.

**33. (K-Means – Partitioning)**  
Data points: (3,4), (4,3), (5,6), (6,5), (10,12), (11,11).  
K=3, initial centroids = (3,4), (5,6), (10,12).  
Show assignments and centroid updates after **one iteration** only. Calculate new SSE.

**34. (Agglomerative Hierarchical – Single Linkage)**  
Points: A(0,0), B(1,0), C(0,1), D(5,5), E(6,5).  
Compute the Euclidean distance matrix.  
Perform Agglomerative clustering using **Single Linkage**. Show the sequence of merges and the dendrogram heights.

**35. (Agglomerative Hierarchical – Complete Linkage)**  
Same points as Q34. Perform Agglomerative clustering using **Complete Linkage**. Draw the linkage steps and final hierarchy.

**36. (Agglomerative Hierarchical – Average Linkage)**  
Points: X(1,1), Y(2,3), Z(4,2), W(8,8), V(9,10).  
Compute distance matrix and apply Average Linkage. Show the dendrogram formation steps.

**37. (Divisive Hierarchical – Conceptual Numerical)**  
For the points in Q34, start with one cluster and perform the first split using divisive approach (split the cluster with maximum diameter). Show the diameter calculation and the resulting two clusters.

**38. (DBSCAN)**  
Points: P1(0,0), P2(0,1), P3(1,0), P4(1,1), P5(5,5), P6(5,6), P7(6,5), P8(10,10).  
Given **Eps = 1.5**, **MinPts = 3**.  
Identify core points, border points, noise points, and the final clusters using DBSCAN algorithm. Show density-reachability steps.

**39. (DBSCAN)**  
Points: A(2,2), B(2,3), C(3,2), D(3,3), E(7,7), F(7,8), G(8,7), H(12,12), I(0,10).  
Eps = 1.2, MinPts = 3. Classify all points and form clusters. Mark any noise.

**40. (DBSCAN Parameter Sensitivity)**  
Using points of Q38, change Eps to 2.0 (keep MinPts=3). Re-run DBSCAN and show how the number of clusters changes.

**41. (BIRCH – Phase Numerical)**  
Consider a large set of 2D points (assume 100 points). Explain numerically why BIRCH’s CF-tree (Clustering Feature) is used instead of storing all points. Compute a simple CF = (N, LS, SS) for the first three points: (1,1), (2,1), (1,2).

**42. (STING – Grid-based)**  
Divide the 2D space [0–10, 0–10] into a 2×2 grid. Given points: (1,2), (2,1), (8,9), (9,8).  
Compute statistical parameters (mean, count) for each cell. Show how STING decides which cells are relevant for clustering.

**43. (CLIQUE – Subspace)**  
In 2D space with points: (1,1), (1,2), (2,1), (5,5), (5,6), (6,5).  
Apply CLIQUE with minimum density threshold = 2. Identify dense units and form clusters in the subspace.

**44. (Silhouette Coefficient – Evaluation)**  
Two clusters formed:  
Cluster 1: (1,1), (2,2)  
Cluster 2: (8,8), (9,9)  
For point (1,1), calculate its silhouette coefficient (a = intra-distance, b = nearest-cluster distance).

**45. (Silhouette Coefficient – Evaluation)**  
Clusters: C1 = {(0,0),(0,1),(1,0)}, C2 = {(5,5),(6,5)}.  
Compute the average Silhouette score of the entire dataset.

**46. (Davies-Bouldin Index – Evaluation)**  
Two clusters:  
C1 centroid (2.5, 2), points (1,1),(2,2),(3,3)  
C2 centroid (8,8), points (7,7),(8,8),(9,9)  
Compute Davies-Bouldin Index (use Euclidean distance).

**47. (SSE Calculation – Partitioning Evaluation)**  
After K-Means (K=2) on points (1,1),(1,3),(2,2),(5,5),(6,5),(5,7), the final clusters are given as:  
Cluster 1: (1,1),(1,3),(2,2)  
Cluster 2: (5,5),(6,5),(5,7)  
Calculate the total SSE.

**48. (Rand Index – External Evaluation)**  
True labels: Cluster A = {P1,P2,P3}, Cluster B = {P4,P5,P6}  
Predicted clusters: Cluster X = {P1,P2,P4}, Cluster Y = {P3,P5,P6}  
Compute the Rand Index.

**49. (Elbow Method – Numerical)**  
SSE values for K=1 to 5: K=1: 180, K=2: 60, K=3: 25, K=4: 22, K=5: 20.  
Plot (mentally) and identify the optimal K using the Elbow Method. Justify your answer.

**50. (Hierarchical + Evaluation)**  
Using points of Q34, after agglomerative single linkage, cut the dendrogram at height = 4.0.  
Form the clusters and compute the Silhouette Coefficient for the resulting partitioning.

