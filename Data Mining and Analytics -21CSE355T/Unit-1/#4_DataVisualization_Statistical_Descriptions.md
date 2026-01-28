# Unit-1: Data Mining Introduction 
**Topic: Data Visualization & Basic Statistical Descriptions**  
 
**Course: 21CSE355T - Data Mining and Analytics**  
**Reference:** Jiawei Han, Micheline Kamber, Jian Pei – "Data Mining: Concepts and Techniques", 3rd Edition, Chapter 2 (Section 2.3 Data Visualization & Basic Statistical Descriptions)  
**Objective:** Students will learn why **visualization** is essential in data understanding/preprocessing, explore key **visualization techniques** (with interpretation tips), and master **basic statistical descriptions** (central tendency, dispersion, shape measures like skewness & kurtosis) for effective data mining preparation.

## 1. Why Data Visualization & Statistical Descriptions?

**Goal of this topic:**  
Quickly understand data distribution, patterns, outliers, correlations, and anomalies before mining.  
- "A picture is worth a thousand data points" – Visuals help spot issues fast.  
- Statistical summaries provide numerical backbone (quantify what visuals show).  

**Importance in Data Mining:**  
- Detect skewness/outliers → affects normalization, algorithm choice.  
- Identify correlations → helps in attribute selection/reduction.  
- Find data quality issues → missing values, noise.  
- Exploratory Data Analysis (EDA) foundation → 70–80% of data mining effort!

**Exam Tip:** Questions often ask: "Explain any 3 visualization techniques with examples" or "Discuss measures of central tendency & dispersion".

## 2. Data Visualization Techniques
Data visualization helps turn raw data into valuable insights. Since data plays a significant role in decision-making today, making sense of large amounts of information is essential. Good visualizations turn complex data into clear and simple graphics, making identifying trends, patterns, and outliers easier.  

Without visualization, data can be overwhelming and challenging to understand. A comprehensive guide to data visualization helps transform complex information into clear insights. Charts, graphs, and dashboards present data in an easy-to-understand format, leading to faster and better decisions.

Data visualization aims to communicate data clearly and effectively through graphical representation. Data visualization has been used extensively in many applications. For example, we can use data visualization at work for reporting, managing business operations,and tracking progress of tasks. More popularly, we may take advantage of visualization techniques to discover data relationships that are otherwise not easily observable by looking at the raw data. Nowadays, people also use data visualization to create fun and interesting graphics.

Key Principles for Effective Visualization:
->**Know Your Audience**: Tailor complexity to their knowledge level.
->**Define Your Goal**: Understand if you're informing, persuading, or exploring data.
->**Keep it Simple**: Prioritize clarity and avoid clutter.
-> Choose the Right Chart: Select visuals that best represent your data and goal.
->**Use Color & Context Wisely**: Employ color to highlight, not decorate, and add context.
->**Ensure Accuracy**: Use high-quality data and avoid misleading visuals

Common Techniques by Data Type/Goal:
->**Comparison**: Bar charts (categories), Line charts (trends over time), Box Plots (distribution comparison).
->**Distribution**: Histograms (frequency of numerical data), Box Plots, Density Plots.
->**Composition**: Pie/Donut charts (parts of a whole), Treemaps (hierarchical data), Stacked Area/Bar charts, Waterfall charts.
->**Relationship**: Scatter plots (two variables), Bubble charts (three variables), Heatmaps, Network diagrams, Correlation matrices.
->**Geospatial**: Choropleth maps (color-coded regions), Dot Maps, Flow Maps, Bubble Maps. 

**Key Techniques:**  

### 2.1 Histograms 
Histograms are powerful data visualization tools that display the distribution of continuous numerical data by grouping values into "bins" (intervals) and showing the frequency (count) of data points in each bin with adjacent bars, revealing patterns like shape (skewness, normality), spread, central tendency, and outliers, unlike bar charts that use discrete categories. They help understand "how many" values fall into specific ranges, making them essential for Exploratory Data Analysis (EDA) to grasp data characteristics quickly. 
Key Components & How They Work
->X-Axis (Horizontal): Represents the continuous numerical variable, divided into equally spaced intervals (bins).
->Y-Axis (Vertical): Shows the frequency (count) or relative frequency of data points falling into each bin.
->Bars: Rectangular bars touch each other, signifying continuous data ranges. Their height corresponds to the count in that bin.  

When to Use Them
->Analyzing Single Variables: Best for understanding the shape and spread of one continuous variable (e.g., ages, heights, temperatures).
->Process Control: Used in quality control to assess process consistency.
->Initial Data Exploration: A fundamental first step in data science to understand a dataset

