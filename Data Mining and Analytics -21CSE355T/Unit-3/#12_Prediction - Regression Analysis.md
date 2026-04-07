# Prediction - Regression Analysis

### **Description**
In data mining, **Prediction** is the process of identifying patterns in historical data to forecast future numerical outcomes. While classification focuses on "Which category?", prediction focuses on "How much?".
**Regression Analysis** is the primary statistical methodology used for this task. It builds a mathematical relationship between known variables to predict a continuous, ordered value.

![regression](./imgs/classification-vs-regression.webp)

---

## 1. What is Regression Analysis?
Regression is a way to model the relationship between a **Dependent Variable** (the target result) and one or more **Independent Variables** (the input factors).

* **Dependent Variable ($Y$):** The value you are trying to predict (e.g., Temperature, Price).
* **Independent Variable ($X$):** The variables that influence the target (e.g., Humidity, Location).


### **The Regression Equation — Intuition**

Every regression model answers: *"If $X$ changes by 1 unit, how much does $Y$ change?"*

* $\beta_0$ (**Intercept**): The predicted value of $Y$ when all $X$ = 0.
* $\beta_1$ (**Slope / Coefficient**): The average change in $Y$ for a one-unit increase in $X$.
* $\epsilon$ (**Error / Residual**): The difference between the actual $Y$ and the predicted $\hat{Y}$ — captures everything the model doesn't explain.

---

## 2. Types of Regression Analysis

### **A. Linear Regression**
It assumes the relationship between $X$ and $Y$ is a straight line.

* **Simple Linear Regression:** Predicts $Y$ using only one $X$.
$$Y = \beta_0 + \beta_1 X + \epsilon$$

* **Multiple Linear Regression:** Predicts $Y$ using a combination of multiple $X$ variables.
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_n X_n + \epsilon$$

In matrix form (useful for computation):
$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$$

**Key Assumptions of Linear Regression (LINE):**
* **L**inearity: The relationship between $X$ and $Y$ is linear.
* **I**ndependence: Observations are independent of each other.
* **N**ormality: Residuals are normally distributed.
* **E**qual Variance (Homoscedasticity): Residuals have constant variance across all $X$.

### **B. Non-Linear (Polynomial) Regression**
Used when data points don't follow a straight line but rather a curve or a wave.

$$Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \beta_3 X^3 + \dots + \beta_d X^d + \epsilon$$

* $d$ = degree of the polynomial (e.g., $d=2$ gives a parabola, $d=3$ gives an S-curve).
* **Warning:** High-degree polynomials overfit easily — the curve "wiggles" through every training point but fails on new data.

![typesofreg](./imgs/linearReg1.jpg)

### **C. Logistic Regression**
**Important Note:** Despite having "Regression" in its name, Logistic Regression is used for **Classification**. It maps any real-valued number into a value between 0 and 1 using the Sigmoid function, predicting probabilities for discrete classes.

$$P(Y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X_1 + \dots + \beta_n X_n)}}$$

[Image comparing Linear Regression line vs Logistic Regression S-curve]

![logisticreg](./imgs/logireg.png)

**Log-Odds (Logit) Interpretation:**
$$\log\left(\frac{P}{1-P}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_n X_n$$

* Each $\beta_i$ represents the change in **log-odds** for a 1-unit increase in $X_i$.
* Exponentiated: $e^{\beta_i}$ = **Odds Ratio** (how many times more likely the outcome is).

### **D. Ridge Regression (L2 Regularisation)**
Standard linear regression can overfit when there are many features or multicollinearity. Ridge adds an L2 penalty to shrink coefficients:
$$\text{Minimise: } \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} \beta_j^2$$

* $\lambda$ = regularisation strength. Higher $\lambda$ → smaller coefficients → simpler model.
* **No coefficient becomes exactly zero** (unlike LASSO).
* Best when all features contribute a little but none should be fully discarded.

### **E. LASSO Regression (L1 Regularisation)**
LASSO (Least Absolute Shrinkage and Selection Operator) adds an L1 penalty:
$$\text{Minimise: } \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |\beta_j|$$

* **Some coefficients become exactly zero** → automatic feature selection.
* Best when you believe many features are irrelevant (sparse model).

### **F. Elastic Net**
Combines L1 and L2 penalties:
$$\text{Minimise: } SSE + \lambda_1 \sum|\beta_j| + \lambda_2 \sum\beta_j^2$$

