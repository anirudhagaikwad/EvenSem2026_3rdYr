# CLIQUE: Clustering In QUEst

While **STING** is great for looking at the big picture, it struggles when data has many dimensions (features). **CLIQUE** (Clustering In QUEst) is a hybrid algorithm that combines **Grid-based** and **Density-based** clustering to find clusters in high-dimensional data. 

---

## 1. The Scenario: The High-Dimensional Shadow
Imagine you are a detective trying to find a criminal in a massive 50-story building. 
* **The Problem:** Searching the whole building at once is impossible. 
* **The CLIQUE Solution:** You look at the building from the side (2D) and notice a shadow on the ground floor. You then look from the front and see the same shadow. 
* **The Logic:** If a "crowded" cluster exists in 50 dimensions, it **must** also look crowded when you look at it in 1 dimension or 2 dimensions. CLIQUE starts with 1D, finds the crowded spots, and then only looks for 2D clusters in those specific spots.

---

## 2. Core Concept: Subspace Clustering
In high-dimensional spaces, data points are often very spread out (the "curse of dimensionality"). CLIQUE solves this by finding **Subspace Clusters**.
* It partitions each dimension into non-overlapping intervals (a grid).
* It identifies "dense" units—cells that contain more than a certain number of data points ($tau$).



---

## 3. The Apriori Property of CLIQUE
CLIQUE uses a logic similar to the **Apriori Algorithm** you learned in Unit 2:
* **The Rule:** If a $k$-dimensional cell is dense, then all of its $(k-1)$-dimensional projections must also be dense.
* **How it works:** 1. Find all dense 1D intervals.
    2. Combine dense 1D intervals to find potential dense 2D cells.
    3. Combine dense 2D cells to find 3D cells, and so on.
    4. This "pruning" saves the computer from checking billions of empty cells.

---

## 4. How the Algorithm Works
1.  **Partitioning:** Divide the data space into a grid of units.
2.  **Identification:** Find all dense units in all subspaces using the bottom-up (Apriori) approach.
3.  **Clustering:** Connect adjacent dense units to form larger clusters.
4.  **Generation:** Generate a minimal description (rules) for each cluster.



---

## 5. Advantages

* **High-Dimensional Expert:** It is specifically designed to find clusters that are "hidden" in specific dimensions of huge datasets.
* **No Pre-set K:** Like DBSCAN, it automatically finds the number of clusters.
* **Interpretability:** It provides a simple "if-then" description of the clusters it finds.
* **Scalability:** It scales linearly with the number of data points.

---

## 6. The Limitations (The Catch)

* **Accuracy vs. Grid Size:** Just like STING, if the grid intervals are too large, you lose accuracy; if they are too small, you increase computation.
* **Complexity:** As the number of dimensions increases, the number of potential subspaces to check can still become very large.

---

## 7. Comparison Table: STING vs. CLIQUE

| Feature | STING | CLIQUE |
| :--- | :--- | :--- |
| **Category** | Purely Grid-based | Hybrid (Grid + Density) |
| **Strategy** | Top-Down (Querying) | Bottom-Up (Subspace building) |
| **Best For** | Fast spatial queries | High-dimensional data |
| **Logic** | Statistical Summaries | Dense Unit Projections |

---

# Algorithm: STING (Statistical Information Grid)

STING is a grid-based multi-resolution clustering technique. It divides the spatial area into rectangular cells and stores statistical information about them, allowing for fast, query-based clustering.

---

## 1. Basic Working Steps
1.  **Grid Partitioning:** Divide the input space into a hierarchical grid of rectangular cells (multiple levels).
2.  **Pre-computation:** Calculate and store statistical parameters (mean, count, etc.) for each cell at the bottom level and propagate them upward to the parent levels.
3.  **Query Processing:** Start at the top level of the grid.
4.  **Probability Filtering:** For each cell in the current level, calculate the probability that it satisfies the user's query.
5.  **Pruning:** Discard irrelevant cells. Move down to the next (finer) level for relevant cells.
6.  **Final Result:** Continue until the bottom level is reached. Return the regions formed by the remaining dense cells.

---

## 2. Key Formulas

### **A. Cell Statistics**
Each cell stores a vector of parameters:
* **n:** Number of points.
* **m:** Mean.
* **s:** Standard deviation.
* **min / max:** Range of values.
* **dist:** Distribution type (Normal, Uniform, etc.).

### **B. Bottom-Up Propagation**
Parameters of a parent cell are calculated from its $k$ children:
$$n_{parent} = \sum_{i=1}^{k} n_{child\_i}$$
$$m_{parent} = \frac{\sum (m_{child\_i} \times n_{child\_i})}{n_{parent}}$$



---

## 3. Practical Example

**Scenario: Find "dense" areas with more than 10 points.**

### **Step 1: Top Level (Level 1)**
The whole map is one cell with $n=100$. Since $100 > 10$, we move to Level 2.

### **Step 2: Level 2 (Divided into 4 cells: C1, C2, C3, C4)**
* C1 ($n=5$), C2 ($n=45$), C3 ($n=40$), C4 ($n=10$).
* **Decision:** C1 is pruned (too few points). C4 is borderline. C2 and C3 are kept.

### **Step 3: Level 3 (Zooming into C2 and C3)**
The algorithm only looks at the sub-grid cells inside C2 and C3. It finds that specific sub-cells are very crowded and merges them to define the "Cluster."

**Decision:** STING is very fast because it never looks at the millions of raw points during the query; it only looks at the small number of grid cells.