**How to interpret:**  
- Tall bars = high frequency  
- Skewed right → long right tail (positive skew)  
- Skewed left → long left tail (negative skew)  
- Bimodal → two peaks (e.g., two customer groups)

#### Steps to Draw a Histogram
**Step 1 Collect and Organize the Data**: Collect the data you wish to display in the histogram. This might range from test results to population distribution. 
    For example: Assume you get the following test scores: 14, 20, 12, 26, 8, 7, 2, 28, 30, 16, 18, 23. 
    First arrange it in ascending order. 
    Exam results: 2, 7, 8, 12, 14, 16, 18, 19, 23, 26, 28 and 30. 

**Step 2 Decide Number of Bins (Intervals)**: Determine the number of intervals, or "bins," you wish to split your data into. This is determined by the scope and distribution of your data, as well as the amount of information you choose to display. Assume we wish to divide the scores into 5 bins. 

**Step 3 Determine Bin Limits**: Determine the limits of each bin. These bounds should encompass the complete range of your data and be regularly spaced. 
[0-5 - 10 - 15 - 20 - 25 - 30].

**Step 4: Count the number of data points that belong in each bin.**
**Total frequency = 12** ✓

| Class Interval | Frequency | Data Points                          |
|----------------|-----------|--------------------------------------|
| 0 – 5          | 1         | 2                                    |
| 5 – 10         | 2         | 7, 8                                 |
| 10 – 15        | 2         | 12, 14                               |
| 15 – 20        | 3         | 16, 18, 19                           |
| 20 – 25        | 1         | 23                                   |
| 25 – 30        | 3         | 26, 28, 30                           |

**Step 5: Visualize – Histogram Description**
In a histogram you would:
- Put **Class Intervals** on the x-axis
- Put **Frequency** (count) on the y-axis
- Draw adjacent bars (no gaps) with height = frequency

![Histogram](../imgs/Histrogram.png)

---
### 2.2 Box Plots (Box-and-Whisker Plots)  
Box plots (or box-and-whisker plots) are powerful data visualization techniques that display a dataset's distribution, highlighting its five-number summary: minimum, first quartile (Q1), median (Q2), third quartile (Q3), and maximum, along with potential outliers. They excel at comparing data spread across different groups, revealing skewness, variability, and anomalies in a compact visual format, making them ideal for Exploratory Data Analysis (EDA). 

A box plot summarizes a dataset using five key values:
- Minimum (excluding outliers)
- First Quartile (Q1) – 25th percentile
- Median (Q2) – 50th percentile
- Third Quartile (Q3) – 75th percentile
- Maximum (excluding outliers)

It also helps identify **outliers** and shows the spread and shape of the data.

**Key Components & Interpretation**
->The Box: Represents the Interquartile Range (IQR), the middle 50% of the data, from Q1 to Q3.
->Median Line: A line inside the box showing the 50th percentile (Q2).
->Whiskers: Lines extending from the box to the minimum and maximum data points within 1.5 * IQR from the box edges.
->Outliers: Individual points (dots) plotted beyond the whiskers, indicating extreme values. 

**What Box Plots Reveal**
->Central Tendency: The median line shows the center of the data.
->Spread/Variability: The box's length (IQR) shows data concentration; longer boxes mean more spread.
->Skewness: If the median isn't centered in the box, or whiskers are unequal, data is skewed.
->Outliers: Dots outside whiskers flag unusual data points

# How to Create a Box Plot (Box-and-Whisker Plot) – Step-by-Step Guide

**Q1** and **Q2** are very important terms used in statistics, especially when describing data in box plots, quartiles, or summary statistics.

### Quick and Simple Explanation

| Term   | Full Name              | What it means                              | Position in ordered data          | Also called              |
|--------|------------------------|--------------------------------------------|-----------------------------------|--------------------------|
| **Q1** | First Quartile         | The value below which **25%** of the data lies | 25th percentile                   | Lower quartile           |
| **Q2** | Second Quartile        | The value below which **50%** of the data lies (the middle value) | 50th percentile                   | **Median**               |
| Q3     | Third Quartile         | The value below which **75%** of the data lies | 75th percentile                   | Upper quartile           |

### Very Easy Way to Remember

Think of your data sorted from smallest to biggest:

- **Q1** → cuts off the **bottom 25%** (first quarter)
- **Q2** → cuts the data **exactly in half** → this is the **median**
- **Q3** → cuts off the **top 25%** (last quarter)