Best of both worlds — handles correlated features (Ridge) while still performing feature selection (LASSO).

### **Regression Types Summary**

| Type | When to Use | Handles Overfitting? | Feature Selection? |
|:---|:---|:---|:---|
| Simple Linear | One predictor, linear | Limited | No |
| Multiple Linear | Many predictors, linear | Limited | No |
| Polynomial | Non-linear curve | Risk of overfit | No |
| Logistic | Binary/multi-class target | Limited | No |
| Ridge (L2) | Multicollinearity present | ✅ Yes | No |
| LASSO (L1) | Sparse features expected | ✅ Yes | ✅ Yes |
| Elastic Net | Many correlated features | ✅ Yes | ✅ Yes |

---

## 3. How the Model Learns: Ordinary Least Squares (OLS)
The most common way to train a regression model is **Ordinary Least Squares (OLS)**.

1. **Residuals:** For every data point, the model calculates the vertical distance (error) between the actual point and the predicted line.
2. **Squaring:** It squares these distances (to remove negative values and punish large errors).
3. **Minimization:** The algorithm mathematically finds the line where the **Sum of Squared Errors (SSE)** is the lowest possible.

$$SSE = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$


### **Deriving OLS Coefficients (Simple Linear Regression)**

Setting the derivative of SSE to zero and solving:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} = \frac{S_{xy}}{S_{xx}}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

Where $\bar{x}$ and $\bar{y}$ are the sample means of $X$ and $Y$.

**Matrix Solution (Multiple Regression):**
$$\hat{\boldsymbol{\beta}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$

This gives the **exact optimal solution** in one step — no iteration needed (unlike Gradient Descent).

### **Gradient Descent Alternative**

For very large datasets where matrix inversion is expensive ($O(p^3)$), **Gradient Descent** iteratively finds the minimum:
$$\beta_j \leftarrow \beta_j - \eta \cdot \frac{\partial SSE}{\partial \beta_j} = \beta_j - \eta \cdot \frac{2}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)(-x_{ij})$$

Where $\eta$ is the learning rate.

---

## 4. Full Worked Example: Simple Linear Regression

**Dataset:** Predict house price ($Y$) from size in $m^2$ ($X$).

| House | Size ($X$) | Price ($Y$) |
|:---|:---|:---|
| 1 | 50 | 150 |
| 2 | 70 | 200 |
| 3 | 80 | 250 |
| 4 | 100 | 300 |
| 5 | 120 | 350 |

**Step 1: Calculate means**
$$\bar{X} = \frac{50+70+80+100+120}{5} = 84, \quad \bar{Y} = \frac{150+200+250+300+350}{5} = 250$$

**Step 2: Calculate $S_{xy}$ and $S_{xx}$**

| $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i-\bar{x})(y_i-\bar{y})$ | $(x_i-\bar{x})^2$ |
|:---|:---|:---|:---|:---|:---|
| 50 | 150 | -34 | -100 | 3400 | 1156 |
| 70 | 200 | -14 | -50 | 700 | 196 |
| 80 | 250 | -4 | 0 | 0 | 16 |
| 100 | 300 | 16 | 50 | 800 | 256 |
| 120 | 350 | 36 | 100 | 3600 | 1296 |
| **Sum** | | | | **8500** | **2920** |

**Step 3: Compute coefficients**
$$\hat{\beta}_1 = \frac{8500}{2920} \approx 2.91, \quad \hat{\beta}_0 = 250 - 2.91 \times 84 \approx 5.56$$

**Regression Equation:**
$$\hat{Y} = 5.56 + 2.91X$$

**Step 4: Predict**
* House of 90 $m^2$: $\hat{Y} = 5.56 + 2.91 \times 90 \approx \mathbf{267.46}$ (in thousands)

---

## 5. Evaluation Metrics: Measuring "Closeness"
Since we aren't predicting "Right/Wrong" labels, we measure how "close" our predicted numbers are to the actual numbers.

### **A. Mean Absolute Error (MAE)**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$
* Average magnitude of errors — same units as $Y$.
* Robust to outliers (no squaring).

### **B. Mean Squared Error (MSE)**
$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
* Penalises large errors heavily (squaring).
* Units are $Y^2$ (not interpretable directly).

