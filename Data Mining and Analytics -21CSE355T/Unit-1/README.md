# Unit-1: Data Mining Introduction  
**Course: 21CSE355T - Data Mining and Analytics**  
**Referance Book - 1. Jiawei Han and Micheline Kamber, "Data Mining Concepts and Techniques", Third Edition, Elsevier, 2012.**
 
**Key Topics:** Introduction • Kinds of Data • Kinds of Patterns • Data Objects and Attribute Types • Data Visualization • Data Preprocessing (Cleaning, Integration, Transformation, Discretization, Reduction: Attribute Subset Selection, Histograms, Clustering, Sampling)


## 1. Introduction to Data Mining

**What is Data Mining?**  
Data Mining is the process of discovering interesting patterns, correlations, and knowledge from large amounts of data using statistical, machine learning, and database techniques.  
It is also known as **Knowledge Discovery in Databases (KDD)**.

**Why Data Mining?**  
- Data is growing exponentially (Big Data).  
- Raw data → Useful information → Knowledge → Decisions.  
- Applications: Market analysis, fraud detection, customer segmentation, medical diagnosis, etc.

**KDD Process**  
1. Data Selection  
2. Data Preprocessing  
3. Data Transformation  
4. Data Mining  
5. Interpretation/Evaluation

## 2. Kinds of Data (Types of Data in Data Mining)

| Type                  | Description                                                                 | Examples                              | Mining Suitability                  |
|-----------------------|-----------------------------------------------------------------------------|---------------------------------------|-------------------------------------|
| Relational Data       | Stored in tables (rows & columns)                                           | Customer database                     | Very common                         |
| Transactional Data    | Market basket data (sets of items purchased together)                       | Supermarket bills                     | Association rules                   |
| Data Warehouse        | Multidimensional (OLAP cubes)                                               | Sales by time, region, product        | OLAP + Mining                       |
| Advanced Data Types   | Text, multimedia (image, audio, video), time-series, spatial, web data     | Social media posts, satellite images  | Text/web/spatial mining             |

**Exam Tip:** Draw table for kinds of data + examples.

## 3. Kinds of Patterns (Data Mining Functionalities)

| Pattern Type              | Description                                                                 | Task Type       | Example                                  |
|---------------------------|-----------------------------------------------------------------------------|-----------------|------------------------------------------|
| Classification            | Predict class label                                                         | Predictive      | Customer churn prediction                |
| Clustering                | Group similar objects                                                       | Descriptive     | Customer segmentation                    |
| Association Rules         | Find relationships between items                                            | Descriptive     | Market basket: Bread → Butter            |
| Sequential Patterns       | Find patterns over time                                                     | Descriptive     | Customer buying sequence                 |
| Outlier/Anomaly Detection | Find unusual data points                                                    | Descriptive     | Fraud detection                          |
| Prediction                | Forecast future values                                                      | Predictive      | Stock price prediction                   |

**Exam Tip:** Classification vs Clustering (supervised vs unsupervised), Predictive vs Descriptive.

## 4. Data Objects and Attribute Types

**Data Object** = Record/Instance/Tuple/Row in dataset.  
**Attribute** = Feature/Column/Field.

**Types of Attributes** (Very Important – Memorize with examples!)

| Category              | Subtype                  | Description                                      | Examples                          | Operations Allowed                  | Distance Measure                    |
|-----------------------|--------------------------|--------------------------------------------------|-----------------------------------|-------------------------------------|-------------------------------------|
| Nominal               | —                        | Categories without order                         | Color, gender, blood group        | =, ≠                                | Simple matching                     |
| Ordinal               | —                        | Categories with meaningful order                 | Rank, education level             | =, ≠, <, >                          | Rank-based                          |
| Binary                | Symmetric                | 2 states (equal importance)                      | Male/Female                       | Hamming distance                    | Symmetric binary                    |
| Binary                | Asymmetric               | 2 states (rare positive important)               | Disease present/absent            | Jaccard coefficient                 | Asymmetric (ignore negative)        |
| Numeric               | Interval                 | Measured on scale with equal intervals           | Temperature (°C)                  | +, −, mean, std dev                 | Euclidean/Manhattan                 |
| Numeric               | Ratio                    | True zero point                                  | Age, height, salary               | All operations                      | Euclidean/Manhattan                 |

**Exam Tip:** Draw table + give 2 examples each + operations allowed + distance measures.

## 5. Data Visualization

**Purpose:** To understand data distribution, patterns, outliers, correlations quickly.

**Common Techniques:**

- **Histograms** → Frequency distribution of numeric data  
- **Box Plots** → Show quartiles, median, outliers  
- **Scatter Plots** → Relationship between two numeric attributes (correlation)  
- **Quantile Plots** → Compare distribution with uniform/normal  
- **Pie Charts** → Proportion of categories (nominal)  
- **Bar Charts** → Comparison of categories  

**Exam Tip:** Explain with example: "Scatter plot shows positive/negative correlation."

## 6. Data Preprocessing (Most Important Topic – 60-70% weightage in Unit-1)

**Why Preprocessing?**  
Raw data is noisy, incomplete, inconsistent, has missing values → Garbage In → Garbage Out.

**Major Tasks in Data Preprocessing:**

1. **Data Cleaning**  
   - Fill missing values (mean/median/mode, regression, KNN imputation)  
   - Smooth noisy data (binning, regression, clustering)  
   - Correct inconsistencies  
   - Remove outliers (sometimes)

2. **Data Integration**  
   - Merge data from multiple sources  
   - Handle schema integration (same attribute different names)  
   - Redundancy detection (correlation analysis)

3. **Data Transformation**  
   - Normalization (min-max, z-score, decimal scaling)  
   - Smoothing  
   - Aggregation  
   - Attribute construction  
   - **Discretization** (binning, entropy-based, clustering-based)

4. **Data Reduction**  
   Goal: Reduce volume but produce same/similar analytical results.

   **Types of Reduction Techniques:**

   | Technique                     | Type                  | Description                                                                 | When to Use                          |
   |-------------------------------|-----------------------|-----------------------------------------------------------------------------|--------------------------------------|
   | Attribute Subset Selection    | Dimensionality        | Remove irrelevant/redundant attributes (wrapper/filter methods)            | High-dimensional data                |
   | Histograms                    | Numerosity            | Divide data into buckets, represent by bucket means/frequencies            | Numeric data                         |
   | Clustering                    | Numerosity            | Cluster data → represent cluster by centroid                                | Detect outliers + reduce             |
   | Sampling                      | Numerosity            | Random/stratified/systematic/cluster sampling                               | Very large datasets                  |
   | Data Cube Aggregation         | —                     | OLAP cubes for summary                                                      | Multidimensional data                |

**Exam Tip:**  
- Draw **flowchart of preprocessing steps**  
- Explain each reduction technique with example + diagram (especially histogram binning & sampling)  
- Difference between Data Cleaning vs Transformation vs Reduction  
- Normalization methods with formula + example