### Real-life Example  
Test scores (sorted):  
**4, 12, 15, 18, 22, 25, 29, 33, 38, 42, 47, 55**  
(12 students)

1. **Q2 (Median)**  
   Middle of 12 numbers = average of 6th and 7th  
   → (25 + 29) ÷ 2 = **27**

2. **Q1**  
   Lower half: 4, 12, 15, 18, 22, 25  
   Median of these 6 = average of 3rd & 4th  
   → (15 + 18) ÷ 2 = **16.5**

So in this case:  
- **Q1 = 16.5** → 25% of students scored 16.5 or less  
- **Q2 = 27** → 50% of students scored 27 or less (half did better, half did worse)

---
#### Box Plot Example
Here is a complete step-by-step guide to create a **Box Plot** (Box-and-Whisker Plot) using the given cricket team's runs scored in 12 matches:

**Data:**  
100, 120, 110, 150, 110, 140, 130, 170, 120, 220, 140, 110

### Step 1: Arrange the data in ascending order
```
100, 110, 110, 110, 120, 120, 130, 140, 140, 150, 170, 220
```

### Step 2: Find the Median (Q2)
Number of observations (n) = 12 (even number)  
Median = average of 6th and 7th values  
6th value = 120  
7th value = 130  
**Median (Q2) = (120 + 130) / 2 = 125**

### Step 3: Find Q1 (First Quartile)
Lower half = first 6 values:  
100, 110, 110, 110, 120, 120  
Median of these 6 values = average of 3rd & 4th  
3rd = 110, 4th = 110  
**Q1 = (110 + 110) / 2 = 110**

### Step 4: Find Q3 (Third Quartile)
Upper half = last 6 values:  
130, 140, 140, 150, 170, 220  
Median of these 6 values = average of 3rd & 4th  
3rd = 140, 4th = 150  
**Q3 = (140 + 150) / 2 = 145**

### Step 5: Calculate Interquartile Range (IQR)
```
IQR = Q3 − Q1 = 145 − 110 = 35
```

### Step 6: Determine outlier boundaries (fences)
Using the standard 1.5 × IQR rule:

```
Lower fence = Q1 − 1.5 × IQR  
            = 110 − (1.5 × 35)  
            = 110 − 52.5  
            = 57.5

Upper fence = Q3 + 1.5 × IQR  
            = 145 + 52.5  
            = 197.5
```

→ Any value **below 57.5** or **above 197.5** is an outlier

### Step 7: Check for outliers
Our values: 100, 110, 110, 110, 120, 120, 130, 140, 140, 150, 170, **220**

- 220 > 197.5 → **220 is an outlier**

### Step 8: Determine the whiskers
- **Lower whisker**: Smallest value that is ≥ lower fence → **100**  
- **Upper whisker**: Largest value that is ≤ upper fence (excluding outliers) → **170**

### Final Five-Number Summary + Outlier

| Component              | Value  |
|------------------------|--------|
| Minimum (lower whisker)| 100    |
| Q1                     | 110    |
| Median (Q2)            | 125    |
| Q3                     | 145    |
| Maximum (upper whisker)| 170    |
| Outlier(s)             | 220    |
| IQR                    | 35     |

### Box Plot Structure (Text Representation)

```
                •               ← Outlier (220)
          ┌──────────────┐      
          │              │      
   ───────┼───────125────┼──────
Lower     │     Q1       │  Q3          Upper
whisker   └──────────────┘              whisker
  100                 110      145      170
```
![Histogram](../imgs/BoxPlot.png)

**Summary Interpretation:**
- Most of the team's scores (middle 50%) were between **110 and 145** runs
- Typical (median) performance ≈ **125** runs
- There is one unusually high score of **220** runs (outlier)
- The team shows moderate spread in performance with one exceptional high-scoring match