### **C. Root Mean Squared Error (RMSE)**
$$RMSE = \sqrt{MSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$
* Most popular metric — same units as $Y$.
* Interpretable: "On average, predictions are off by $RMSE$ units."

### **D. Coefficient of Determination ($R^2$)**
$$R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

* $R^2 = 1$: Perfect prediction — model explains all variance.
* $R^2 = 0$: Model is no better than predicting the mean $\bar{y}$.
* $R^2 < 0$: Model is worse than the mean (possible with non-linear data and linear model).

### **E. Adjusted $R^2$**
Standard $R^2$ always increases when more features are added, even useless ones. **Adjusted $R^2$** penalises for unnecessary features:

$$\bar{R}^2 = 1 - \frac{(1-R^2)(n-1)}{n-p-1}$$

Where $p$ = number of predictors and $n$ = number of samples. Use this for **Multiple Regression** model comparison.

### **Metric Comparison Table**

| Metric | Formula | Units | Outlier Sensitive? | Best For |
|:---|:---|:---|:---|:---|
| MAE | $\frac{1}{n}\sum\|y_i-\hat{y}_i\|$ | Same as $Y$ | No | Robust evaluation |
| MSE | $\frac{1}{n}\sum(y_i-\hat{y}_i)^2$ | $Y^2$ | Yes | Penalising large errors |
| RMSE | $\sqrt{MSE}$ | Same as $Y$ | Yes | Most interpretable |
| $R^2$ | $1 - SSE/SST$ | Unitless (0–1) | Moderate | Goodness of fit |
| Adjusted $R^2$ | (see formula) | Unitless | Moderate | Comparing models with different features |

---

## 6. Challenges in Regression

### **A. Multicollinearity**
When your "independent" variables are actually dependent on each other (e.g., using both "Total Square Feet" and "Number of Rooms" to predict house price — they usually increase together).

**Detecting Multicollinearity — VIF (Variance Inflation Factor):**
$$VIF_j = \frac{1}{1 - R_j^2}$$

Where $R_j^2$ is the $R^2$ from regressing feature $j$ on all other features.

| VIF Value | Interpretation |
|:---|:---|
| VIF = 1 | No multicollinearity |
| 1 < VIF < 5 | Moderate — acceptable |
| VIF > 5 | High — problem |
| VIF > 10 | Severe — must address |

**Solutions:** Remove one of the correlated features, use Ridge/LASSO, or apply PCA.

### **B. Outliers**
A single extreme value (like a mansion in a middle-class neighbourhood) can "pull" the regression line away from the majority of data.

**Detection:** Standardised residuals $> 3$ or $< -3$ are likely outliers. Cook's Distance measures each point's influence on the regression line.

**Solutions:** Remove genuine outliers, use MAE instead of MSE (less outlier-sensitive), or apply **Robust Regression** (e.g., Huber loss).

### **C. Heteroscedasticity**
When the "noise" or error in our data isn't constant across all values of $X$ — errors grow or shrink as $X$ increases.

```
Homoscedastic (Good):        Heteroscedastic (Problem):
  Residuals                    Residuals
    · · ·                        ·     ·  ·  ·  ·
  · · · · ·          →       · ·  ·                ·  ·
    · · ·                  ·                               ·
  ─────────── X            ─────────────────────────────── X
  Constant spread          Spread grows with X (funnel shape)
```

**Detection:** Plot residuals vs fitted values; look for a fan shape.
**Solution:** Apply log-transformation to $Y$ (e.g., `log(price)`), or use Weighted Least Squares.

### **D. Overfitting in Regression**
High-degree polynomial models or too many features fit training data perfectly but fail on test data.

**Solutions:**
* Regularisation (Ridge, LASSO, Elastic Net).
* Cross-validation to select optimal complexity.
* Feature selection to remove irrelevant predictors.

---

## 7. Real-World Applications
1. **Sales Forecasting:** Predicting how many units of a product will sell next month based on past trends.
2. **Weather Prediction:** Estimating the exact degrees of temperature or centimeters of rainfall.
3. **Economic Trends:** Predicting the inflation rate or GDP growth for a country.
4. **Health Metrics:** Predicting a person's life expectancy based on lifestyle habits and genetics.
5. **Real Estate:** Estimating property prices based on location, size, and amenities.
6. **Energy Consumption:** Predicting electricity demand based on temperature, time of day, and season.
7. **Sports Analytics:** Predicting a player's performance score based on historical stats.
8. **Stock Price Prediction:** Forecasting next-day closing price based on technical indicators.

---

## 8. Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet, LogisticRegression
)
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 1. Simple / Multiple Linear Regression ---
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print(f"Intercept (β₀): {lr.intercept_:.4f}")
print(f"Coefficients:   {lr.coef_}")

mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)
print(f"MAE:  {mae:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")

# --- 2. Polynomial Regression ---
poly_pipeline = Pipeline([
    ('poly',  PolynomialFeatures(degree=3, include_bias=False)),
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
poly_pipeline.fit(X_train, y_train)
r2_poly = r2_score(y_test, poly_pipeline.predict(X_test))
print(f"Polynomial Regression R²: {r2_poly:.4f}")

# --- 3. Ridge Regression ---
ridge = Ridge(alpha=1.0)    # alpha = λ (regularisation strength)
ridge.fit(X_train, y_train)
print(f"Ridge R²: {r2_score(y_test, ridge.predict(X_test)):.4f}")

# --- 4. LASSO Regression ---
lasso = Lasso(alpha=0.1, max_iter=10000)
lasso.fit(X_train, y_train)
print(f"LASSO R²: {r2_score(y_test, lasso.predict(X_test)):.4f}")
print(f"Non-zero features: {np.sum(lasso.coef_ != 0)} / {len(lasso.coef_)}")

# --- 5. Elastic Net ---
enet = ElasticNet(alpha=0.1, l1_ratio=0.5)
enet.fit(X_train, y_train)
print(f"Elastic Net R²: {r2_score(y_test, enet.predict(X_test)):.4f}")

# --- 6. Cross-validation for model selection ---
models = {
    "Linear":     LinearRegression(),
    "Ridge":      Ridge(alpha=1.0),
    "LASSO":      Lasso(alpha=0.1),
    "ElasticNet": ElasticNet(alpha=0.1, l1_ratio=0.5)
}
print("\n--- Model Comparison (5-Fold CV, RMSE) ---")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_root_mean_squared_error')
    print(f"{name:12s}: RMSE = {-scores.mean():.4f} ± {scores.std():.4f}")

# --- 7. Residual Plot ---
residuals = y_test - y_pred
plt.figure(figsize=(8, 4))
plt.scatter(y_pred, residuals, alpha=0.5, color='steelblue')
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Fitted Values ($\\hat{Y}$)")
plt.ylabel("Residuals ($Y - \\hat{Y}$)")
plt.title("Residual Plot — Check for Heteroscedasticity")
plt.grid(True)
plt.tight_layout()
plt.savefig("residual_plot.png", dpi=150)
plt.show()
```

---

## 9. Summary Comparison: Classification vs. Prediction

| Feature | Classification | Prediction (Regression) |
| :--- | :--- | :--- |
| **Output Type** | Discrete / Categorical (e.g., Safe/Risky) | Continuous / Numeric (e.g., $50,000) |
| **Logic** | Finds boundaries to separate classes | Finds a line/curve to fit the trend |
| **Algorithms** | Decision Trees, Naive Bayes, SVM | Linear Regression, Polynomial, LASSO |
| **Key Metric** | Accuracy / F1-Score | RMSE / R-Squared |
| **Error Type** | Misclassification | Residual (distance from line) |
| **Evaluation** | Confusion Matrix, ROC | Residual Plot, Adjusted $R^2$ |

---

## 10. Quick Reference Card

| Concept | Formula | Purpose |
|:---|:---|:---|
| Simple Linear | $Y = \beta_0 + \beta_1 X + \epsilon$ | One-predictor model |
| Multiple Linear | $Y = \beta_0 + \sum \beta_i X_i + \epsilon$ | Multi-predictor model |
| OLS Slope | $\hat{\beta}_1 = S_{xy}/S_{xx}$ | Optimal slope |
| OLS Intercept | $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$ | Optimal intercept |
| Matrix OLS | $\hat{\beta} = (X^TX)^{-1}X^TY$ | Multi-variable exact solution |
| MAE | $\frac{1}{n}\sum\|y_i - \hat{y}_i\|$ | Robust error measure |
| RMSE | $\sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2}$ | Interpretable error |
| $R^2$ | $1 - SSE/SST$ | Goodness of fit (0–1) |
| Ridge | $SSE + \lambda\sum\beta_j^2$ | L2 regularisation |
| LASSO | $SSE + \lambda\sum\|\beta_j\|$ | L1 + feature selection |
| VIF | $1/(1-R_j^2)$ | Multicollinearity check |