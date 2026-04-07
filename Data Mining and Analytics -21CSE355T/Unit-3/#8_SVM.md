# Support Vector Machines (SVM)

**Support Vector Machines (SVM)** are among the most robust and mathematically elegant classification algorithms in data mining. While other algorithms try to find any boundary that works, SVM is obsessed with finding the **Optimal Hyperplane** — the one that provides the greatest "safety buffer" between classes.

---

## 1. The Geometry of the "Safety Buffer"
The power of SVM lies in its objective: maximizing the **Margin**.

* **The Hyperplane:** In a 2D space, this is a line. In 3D, it's a plane. In N-dimensions, it's a hyperplane. It is defined by the equation:
  $$w \cdot x + b = 0$$
* **Support Vectors:** These are the "VIP" data points. They are the observations that lie exactly on the marginal boundaries. If you remove any other data points, the hyperplane stays the same; but if you move a Support Vector, the entire model changes.
* **Maximum Margin:** The distance between the hyperplane and the nearest data point from either class. A larger margin leads to better generalization on new data.

![svm](./imgs/working_of_svm.jpg)

### **Why Maximum Margin?**

Intuitively, a classifier with a larger margin is more confident and more tolerant of small perturbations in new data. This is supported by **VC theory** (Vapnik-Chervonenkis): for a fixed number of training errors, a classifier with a larger margin has a lower VC dimension and therefore a tighter upper bound on generalisation error.

$$\text{Generalisation Error} \leq \text{Training Error} + \sqrt{\frac{VC\_dimension \cdot \ln(n) - \ln(\delta)}{n}}$$

A larger margin → lower VC dimension → tighter bound → better performance on unseen data.

### **Margin Width Formula**

The two marginal hyperplanes are:
$$w \cdot x + b = +1 \quad \text{(positive class boundary)}$$
$$w \cdot x + b = -1 \quad \text{(negative class boundary)}$$

The perpendicular distance between them is:
$$\text{Margin} = \frac{2}{\|w\|}$$

Maximising the margin is equivalent to **minimising $\|w\|$**, or equivalently $\frac{1}{2}\|w\|^2$ (for mathematical convenience in differentiation).

---

## 2. Linear SVM: The Mathematical Goal

For a dataset that is linearly separable, SVM tries to solve a constrained optimization problem. We want to minimize the weight vector $w$ (which maximizes the margin) subject to the condition that all points are correctly classified:

$$\text{Minimize } \frac{1}{2} \|w\|^2$$
$$\text{Subject to: } y_i(w \cdot x_i + b) \ge 1 \quad \forall i$$

To solve this, SVM uses **Lagrange Multipliers**, converting the problem into a "Dual Form" that only depends on the dot product of the input vectors.

### **Lagrangian Formulation**

Introduce a Lagrange multiplier $\alpha_i \geq 0$ for each constraint:
$$\mathcal{L}(w, b, \alpha) = \frac{1}{2}\|w\|^2 - \sum_{i=1}^{n} \alpha_i [y_i(w \cdot x_i + b) - 1]$$

Taking partial derivatives and setting to zero gives the **Dual Problem**:
$$\text{Maximise } \sum_{i=1}^{n} \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j (x_i \cdot x_j)$$
$$\text{Subject to: } \alpha_i \geq 0 \text{ and } \sum_{i=1}^{n} \alpha_i y_i = 0$$

**Key insight:** Only support vectors have $\alpha_i > 0$. All other points have $\alpha_i = 0$ and are irrelevant to the solution. This makes SVM memory-efficient after training.

### **Decision Function**
Once solved, a new point $x$ is classified by:
$$f(x) = \text{sign}\left(\sum_{i \in SV} \alpha_i y_i (x_i \cdot x) + b\right)$$

---

## 3. Soft Margin SVM: Handling Real-World Noise

Real data is rarely perfectly separable. **Soft Margin SVM** introduces **slack variables** $\xi_i \geq 0$ that allow some points to violate the margin:

