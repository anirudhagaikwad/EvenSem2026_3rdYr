**Correlation Analysis**
Correlation analysis is a statistical technique for determining the strength of a link between two variables. It is used to detect patterns and trends in data and to forecast future occurrences.
➜ Consider a problem with different factors to be considered for making optimal conclusions
➜ Correlation explains how these variables are dependent on each other.
➜ Correlation quantifies how strong the relationship between two variables is. A higher value of the correlation coefficient implies a stronger association.
➜ The sign of the correlation coefficient indicates the direction of the relationship between variables. It can be either positive, negative, or zero.

## 1. What is Correlation Analysis?
Correlation analysis is a **statistical technique** used to measure the **strength** and **direction** of the relationship (association) between **two variables**.
➜ It helps identify **patterns** and **trends** in data.
➜ It supports **prediction** of future values based on observed relationships.
➜ Most real-world data variables are interrelated — correlation quantifies **how** and **how strongly** they depend on each other.
➜ The **correlation coefficient** (value between -1 and +1) shows:
  ➜ **Sign** → direction (positive or negative)
  ➜ **Magnitude** → strength of the relationship
  
> A higher absolute value of the correlation coefficient indicates a stronger association between the variables.

## 2. Types of Correlation (Direction)
![Types of Correlation](../imgs/TypesCorrelation.png)
There are three main types based on direction:
➤ 1.**Positive Correlation**  
  Both variables move in the **same direction**.  
  As one increases, the other also increases.  
  **Example:** Height and weight — taller people tend to weigh more.

➤ 2.**Negative Correlation**  
  Variables move in **opposite directions**.  
  As one increases, the other decreases.  
  **Example:** Price and demand — as price rises, demand usually falls.

➤ 3.**Zero Correlation** (No Correlation)  
  No apparent relationship — change in one variable does **not** affect the other.  
  **Example:** Shoe size and intelligence level.

## 3. Types of Correlation Coefficients
Different coefficients are used depending on data type, distribution, and relationship nature:

| Coefficient                        | Type of Relation | Levels of Measurement              | Assumed Data Distribution   | Best For                          |
|------------------------------------|------------------|------------------------------------|-----------------------------|-----------------------------------|
| **Pearson**                        | Linear           | Interval / Ratio                   | Normal                      | Continuous numeric data           |
| **Spearman Rank**                  | Monotonic (non-linear OK) | Ordinal                      | Any                         | Ranked / non-normal data          |
| **Kendall Tau**                    | Monotonic        | Ordinal                            | Any                         | Small samples, ordinal data       |
| **Phi Coefficient**                | –                | Nominal (dichotomous)              | Any                         | Binary vs binary variables        |
| **Cramer’s V**                     | –                | Nominal (two variables)            | Any                         | Categorical variables             |

**Most common:** **Pearson correlation coefficient** (denoted as **r**)

## 4. Pearson Correlation Coefficient – Formula & Interpretation

The Pearson correlation coefficient is the most often used metric of correlation. It expresses the linear relationship between two variables in numerical terms. The Pearson correlation coefficient, written as "r," is as follows:

**Formula:**
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}

    r: Correlation coefficient 
    xixi​ : i^th value first dataset X
    xˉxˉ : Mean of first dataset X
    yiyi​ : i^th value second dataset Y
    yˉyˉ​ : Mean of second dataset Y

Where:
- r = Pearson correlation coefficient
- x_i, y_i  = individual data points
- \bar{x}, \bar{y} = means of the two variables

More precisely:
> r = how much X and Y move together / how much X moves on its own X how much Y moves on its own

Top part (numerator) → Measures if X and Y change in the same direction or opposite directions (and how strongly).
Bottom part (denominator) → Just normalizes/scales the value so it always stays between -1 and +1.