---
**Example 2**
Test scores (out of 50):  
**3, 12, 15, 18, 22, 25, 28, 31, 34, 37, 41, 48**  
(12 scores – we'll add one outlier later to demonstrate)

**Step 1: Sort the data in ascending order**
```
3, 12, 15, 18, 22, 25, 28, 31, 34, 37, 41, 48
```
**Step 2: Find the Median (Q2)**
Number of values (n) = 12 (even)  
Median = average of 6th and 7th values  
6th = 25  
7th = 28  
**Median (Q2) = (25 + 28) / 2 = 26.5**

### Step 3: Find Q1 (First Quartile – lower half)
Lower half (first 6 values):  
3, 12, 15, 18, 22, 25  
Median of these 6 values = average of 3rd and 4th  
3rd = 15, 4th = 18  
**Q1 = (15 + 18) / 2 = 16.5**

### Step 4: Find Q3 (Third Quartile – upper half)
Upper half (last 6 values):  
28, 31, 34, 37, 41, 48  
Median of these 6 values = average of 3rd and 4th  
3rd = 34, 4th = 37  
**Q3 = (34 + 37) / 2 = 35.5**

### Step 5: Calculate the Interquartile Range (IQR)
```
IQR = Q3 − Q1 = 35.5 − 16.5 = 19
```

### Step 6: Determine the outlier fences
```
Lower fence = Q1 − 1.5 × IQR = 16.5 − (1.5 × 19) = 16.5 − 28.5 = -12  
Upper fence = Q3 + 1.5 × IQR = 35.5 + 28.5 = 64
```

→ Any value **below -12** or **above 64** is considered an outlier  
(In our data: no outliers)

### Step 7: Determine the whiskers
- **Lower whisker**: Smallest value that is **≥ lower fence** → **3**  
- **Upper whisker**: Largest value that is **≤ upper fence** → **48**

### Step 8: Summary of the Five-Number Summary + Outliers

| Component          | Value  |
|--------------------|--------|
| Minimum (whisker)  | 3      |
| Q1                 | 16.5   |
| Median             | 26.5   |
| Q3                 | 35.5   |
| Maximum (whisker)  | 48     |
| IQR                | 19     |
| Outliers           | None   |

### Bonus Example with Outlier
Add one more score: **72**  
New data → 3, 12, 15, 18, 22, 25, 28, 31, 34, 37, 41, 48, **72** (n=13)

- New median = 7th value = **28**  
- New Q1 = median of first 6 = **16.5** (same)  
- New Q3 = median of last 7 → average of 4th = **37**  
- New IQR = 37 − 16.5 = **20.5**  
- Upper fence = 37 + 1.5×20.5 = 37 + 30.75 = **67.75**  
→ **72** is now an **outlier** (shown as a dot beyond the upper whisker)

## Final Box Plot Structure (Text Representation)


          ┌──────────────┐           • (outlier if present)
          │              │
   ───────┼───────Median─┼───────
Lower     │     Q1       │  Q3          Upper
whisker   └──────────────┘              whisker
   3                  26.5             48     (72)
    
**Example 3:**  
Compare salary distribution across departments → Box plot shows HR has lower median but more outliers (high executives).

**Real-world:** Excellent for spotting outliers in fraud detection or sensor data.

---


### 2.3 Quantile Plots (Quantile-Quantile or Q-Q Plots)  
Quantile plots, especially Quantile-Quantile (Q-Q) plots, are powerful data visualization tools used to check if a dataset follows a specific theoretical distribution (like normal) or if two datasets come from the same distribution by plotting their quantiles against each other; if they match, points form a straight line, revealing patterns like skewness, heavy tails, or outliers, which helps validate statistical assumptions and guide model selection. 

**How Quantile Plots Work**
->Quantiles: These are values that divide a dataset into equal-sized groups (e.g., quartiles split into four, percentiles into 100).
->Plotting: A Q-Q plot plots the quantiles of your sample data against the corresponding quantiles of a reference distribution (e.g., standard normal) or another dataset.
->Reference Line: A straight 45-degree line (or diagonal line) is added; if data points fall roughly along this line, they match the reference distribution

**Key Uses in Data Visualization & Analysis**
->Normality Testing: Visually assess if residuals or data are normally distributed, a common assumption for many tests.
->Distribution Comparison: See if two samples share the same underlying distribution by plotting one's quantiles against the other's.
->Detecting Deviations:
        ->Skewness: Points curving away from the line (e.g., upward curve for right-skew).
        ->Heavy/Light Tails: Points rising faster or slower than the line at the ends.
        ->Outliers: Points far away from the main cluster.
->Model Selection: Helps choose appropriate models by identifying data distribution shapes. 

**Advantages**
->Provides visual confirmation of distributional assumptions, crucial for statistical validity.
->Reveals subtle distributional differences (skew, tails) that histograms might miss.
->Robust to different sample sizes and effective for spotting outliers

#### Purpose of a Q-Q Plot
If the points lie approximately along a **straight diagonal line**, your data follows the theoretical distribution quite well.  
Deviations from the straight line show where and how the distribution differs.

#### Step-by-Step: How to Create a Q-Q Plot Manually  
(Example: Checking if data is normally distributed)

**Sample Data** (10 observations – exam marks):  
65, 72, 78, 81, 84, 88, 92, 95, 98, 105

**Step 1: Sort the data in ascending order**
```
65, 72, 78, 81, 84, 88, 92, 95, 98, 105
```

**Step 2: Calculate the ranks / positions**
Number of observations **n = 10**

For each ordered value, calculate its **theoretical quantile** (expected position under normal distribution).

Common formula for plotting position (most popular & simple version):  
**pᵢ = (i - 0.5) / n**  
where i = rank (1 to n)

So:

| i  | Data (sorted) | pᵢ = (i-0.5)/10 | Theoretical z-score (from standard normal table or calculator) |
|----|---------------|------------------|-----------------------------------------------------------------|
| 1  | 65            | 0.05             | -1.645                                                          |
| 2  | 72            | 0.15             | -1.036                                                          |
| 3  | 78            | 0.25             | -0.674                                                          |
| 4  | 81            | 0.35             | -0.385                                                          |
| 5  | 84            | 0.45             | -0.126                                                          |
| 6  | 88            | 0.55             |  0.126                                                          |
| 7  | 92            | 0.65             |  0.385                                                          |
| 8  | 95            | 0.75             |  0.674                                                          |
| 9  | 98            | 0.85             |  1.036                                                          |
| 10 | 105           | 0.95             |  1.645                                                          |

**Step 3: Plot the points**
- **X-axis** → Theoretical quantiles (z-scores from standard normal distribution)  
- **Y-axis** → Your actual (sorted) data values

So points are:

```
(-1.645, 65)
(-1.036, 72)
(-0.674, 78)
(-0.385, 81)
(-0.126, 84)
( 0.126, 88)
( 0.385, 92)
( 0.674, 95)
( 1.036, 98)
( 1.645, 105)
```

Here are some real examples of what Q-Q plots look like (with labels):

![Q-Q Plot](../imgs/normal_probability_plot_C3.webp)

![Q-Q Plot](../imgs/NORMALDISTRIBUTION-660x362.png)

**Step 4: Add a reference line (optional but very helpful)**
Usually a straight line is added from the 25th to 75th percentile (or simply y = x after scaling).

Many software packages draw the line that passes through the points or uses the theoretical line.

**Step 5: Interpret the plot**

Here are classic patterns you will see:

**Good normal distribution** → points follow straight diagonal line quite closely
![QPlot](../imgs/NORMALDISTRIBUTION-660x362.png)

**Heavy tails / outliers** → points curve upward at both ends (like an "S" rotated)

**Light tails** → points curve downward at ends

**Right-skewed** → points start low-left, then bend upward on the right

**Left-skewed** → opposite pattern

Here are visual examples of different patterns:

![QPlot](../imgs/Q-Q_Plot_Normal.png)

### Quick Modern Way (Recommended in Practice)

Most people today **don't calculate manually** — use software:

- **Excel**: Sort data → calculate NORM.S.INV((rank-0.5)/n) → scatter plot
- **Python**: `scipy.stats.probplot(data, dist="norm", plot=plt)`
- **R**: `qqnorm(data); qqline(data)`
- **Jamovi / SPSS / Minitab**: Built-in Q-Q plot option

---
**Example:**  
Q-Q plot of student marks → Points along diagonal → data is approximately normal → good for parametric tests later.

**Real-world:** Used in preprocessing to decide transformations (log, square root) for normality.

### 2.4 Scatter Plots  
Scatter plots are a key data visualization technique using dots to show relationships between two numerical variables, revealing patterns like correlation (positive, negative, none), trends, clusters, and outliers, by plotting one variable on the x-axis and the other on the y-axis, with variations like bubble charts adding a third dimension via dot size. They're ideal for exploring feature relationships, validating models, and spotting anomalies in data sets. 

**Key Aspects of Scatter Plots**
->Purpose: To visualize correlations, trends, clusters, and outliers between two quantitative variables.
->Axes: Typically, the independent variable is on the x-axis (horizontal) and the dependent variable on the y-axis (vertical).
->Data Points: Each dot represents an individual data point or observation

**What They Reveal**
->Correlation: Strength and direction (positive/negative) of the relationship.
->Trends: Linear, parabolic, or other patterns in the data.
->Clusters: Groups of data points, suggesting segments.
->Outliers: Unusual points that deviate from the main pattern. 

**Common Uses**
->Business: Analyzing marketing spend vs. revenue, customer segmentation.
->Finance: Risk analysis.
->Education/L&D: Study hours vs. test scores, training effectiveness. 

**Variations & Enhancements**
->Bubble Charts: Add a third variable by varying the size of the dots (bubbles).
->Color & Labels: Use different colors or labels to distinguish categories or additional dimensions.
->Trend Lines: Add regression lines to summarize the overall relationship

**Definition:** Plot two numeric attributes — one on x-axis, one on y-axis (dots).  
**Purpose:** Show relationship (positive/negative correlation), clusters, outliers, trends.

**Example and Steps How to create Scatter Plot**
Here are the clear **step-by-step instructions** to draw a **Scatter Plot** showing the relationship between:

- **X-axis**: Number of T20 World Cup matches played  
- **Y-axis**: Total wickets taken  

We will use real career statistics of top **Indian bowlers** in the **ICC Men's T20 World Cup** (historical data up to 2024 edition, as of early 2026).

### Example Data (Top Indian Bowlers – T20 World Cup Career Stats)
Approximate figures based on reliable sources (ESPNcricinfo, ICC records):

| Bowler              | Matches Played | Wickets Taken |
|---------------------|----------------|---------------|
| Ravichandran Ashwin | 24             | 32            |
| Arshdeep Singh      | 14–15          | 27            |
| Jasprit Bumrah      | ~20–22         | 30+ (approx)  |
| Yuzvendra Chahal    | 18–20          | ~25–28        |
| Hardik Pandya       | 25+            | ~20–25        |
| Bhuvneshwar Kumar   | 15–18          | ~18–20        |
| Axar Patel          | 10–12          | ~15           |
| Mohammed Shami      | 8–10           | ~12–15        |

**Note**: Arshdeep Singh has shown excellent efficiency (high wickets in fewer matches), while Ashwin leads in total wickets due to more matches played.

### Step-by-Step: How to Draw the Scatter Plot

**Step 1: Prepare your data**  
Create two lists/columns:  
- Matches played (X values)  
- Wickets taken (Y values)

**Step 2: Choose your tools**  
Options:  
- Manual: Graph paper + pencil  
- Software: Excel/Google Sheets (Insert → Chart → Scatter)  
- Programming: Python (matplotlib) – best for precision  
- Other: Tableau, R, etc.

**Step 3: Set up the axes**  
- **X-axis**: Matches Played (suggested range: 0 to 30)  
- **Y-axis**: Wickets Taken (suggested range: 0 to 40)  
- Title: "Indian Bowlers in T20 World Cup: Matches Played vs Wickets Taken"  
- Label axes:  
  - X: "Matches Played"  
  - Y: "Wickets Taken"

**Step 4: Plot each point**  
Place a dot for each bowler at coordinates (Matches, Wickets)  
Examples:  
- Ashwin: (24, 32)  
- Arshdeep: (15, 27)  
- Bumrah: (22, 30)  
- etc.

**Step 5: Add enhancements (highly recommended)**  
- Use different colors/markers for spinners vs pacers  
- Add data labels (bowler names) next to points  
- Include a trend line (linear regression) → shows positive correlation (more matches generally = more wickets)  
- Highlight efficient bowlers (points above the trend line)

**Step 6: Interpret the scatter plot**  
- Positive trend: Bowlers with more matches tend to have more wickets (expected)  
- Efficiency outliers: Arshdeep Singh appears high up with relatively fewer matches → very effective in recent editions (especially 2024)  
- Veterans like Ashwin show accumulation over multiple tournaments  
- Younger/fast bowlers (Bumrah, Arshdeep) show high potential

![Scatter Plot](../imgs/ScatterPlot.png)

**Example:**  
Height vs Weight → Upward trend → positive correlation.  
Add color/size for third variable (e.g., age).

**Real-world:** Detect correlation before attribute reduction.
---
**Other Common Visuals:**  
## Pie charts 
visualize parts of a whole as proportional slices in a circle, excellent for showing simple composition with few categories (ideally under 5-6) and clearly labeled percentages, but avoid 3D effects and too many slices for clarity, focusing on comparing categories to the total, not each other directly. Best practices include using flat, contrasting colors, sorting slices largest to smallest (starting at the top), and combining small segments into an "Other" category to maintain readability. 

**How Pie Charts Work**
->Circular Representation: A whole dataset is a full circle (100% or 360°).
->Slices: Each category gets a slice (sector) whose area, arc length, and angle are proportional to its value.
->Proportions: Slices show how much each part contributes to the total

**When to Use Them**
->Part-to-Whole: To show composition (e.g., market share, budget breakdown).
->Few Categories: Best with 2 to 5 categories for easy comparison.
->Simple Comparisons: Quick visual of a category's share of the total. 

**Best Practices for Effective Pie Charts**
->Limit Slices: Keep categories minimal (5 max); use an "Other" slice for small groups.
->Label Clearly: Add percentages or values directly on slices or use a clear legend.
->Sort Slices: Arrange from largest to smallest (clockwise from the top) for intuitive understanding.
->Use Color Wisely: Distinct, contrasting colors for each slice.
->Keep it Flat: Avoid 3D, gradients, or explosions, as they distort perception.
->Avoid Multiple Pies: Don't compare proportions across multiple pie charts; use bar charts instead

#### How to Create a Pie Chart – Manual Steps (with Example)

**Example Data**: Distribution of India's wickets in the 2024 T20 World Cup by bowler type (approximate real data)  

| Bowler Type     | Wickets Taken | Percentage of Total |
|-----------------|---------------|---------------------|
| Fast Bowlers    | 42            | 58%                 |
| Spinners        | 28            | 39%                 |
| All-rounders    | 2             | 3%                  |
| **Total**       | **72**        | **100%**            |

#### Step-by-Step Manual Process

1. **Calculate the total**  
   Add up all wickets: 42 + 28 + 2 = 72

2. **Find the percentage for each category** (if not already given)  
   Percentage = (Part ÷ Total) × 100  
   - Fast: (42 ÷ 72) × 100 ≈ 58%  
   - Spinners: (28 ÷ 72) × 100 ≈ 39%  
   - All-rounders: (2 ÷ 72) × 100 ≈ 3%

3. **Convert percentages to angles for the pie**  
   Full circle = 360°  
   Angle for each slice = (Percentage ÷ 100) × 360°  
   - Fast Bowlers: 58% → 0.58 × 360 = **209°**  
   - Spinners: 39% → 0.39 × 360 = **140°**  
   - All-rounders: 3% → 0.03 × 360 = **11°**

4. **Draw a circle**  
   Use a compass or trace a round object to draw a perfect circle on paper.

5. **Draw the slices**  
   - Start from the right horizontal line (0° position).  
   - Use a protractor:  
     – First slice (Fast Bowlers): Measure 209° clockwise or anticlockwise and mark.  
     – Draw a straight line from centre to this mark.  
     – Next slice (Spinners): From the end of the first slice, measure another 140°.  
     – Last slice (All-rounders): Remaining 11°.  

6. **Label and colour each slice**  
   - Shade or colour each section differently.  
   - Write the category name and percentage (or wickets) inside or outside the slice.  
   - Add a title: “India’s Wickets in T20 World Cup 2024 by Bowler Type”

7. **Optional: Add a legend/key**  
   Draw small coloured boxes with labels if space inside the pie is limited.

![PI Chart](../imgs/PIChartResult.png)
---

## Bar Chart
A bar chart (or bar graph) is a visual tool that represents data using rectangular bars of varying lengths or heights. It is primarily used to compare discrete categories or groups, where each bar's length is proportional to the value it represents.

**Types of Bar Charts and Techniques**
The choice of bar chart type depends on the data and the message you want to convey: 
->Vertical Bar Chart (Column Chart): The standard format, best for comparing a few categories or showing trends over a period of time when category labels are short.
->Horizontal Bar Chart: Ideal when you have many categories or long category labels that would overlap in a vertical chart. It makes the labels easier to read.
->Grouped (or Clustered) Bar Chart: Used to compare multiple sub-categories within each main category (e.g., sales of different product types across various regions). Different colors or shades differentiate the sub-groups.
->Stacked Bar Chart: Displays how different sub-groups contribute to a total, by stacking bars representing each sub-group on top of each other. The total height of the bar shows the combined result.
->100% Stacked Bar Chart (Percentage Bar Chart): A variation of the stacked bar chart where all bars are the same total height (100%), allowing for a focus on the proportions each sub-group contributes to the whole, rather than the absolute 

#### How to Create a Bar Chart – Manual Steps (with Example)

**Example Data**: Top 5 Indian Bowlers – T20 World Cup Wickets (Career approximate)

| Bowler            | Wickets |
|-------------------|---------|
| R Ashwin          | 32      |
| Jasprit Bumrah    | 30      |
| Arshdeep Singh    | 27      |
| Y Chahal          | 26      |
| Hardik Pandya     | 22      |

#### Step-by-Step Manual Process

1. **Draw the axes**  
   - Draw a horizontal line (X-axis) for bowler names.  
   - Draw a vertical line (Y-axis) for number of wickets.

2. **Scale the Y-axis**  
   - Decide intervals (e.g., every 5 wickets: 0, 5, 10, 15, 20, 25, 30, 35).  
   - Mark and label these numbers on the Y-axis.

3. **Mark equal spacing on X-axis**  
   - Write the five bowler names with equal space between them.

4. **Draw the bars**  
   - For each bowler, draw a vertical rectangle (bar) from the X-axis up to the correct height on the Y-axis.  
     – Ashwin → up to 32  
     – Bumrah → up to 30  
     – Arshdeep → up to 27  
     – Chahal → up to 26  
     – Pandya → up to 22  
   - Make all bars the same width.

5. **Colour or shade the bars** (optional)  
   Use different colours or patterns for visual appeal.

6. **Label the bars**  
   Write the exact number (32, 30, etc.) on top of or inside each bar.

7. **Add title and axis labels**  
   - Title: “Top 5 Indian Bowlers – T20 World Cup Wickets”  
   - X-axis label: “Bowler”  
   - Y-axis label: “Wickets Taken”

**Final Result** 
![Bar Chart](../imgs/BarChartResult.png)

---

## 3. Basic Statistical Descriptions 

**Three main categories:**  
1. Measures of **Central Tendency** (location)  
2. Measures of **Dispersion** (spread/variability)  
3. Measures of **Shape** (skewness & kurtosis)

### 3.1 Central Tendency  
**Mean** (Arithmetic Average): Sum / n  
- Sensitive to outliers  
**Median** (Middle value): Robust to outliers  
**Mode** (Most frequent): For categorical/nominal  

**When to use:**  
- Symmetric → Mean  
- Skewed/Outliers → Median  
- Categorical → Mode

**Example:**  
Salaries: 10k, 12k, 15k, 20k, 100k → Mean high (due to outlier), Median = 15k (better representative)

---

### 3.2 Dispersion / Variability  
**Range** = Max – Min (simple but outlier-sensitive)  
**Variance** = Average squared deviation from mean  
**Standard Deviation** (σ) = √Variance (same unit as data)  
**Interquartile Range (IQR)** = Q3 – Q1 (robust)

**Example:**  
Two classes same mean CGPA but one has SD=0.5 (consistent), other SD=2 (varied) → Dispersion tells quality/consistency.

### 3.3 Shape of Distribution – Skewness & Kurtosis  
**Skewness** (Asymmetry):  
- 0 → Symmetric (normal)  
- Positive (>0) → Right-skewed (tail on right, mean > median)  
- Negative (<0) → Left-skewed (tail on left, mean < median)  

**Kurtosis** (Tailedness/Peakedness):  
- 3 (or excess kurtosis = 0) → Mesokurtic (normal)  
- >3 (positive excess) → Leptokurtic (heavy tails, more outliers)  
- <3 (negative excess) → Platykurtic (light tails, fewer outliers)

**Real-world Impact in Data Mining:**  
- Skewed data → Log transform before modeling  
- High kurtosis → More outliers → Needs robust methods

## 4. Summary Table – Quick Revision (Very Important!)

| Concept                  | Key Measures/Techniques                  | What it Reveals                          | Robust to Outliers? | Example Use in Preprocessing          |
|--------------------------|------------------------------------------|------------------------------------------|---------------------|---------------------------------------|
| Central Tendency         | Mean, Median, Mode                       | Typical/central value                    | Median & Mode       | Choose representative value           |
| Dispersion               | Range, Variance, SD, IQR                 | Spread/variability                       | IQR                 | Scale/normalize data                  |
| Shape – Skewness         | Skewness coefficient                     | Asymmetry (left/right tail)              | —                   | Decide transformation                 |
| Shape – Kurtosis         | Kurtosis coefficient                     | Tailedness (outliers)                    | —                   | Handle heavy/light tails              |
| Visualization            | Histogram, Box Plot, Q-Q Plot, Scatter   | Distribution, outliers, relationships    | Box & Q-Q           | Spot issues before mining             |

## 5. Class Activity & Q&A 

**Quick Questions:**  
1. In a right-skewed salary distribution, which central tendency is best? Why?  
2. Draw a rough box plot for data with many outliers on the high side.  
3. How would a histogram look for bimodal customer age data?  

**Homework:**  
- Download any small dataset (e.g., Iris from UCI/Kaggle)  
- Compute mean, median, mode, SD, skewness for one numeric column  
- Sketch histogram & box plot (hand-drawn or Python)


**Motivation Quote:**  
"Visualize first, model later – good EDA saves you from garbage-in-garbage-out!"  