$$\text{Minimize } \frac{1}{2}\|w\|^2 + C \sum_{i=1}^{n} \xi_i$$
$$\text{Subject to: } y_i(w \cdot x_i + b) \geq 1 - \xi_i \quad \text{and} \quad \xi_i \geq 0$$

Where:
* $\xi_i = 0$: point is correctly classified and outside the margin (no penalty)
* $0 < \xi_i \leq 1$: point is inside the margin but correctly classified
* $\xi_i > 1$: point is misclassified

The **C parameter** controls the tradeoff:

| C Value | Margin | Misclassifications Allowed | Risk |
|:---|:---|:---|:---|
| Very small ($C \to 0$) | Very wide | Many | Underfitting |
| Small | Wide | Some | Balanced (soft margin) |
| Large | Narrow | Few | Overfitting |
| Very large ($C \to \infty$) | Minimal | None | Hard margin (overfits noise) |

---

## 4. The Kernel Trick: Moving to Higher Dimensions

Real-world data is rarely a straight line. Sometimes, data points of Class A are surrounded by Class B.

**The Logic:** If we cannot separate data in 2D, we project it into 3D (or higher). In this new space, we can pass a flat "sheet" (hyperplane) through the data.


### **Why the "Trick"?**

Explicitly computing the transformed features $\phi(x)$ in a very high (or infinite) dimensional space would be computationally prohibitive. The **Kernel Trick** bypasses this by computing the dot product in the transformed space **without ever computing $\phi(x)$ explicitly**:

$$K(x_i, x_j) = \phi(x_i) \cdot \phi(x_j)$$

We simply replace every dot product $(x_i \cdot x_j)$ in the dual formulation with a kernel evaluation $K(x_i, x_j)$.

### **Common Kernel Functions**

#### **1. Linear Kernel**
$$K(x_i, x_j) = x_i \cdot x_j$$
* No transformation. Used when data is already linearly separable.
* Fastest to compute. Equivalent to standard linear SVM.

#### **2. Polynomial Kernel**
$$K(x_i, x_j) = (x_i \cdot x_j + c)^d$$
* $d$ = degree of the polynomial, $c$ = constant (typically 1).
* Captures interaction terms up to degree $d$.
* **Example:** $d=2$ can separate XOR-like patterns.

#### **3. Radial Basis Function (RBF / Gaussian)**
$$K(x_i, x_j) = \exp\left(-\gamma \|x_i - x_j\|^2\right)$$
* The most popular kernel — equivalent to projecting into **infinite-dimensional** space.
* $\gamma$ controls the "reach" of each support vector.
* Creates smooth, circular boundaries.