## Step-by-step :
➜ 1. Take each pair of values (xᵢ and yᵢ)
You have two lists:
Example:
X: [10, 20, 30, 40]
Y: [15, 25, 35, 50]
➜ 2. Find the average (mean) of each list
\bar{x} = average of X
\bar{y} = average of Y
➜ 3. For every pair, calculate how far each value is from its own average
(xᵢ - \bar{x}) → how much this X value is above/below average X
(yᵢ - \bar{y}) → same for Y
➜ 4. Multiply those deviations together
(xᵢ - \bar{x}) × (yᵢ - \bar{y})
→ If both are above average or both below → positive number (they move together)
→ If one above and one below → negative number (they move opposite)
➜ 5. Add up all those products → this is the top part (numerator)
Big positive sum = strong positive relationship
Big negative sum = strong negative relationship
Close to zero = little or no linear relationship
➜ 6. Bottom part → square the deviations, add them up, and take square root
This is basically the "spread" or "variability" of X and of Y (like standard deviation without the division by n).
➜ 7. Divide top by bottom → you get r between -1 and +1

The correlation coefficient, denoted by "r", ranges between -1 and 1.
    r = -1 indicates a perfect negative correlation.
    r = 0 indicates no linear correlation between the variables.
    r = 1 indicates a perfect positive correlation.


**Strength Interpretation Table:**

| Strength   | Correlation Coefficient Range | Description                  |
|------------|-------------------------------|------------------------------|
| Perfect    | 0.80 – 1.00                   | Very strong relationship     |
| Strong     | 0.50 – 0.79                   | Notable relationship         |
| Moderate   | 0.30 – 0.49                   | Fair relationship            |
| Weak       | 0.00 – 0.29                   | Little to no relationship    |

**Rule of thumb:** |r| > 0.7 is generally considered **strong**.

## 5. Steps to Perform Correlation Analysis
1. **Identify the variables**  
   Choose **two quantitative** variables (must be numeric).

2. **Collect the data**  
   From surveys, experiments, databases, etc.

3. **Select the appropriate correlation coefficient**  
   Usually Pearson for linear + continuous data; Spearman if ordinal or non-normal.

4. **Calculate the coefficient**  
   Use formula, Excel, Python (pandas/numpy), R, etc.

5. **Interpret the result**  
   Assess **direction** (sign) and **strength** (magnitude).  
   Remember: Correlation ≠ Causation!

## 6. Practical Examples in Python

### Using NumPy

```python
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 3, 9, 1])

# Correlation matrix
corr = np.corrcoef(x, y)
print("Correlation Coefficient:\n", corr)
```

**Output:**
```
Correlation Coefficient:
 [[ 1.  -0.3]
  [-0.3  1. ]]
```

→ r = -0.3 (weak negative correlation)

### Using Pandas

```python
import pandas as pd

data = pd.DataFrame({'X': [1, 2, 3, 4, 5],
                     'Y': [5, 7, 3, 9, 1]})

corr_value = data['X'].corr(data['Y'])
print("Correlation Coefficient:", corr_value)
```

**Output:**
```
Correlation Coefficient: -0.3
```

## 7. Advantages of Correlation Analysis

- Simple and easy to calculate/interpret
- Reveals relationships between variables quickly
- Useful in **feature selection** for machine learning
- Supports decision-making in business, healthcare, marketing, etc.
- Helps understand patterns and dependencies in data

## 8. Limitations / Disadvantages

- **Correlation ≠ Causation** — strong correlation does not mean one causes the other
- Sensitive to **outliers** — extreme values can distort results
- Only measures **linear** relationships well (Pearson); misses non-linear patterns
- Best for **bivariate** analysis — multivariate relationships are harder to interpret
- Cannot handle complex or hidden relationships accurately

## 9. Real-World Applications

- **Economics & Finance** — supply vs demand, stock prices vs interest rates
- **Business Analytics** — sales vs advertising spend
- **Market Research** — customer behavior vs marketing campaigns
- **Medical/Healthcare** — symptoms vs diseases, lifestyle factors vs health outcomes
- **Weather Forecasting** — temperature vs humidity/pressure
- **Environmental Studies** — pollution levels vs health indicators
- **Customer Service** — satisfaction scores vs response time
