# STING: Statistical Information Grid

If DBSCAN is like finding popular crowds, **STING** (Statistical Information Grid) is like looking at a satellite map of a city. Instead of looking at every individual person, it divides the map into a grid of squares and stores statistics about what is happening inside each square.

---

## 1. The Scenario: The High-Resolution Satellite
Imagine you are a weather researcher studying a massive forest.
* **The Problem:** You have 100 million trees. You can't measure the health of every single leaf.
* **The STING Solution:** You divide the forest into 1,000 large squares. Inside each square, you record the "average health" and "color." Then, you divide each of those squares into 100 smaller squares for more detail.
* **The Query:** When someone asks, "Where are the healthiest trees?", you don't look at 100 million leaves. You start with the large squares, discard the "unhealthy" ones, and only zoom into the smaller squares of the "healthy" areas.

---

## 2. The Hierarchical Grid Structure
STING is a **Grid-based** multi-resolution clustering technique. 
* **The Layers:** The spatial area is divided into rectangular cells. There are several levels of such rectangular cells, and these levels form a hierarchical structure.
* **Parent-Child Relationship:** Each cell at a high level (except the bottom) is partitioned to form several cells at the next lower level.



---

## 3. Cell Statistics (What is stored?)
For each cell in the grid, STING pre-computes and stores statistical information. You don't need the original data points once these are calculated:
* **$n$:** The total number of points in the cell.
* **$m$:** The mean (average) of the points.
* **$s$:** The standard deviation.
* **$min / max$:** The minimum and maximum values.
* **$dist$:** The type of distribution (e.g., Normal, Uniform, Exponential).

---

## 4. How the Algorithm Works (Top-Down Querying)
1. **Start at the Top:** Start with the topmost (coarsest) layer of the grid.
2. **Calculate Probability:** For each cell in the current layer, calculate the probability that it contains data relevant to the user's query.
3. **Prune:** If a cell is irrelevant, discard it and all its "children".
4. **Zoom In:** Move down to the next level and repeat the process for only the relevant cells.
5. **Final Result:** Continue until the bottom layer is reached, and return the regions that satisfy the query.

---

## 5. Why Students Love STING (Advantages)

* **Extremely Fast:** Since it uses pre-computed statistics, the query processing time is independent of the number of data points. It is $O(g)$, where $g$ is the number of grid cells at the bottom layer.
* **Parallel Processing:** Each cell can be processed independently, making it great for modern computers.
* **Incremental Updates:** If a new data point is added, you only need to update the statistics of the specific cells it belongs to, not the whole tree.

---

## 6. The Limitations (The Catch)

* **Grid Accuracy:** The quality of the clusters depends on the "granularity" (size) of the bottom-level grid. If the grid is too big, you lose detail.
* **Rectangular Bias:** Because it uses a grid, the cluster boundaries are always horizontal or vertical (rectangular), which might not fit the natural "curvy" shape of data.

---

## 7. Comparison Table

| Feature | DBSCAN (Density-Based) | STING (Grid-Based) |
| :--- | :--- | :--- |
| **Data Access** | Looks at individual points | Looks at cell summaries |
| **Speed** | Slows down as points increase ($O(n^2)$) | Very fast, independent of point count |
| **Boundary** | Arbitrary/Curvy shapes | Rectangular/Grid shapes |
| **Outliers** | Excellent at detection | Handles outliers as cell statistics |

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