#### **4. Sigmoid Kernel**
$$K(x_i, x_j) = \tanh(\kappa \cdot x_i \cdot x_j + c)$$
* Mimics the activation function of neural networks.
* Not always a valid kernel (may not satisfy Mercer's condition for all parameter choices).

### **Kernel Comparison**

| Kernel | Formula | Parameters | Best For |
|:---|:---|:---|:---|
| Linear | $x_i \cdot x_j$ | None | High-dim text, linearly separable |
| Polynomial | $(x_i \cdot x_j + c)^d$ | $d$, $c$ | Image recognition, moderate complexity |
| RBF (Gaussian) | $\exp(-\gamma\|x_i - x_j\|^2)$ | $\gamma$ | General-purpose, default choice |
| Sigmoid | $\tanh(\kappa x_i \cdot x_j + c)$ | $\kappa$, $c$ | Neural-net-like boundaries |

---

## 5. Tuning the SVM: Hyperparameters

To get the best performance, two parameters must be tuned carefully:

### **A. The C Parameter (Regularization)**
* **Small C:** Prioritizes a large margin, even if it means some training points are misclassified (Soft Margin). This prevents overfitting.
* **Large C:** Prioritizes classifying all training points correctly, even if the margin becomes very small. This can lead to overfitting.

### **B. Gamma ($\gamma$) — RBF Kernel Only**
* **Low Gamma:** The "influence" of a support vector reaches far. The boundary is smooth.
* **High Gamma:** The "influence" is local. The boundary is very wiggly and tries to "hug" every single data point.

### **Gamma Effect Visualised**

```
Low γ:                        High γ:
  ·····○○○○                     ·····○
 ·····○○○○○                    ····○○○
··········○○        →→→       ···○○○○○○
··········○○                   ··○○○○○
  ··········                    ·○○○○
Smooth, generalised            Wiggly, overfitted
```

### **Hyperparameter Grid Search (C, γ)**

The standard approach is to search over a logarithmic grid:

| C \ γ | 0.001 | 0.01 | 0.1 | 1 |
|:---|:---|:---|:---|:---|
| **0.1** | Test each combo | ... | ... | ... |
| **1** | ... | ... | ... | ... |
| **10** | ... | ... | ... | ... |
| **100** | ... | ... | ... | ... |

Use **5-fold cross-validation** at each grid point to find the combination with the best validation accuracy.

---

## 6. Multi-Class Classification

SVM is naturally a binary classifier (Class A vs Class B). To handle multiple classes (e.g., Apple vs Orange vs Banana), it uses two strategies:

### **One-vs-One (OvO)**
* Builds $\frac{k(k-1)}{2}$ binary classifiers, one for each pair of classes.
* For $k=4$ classes: $\frac{4 \times 3}{2} = 6$ classifiers.
* Final prediction: majority vote among all classifiers.
* **Pro:** Each classifier trains on a small subset of data (fast).
* **Con:** Many classifiers needed for large $k$.

### **One-vs-All (OvA)**
* Builds $k$ binary classifiers: each class vs. all others combined.
* For $k=4$: 4 classifiers.
* Final prediction: the class whose classifier gives the highest confidence score.
* **Pro:** Fewer classifiers needed.
* **Con:** Class imbalance in each sub-problem (one class vs. many).

### **Multi-Class Comparison**

| Strategy | # Classifiers | Training Size per Classifier | Voting |
|:---|:---|:---|:---|
| One-vs-One (OvO) | $k(k-1)/2$ | Small (2 classes only) | Majority vote |
| One-vs-All (OvA) | $k$ | Full dataset | Highest score |

---

## 7. SVM for Regression: SVR

SVM extends naturally to **Support Vector Regression (SVR)**. Instead of maximising a margin for classification, SVR fits a "tube" of width $2\varepsilon$ around the data and ignores errors within that tube:

$$\text{Minimize } \frac{1}{2}\|w\|^2 + C\sum(\xi_i + \xi_i^*)$$
$$\text{Subject to: } y_i - (w \cdot x_i + b) \leq \varepsilon + \xi_i$$
$$\quad\quad\quad\quad (w \cdot x_i + b) - y_i \leq \varepsilon + \xi_i^*$$

* $\varepsilon$ controls the width of the insensitive tube (errors smaller than $\varepsilon$ are ignored).
* Points outside the tube become support vectors and incur a cost.

---

## 8. Comparison Table: SVM vs. The Rest

| Feature | Naive Bayes | Decision Trees | Neural Network | SVM |
| :--- | :--- | :--- | :--- | :--- |
| **Foundation** | Probability | Logic/Rules | Biological neurons | Geometry/Optimization |
| **Boundary** | Linear/Simple | Axis-Parallel Steps | Complex curves | Smooth/Complex Curves |
| **Outliers** | Robust | Sensitive | Sensitive | Robust (due to Margin) |
| **Small Data** | Good | Moderate | Poor | Excellent |
| **Large Data** | Excellent | Good | Excellent | Poor ($O(n^3)$) |
| **High Dimensions** | Good | Poor | Good | Excellent |
| **Interpretability** | High | Very High | Very Low | Low |
| **Kernel Needed** | No | No | No | For non-linear data |

---

## 9. When to Choose SVM?
* Use SVM when you have a **clear margin of separation**.
* Use SVM when your data has **high dimensions** (e.g., gene sequences or text features).
* Use SVM when you have **small to medium datasets** (thousands of samples).
* Avoid SVM if your dataset is **extremely large** (millions of rows) because the training time increases cubically ($O(n^3)$).
* Avoid SVM when you need **probability outputs** (SVM gives hard class labels by default; probabilities require Platt scaling).

### **SVM vs. Logistic Regression**

| Aspect | SVM | Logistic Regression |
|:---|:---|:---|
| Objective | Maximise margin | Maximise likelihood |
| Output | Hard label (sign) | Probability (sigmoid) |
| Outlier sensitivity | Low (margin focus) | Moderate |
| High-dim data | Excellent | Good |
| Kernel support | Yes | No (linear only) |
| Training speed | Slow ($O(n^3)$) | Fast ($O(n)$) |

---

## 10. Python Implementation

```python
from sklearn.svm import SVC, SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

# --- IMPORTANT: SVM requires feature scaling ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# --- 1. Linear SVM ---
linear_svm = SVC(kernel='linear', C=1.0)
linear_svm.fit(X_train_scaled, y_train)
print("Linear SVM Accuracy:", accuracy_score(y_test, linear_svm.predict(X_test_scaled)))
print("Number of Support Vectors:", linear_svm.n_support_)  # per class

# --- 2. RBF SVM ---
rbf_svm = SVC(kernel='rbf', C=10, gamma=0.1)
rbf_svm.fit(X_train_scaled, y_train)
print("RBF SVM Accuracy:", accuracy_score(y_test, rbf_svm.predict(X_test_scaled)))

# --- 3. Polynomial SVM ---
poly_svm = SVC(kernel='poly', degree=3, C=1.0)
poly_svm.fit(X_train_scaled, y_train)
print("Poly SVM Accuracy:", accuracy_score(y_test, poly_svm.predict(X_test_scaled)))

# --- 4. Grid Search for Best C and Gamma ---
param_grid = {
    'C':     [0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1],
    'kernel': ['rbf']
}
grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train_scaled, y_train)
print("Best Parameters:", grid_search.best_params_)
print("Best CV Accuracy:", grid_search.best_score_)

# --- 5. Get probability estimates (requires probability=True) ---
prob_svm = SVC(kernel='rbf', C=10, gamma=0.1, probability=True)
prob_svm.fit(X_train_scaled, y_train)
proba = prob_svm.predict_proba(X_test_scaled)
print("Class probabilities (first sample):", proba[0])

# --- 6. Classification report ---
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))
```

> **Critical Note:** SVM is sensitive to feature scale. Always apply `StandardScaler` before training. Without scaling, features with larger ranges dominate the margin calculation.

---

### **Key Takeaways**
> SVM doesn't just look for *a* solution; it looks for the **strongest** solution by maximising the gap between classes. Through the **Kernel Trick**, it can solve problems that appear impossible in lower dimensions. The support vectors alone define the model — making SVM elegantly sparse and robust to outliers far from the margin.

---

# Algorithm: Support Vector Machines (SVM)

Support Vector Machines (SVM) is a classifier that finds the optimal hyperplane which maximizes the margin between two classes. It is highly effective for both linear and non-linear data (using the Kernel Trick).

---

## 1. Basic Working Steps
1.  **Map Data:** Plot the data points in an $n$-dimensional space (where $n$ is the number of features).
2.  **Identify Support Vectors:** Find the data points from each class that are closest to the boundary. These points are the "Support Vectors."
3.  **Calculate Hyperplane:** Determine the decision boundary (hyperplane) that is equidistant from the support vectors of both classes.
4.  **Maximize Margin:** Adjust the hyperplane to ensure the distance (margin) between the support vectors of the two classes is as large as possible.
5.  **Kernel Trick (Optional):** If data is not linearly separable, use a kernel function to project data into a higher dimension where a linear split is possible.

---

## 2. Key Formulas

### **A. Hyperplane Equation**
For a linear SVM, the decision boundary is:
$$w \cdot x + b = 0$$
* $w$ = Weight vector (normal to the hyperplane).
* $b$ = Bias (offset).

### **B. The Margin**
The distance between the two supporting planes ($w \cdot x + b = 1$ and $w \cdot x + b = -1$) is:
$$\text{Margin} = \frac{2}{\|w\|}$$
To get the maximum margin, we must **minimize** $\|w\|$.

### **C. Optimization Problem (Hard Margin)**
$$\text{Minimize } \frac{1}{2}\|w\|^2 \quad \text{subject to } y_i(w \cdot x_i + b) \geq 1$$

### **D. Soft Margin (with slack variables)**
$$\text{Minimize } \frac{1}{2}\|w\|^2 + C\sum_{i=1}^{n}\xi_i \quad \text{subject to } y_i(w \cdot x_i + b) \geq 1 - \xi_i$$

### **E. Kernel Function (RBF)**
To handle non-linear data:
$$K(x_i, x_j) = \exp(-\gamma \|x_i - x_j\|^2)$$

### **F. Decision Function**
$$f(x) = \text{sign}\left(\sum_{i \in SV} \alpha_i y_i K(x_i, x) + b\right)$$


---

## 3. Practical Example

**Scenario: Classifying "Healthy" vs "Sick" based on two blood markers.**

| Patient | Marker A ($x_1$) | Marker B ($x_2$) | Class ($y$) |
| :--- | :--- | :--- | :--- |
| 1 | 2 | 2 | Healthy (+1) |
| 2 | 2 | 3 | Healthy (+1) |
| 3 | 5 | 5 | Sick (-1) |
| 4 | 6 | 5 | Sick (-1) |

### **Step 1: Identify Support Vectors**
By plotting the points, we see that Patient 1 $(2,2)$ and Patient 3 $(5,5)$ are the closest points to the "middle" between the two groups. These are our **Support Vectors**.

### **Step 2: Find the Hyperplane**
The middle point between $(2,2)$ and $(5,5)$ is roughly $(3.5, 3.5)$.
A simple linear boundary could be: $x_1 + x_2 - 7 = 0$.

**Verify the margin constraint:**
* Patient 1: $y_i(w \cdot x_i + b) = (+1)(2 + 2 - 7) = -3$ ← not scaled to ±1 yet

After proper scaling, the normal vector $w = (1, 1)$ gives $\|w\| = \sqrt{2}$, so:
$$\text{Margin} = \frac{2}{\sqrt{2}} = \sqrt{2} \approx 1.414$$

### **Step 3: Test a New Point**
New Patient: {Marker A = 1, Marker B = 1}
* $1 + 1 - 7 = -5$
* Since the result is **negative** (falling on the "Healthy" side of the plane), the patient is classified as **Healthy**.

### **Step 4: Test a Boundary Case**
New Patient: {Marker A = 3, Marker B = 4}
* $3 + 4 - 7 = 0$
* This point falls exactly **on the hyperplane** — maximum uncertainty. In practice, classify by the sign convention (assign to positive or negative class based on implementation).

**Decision:** The SVM creates a "clearance zone" (margin of width $\sqrt{2}$). Even if the new patient had slightly higher markers, they would still safely fall into the Healthy cluster because of the maximized margin.

---

## 4. Quick Reference Card

| Concept | Formula | Notes |
|:---|:---|:---|
| Hyperplane | $w \cdot x + b = 0$ | Decision boundary |
| Margin width | $\frac{2}{\|w\|}$ | Maximise this |
| Hard margin objective | $\min \frac{1}{2}\|w\|^2$ s.t. $y_i(w \cdot x_i + b) \geq 1$ | Linearly separable |
| Soft margin | $\min \frac{1}{2}\|w\|^2 + C\sum\xi_i$ | Allows violations |
| RBF kernel | $\exp(-\gamma\|x_i - x_j\|^2)$ | Most popular kernel |
| Polynomial kernel | $(x_i \cdot x_j + c)^d$ | Degree-$d$ boundary |
| Decision function | $\text{sign}(\sum \alpha_i y_i K(x_i, x) + b)$ | Final classification |
| Large C | Narrow margin, low training error | Risk of overfitting |
| Small C | Wide margin, some misclassification | Better generalisation |
| Large $\gamma$ | Local influence, wiggly boundary | Risk of overfitting |
| Small $\gamma$ | Global influence, smooth boundary | Better generalisation |