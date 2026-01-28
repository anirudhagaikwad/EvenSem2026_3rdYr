# Unit-1: Data Mining Introduction –   
**Topic: Data Preprocessing in Detail**  
**(Cleaning, Integration, Transformation, Reduction)**  
**Lecture Duration: 2 Hours** (Approx. 120 minutes – 45 min theory + techniques + 45 min examples + sub-methods + 30 min diagrams/discussion/Q&A)  
**Course: 21CSE355T - Data Mining and Analytics**  
**Reference:** Jiawei Han, Micheline Kamber – "Data Mining: Concepts and Techniques", 3rd Edition, Chapter 2 (Data Preprocessing)  
**Objective:** Students will deeply understand why preprocessing is crucial ("Garbage In → Garbage Out"), master the **four major tasks** (Cleaning, Integration, Transformation, Reduction), learn key techniques with real-world examples, and see how they connect to later units (e.g., discretization → classification, reduction → efficiency).

## 1. Introduction – Data Preprocessing? 
Data preprocessing in data mining is the essential step of cleaning, transforming, and organizing raw, messy data into a high-quality, usable format for analysis, ensuring algorithms get accurate inputs for reliable insights by handling missing values, inconsistencies, and noise through tasks like data cleaning, integration, reduction, and transformation. Without it, even advanced models produce poor, misleading results because real-world data is inherently incomplete, inconsistent, and noisy.

**Definition:** Data Preprocessing is the **first and most important step** in data mining – preparing raw, real-world data into a clean, consistent, suitable format for pattern discovery and modeling.

**Why needed Data Preprocessing ?**  
->Improves Data Quality: Addresses real-world messiness (inaccuracies, incompleteness, inconsistencies).
->Enhances Algorithm Performance: Makes data understandable and efficient for mining algorithms.
->Ensures Accurate Results: Prevents misleading patterns and flawed business decisions

**Major Tasks in Data Preprocessing**:  

![Summary](../imgs/SummaryDataPreProcessing.png)

->Data Cleaning: Addresses errors, inconsistencies, and missing values (e.g., filling gaps, smoothing noisy data, removing duplicates).
->Data Integration: Combines data from multiple sources into a coherent store, resolving schema conflicts and redundancies
->Data Transformation: Converts data into suitable formats, such as normalization (scaling) or aggregation (summarizing).
->Data Reduction: Reduces data volume while maintaining integrity, using methods like dimensionality reduction or data compression.
->Data Discretization: Converts continuous attribute values into categorical (interval) labels, simplifying analysis


## 2. Data Cleaning 
1. Data Cleaning: It is the process of identifying and correcting errors or inconsistencies in the dataset. It involves handling missing values, removing duplicates, and correcting incorrect or outlier data to ensure the dataset is accurate and reliable. Clean data is essential for effective analysis, as it improves the quality of results and enhances the performance of data models.

![Data Cleaning](../imgs/DataCleaning.png)

   **Missing Values**: This occur when data is absent from a dataset. You can either ignore the rows with missing data or fill the gaps manually, with the attribute mean, or by using the most probable value. This ensures the dataset remains accurate and complete for analysis.

   **Noisy Data**: It refers to irrelevant or incorrect data that is difficult for machines to interpret, often caused by errors in data collection or entry. It can be handled in several ways:
      ->Binning Method: The data is sorted into equal segments, and each segment is smoothed by replacing values with the mean or boundary values.
      ->Regression: Data can be smoothed by fitting it to a regression function, either linear or multiple, to predict values.
      ->Clustering: This method groups similar data points together, with outliers either being undetected or falling outside the clusters. These techniques help remove noise and improve data quality.
       
   **Removing Duplicates**: It involves identifying and eliminating repeated data entries to ensure accuracy and consistency in the dataset. This process prevents errors and ensures reliable analysis by keeping only unique records.
      
**Key Techniques & Examples:**

1. **Handling Missing Values**  
   - **Ignore tuple** → If many missing, delete row (simple but loss of info).  
   - **Fill manually** → Time-consuming, small datasets.  
   - **Fill with global constant** → e.g., "Unknown" or 0 (risky).  
   - **Use central tendency** → Mean (numeric), Median (skewed), Mode (categorical).  
     Example: Age missing → Fill with average age of customers (e.g., 35).  
   - **Use most probable value** → Regression, KNN imputation, Bayesian inference.  
   - **Prediction models** → Use other attributes to predict missing one.

2. **Noisy Data (Smooth it)**  
   - **Binning** (Smoothing by bin means/medians/boundaries)  
     Example: Sorted prices: 4,8,9,15,21,21,24,25,26,28,29,34  
     Equal-depth bins (3 bins) → Bin1: 4,8,9,15 → Bin mean=9 → Replace all with 9.  
   - **Regression** → Fit linear/multiple regression → Replace with predicted value.  
   - **Clustering** → Group similar → Outliers fall outside clusters → Detect/remove.

3. **Outlier Detection** → Statistical (z-score), Distance-based, Clustering-based (later in Unit-5).  
4. **Inconsistencies** → Correct format (date: DD/MM vs MM/DD), unified units (kg vs lbs).

**Real-world Example:** Bank transaction data – Missing salary → Fill with mean of similar customers. Noisy age=150 → Detect as outlier & remove.

## 3. Data Integration 

 Data Integration: It involves merging data from various sources into a single, unified dataset. It can be challenging due to differences in data formats, structures, and meanings. Techniques like record linkage and data fusion help in combining data efficiently, ensuring consistency and accuracy.

![Data Integration](../imgs/DataIntegration.png)

   **Record Linkage** is the process of identifying and matching records from different datasets that refer to the same entity, even if they are represented differently. It helps in combining data from various sources by finding corresponding records based on common identifiers or attributes.

   **Data Fusion** involves combining data from multiple sources to create a more comprehensive and accurate dataset. It integrates information that may be inconsistent or incomplete from different sources, ensuring a unified and richer dataset for analysis.

**Definition:** Merge data from **multiple sources** into one consistent dataset. Handle entity identification, redundancies, schema differences.

**Issues:**  
- Different names (cust_id vs customer_no)  
- Different units/formats  
- Redundancy → Tuple duplication, attribute correlation

**Techniques:**  
- **Entity identification** → Match records across sources (e.g., name + address).  
- **Redundancy detection** → Correlation analysis (Pearson), Chi-square test.  
- **Data fusion** → Resolve conflicts (take most recent/trusted value).

**Example:**  
Merge customer data from online store + physical store + CRM system.  
- Same customer appears as "John D" in one, "J. Doe" in another → Link using email/phone.  
- Remove redundant attribute (e.g., both have age → keep one).

**Real-world:** E-commerce company integrates sales from website + app + POS → Unified customer view for better analytics.

## 4. Data Transformation 
Data Transformation: It involves converting data into a format suitable for analysis. Common techniques include normalization, which scales data to a common range; standardization, which adjusts data to have zero mean and unit variance; and discretization, which converts continuous data into discrete categories. These techniques help prepare the data for more accurate analysis.

![Data Transformation](../imgs/DataTransform.png)

   **Data Normalization**: The process of scaling data to a common range to ensure consistency across variables.

   **Discretization**: Converting continuous data into discrete categories for easier analysis.

   **Data Aggregation**: Combining multiple data points into a summary form, such as averages or totals, to simplify analysis.

   **Concept Hierarchy Generation**: Organizing data into a hierarchy of concepts to provide a higher-level view for better understanding and analysis.

**Definition:** Convert data into appropriate form for mining. Includes normalization, smoothing, aggregation, generalization, attribute construction, **discretization**.

**Key Techniques:**

1. **Normalization** (Scale to common range)  
   - **Min-Max** → [0,1] or custom → v' = (v-min)/(max-min)  
   - **Z-score** → Mean=0, SD=1 → v' = (v-mean)/SD  
   - **Decimal scaling** → Divide by 10^k (e.g., salary 20000 → 2.0000)  
   Example: Income 1000–100000 → Normalize to [0,1] so not dominated by scale.

2. **Discretization** (Convert continuous → categorical)  
   - **Binning** (Equal-width / Equal-frequency)  
     Example: Age 0–100 → Equal-width 5 bins: 0-20, 21-40, etc.  
   - **Entropy-based** → Supervised (ID3-like)  
   - **Clustering** → K-means on values

3. **Aggregation** → Summary (sum, avg, count) for data cube/OLAP.

4. **Attribute Construction** → Create new attributes (e.g., age_group from age).

**Real-world:** Sensor data (high range) → Normalize before feeding to classifier.

## 5. Data Reduction 
 Data Reduction: It reduces the dataset's size while maintaining key information. This can be done through feature selection, which chooses the most relevant features, and feature extraction, which transforms the data into a lower-dimensional space while preserving important details. It uses various reduction techniques such as,

   **Dimensionality Reduction** (e.g., Principal Component Analysis): A technique that reduces the number of variables in a dataset while retaining its essential information.

   **Numerosity Reduction**: Reducing the number of data points by methods like sampling to simplify the dataset without losing critical patterns.

   **Data Compression**: Reducing the size of data by encoding it in a more compact form, making it easier to store and process

**Goal:** Reduce volume but produce **same or similar analytical results** (save time, memory).

**Types & Techniques:**

1. **Dimensionality Reduction**  
   - **Attribute subset selection** → Remove irrelevant/redundant attributes (wrapper/filter methods).  
   - **Principal Component Analysis (PCA)** → Transform to fewer uncorrelated components.

2. **Numerosity Reduction**  
   - **Parametric** → Regression models (store coefficients instead of data).  
   - **Non-parametric** → Histograms, Clustering (replace cluster with centroid), Sampling.

3. **Data Compression** → Encoding (e.g., wavelet, Huffman) for storage/transmission.

**Sampling Methods (Very Important):**  
- **Simple random**  
- **Stratified** → Preserve class proportions  
- **Cluster** → Randomly select clusters  
- **Systematic** → Every kth record

**Example:** 1 million customer records → Stratified sampling 10% → Maintain similar distribution for faster mining.

**Real-world:** Big retail data → Dimensionality reduction (remove correlated attributes) + sampling → Faster association rule mining.

## 6. Summary Table – Quick Revision 

| Task                  | Main Goal                              | Key Techniques                                      | Example Benefit                          |
|-----------------------|----------------------------------------|-----------------------------------------------------|------------------------------------------|
| Data Cleaning         | Fix errors, fill missing, smooth noise | Missing: Mean/Median, Noisy: Binning/Regression     | Prevent bias in classification           |
| Data Integration      | Merge multiple sources                 | Entity matching, Redundancy removal                 | Unified 360° customer view               |
| Data Transformation   | Suitable format                        | Normalization, Discretization (Binning), Aggregation| Equal scale, categorical for decision tree|
| Data Reduction        | Reduce size, same results              | Sampling, PCA, Clustering, Histograms               | Faster processing on big data            |

---
**Advantages of Data Preprocessing**
   ->Improved Data Quality: Ensures data is clean, consistent, and reliable for analysis.
   ->Better Model Performance: Reduces noise and irrelevant data, leading to more accurate predictions and insights.
   ->Efficient Data Analysis: Streamlines data for faster and easier processing.
   ->Enhanced Decision-Making: Provides clear and well-organized data for better business decisions.

**Limitations Disadvantages of Data Preprocessing**
   ->Time-Consuming: Requires significant time and effort to clean, transform, and organize data.
   ->Resource-Intensive: Demands computational power and skilled personnel for complex preprocessing tasks.
   ->Potential Data Loss: Incorrect handling may result in losing valuable information.
    Complexity: Handling large datasets or diverse formats can be challenging.
---
## 7. Class Activity & Q&A 

**Quick Questions:**  
1. For skewed salary data, which missing value fill is best: Mean or Median? Why?  
2. Why normalize before KNN/SVM?  
3. How does binning help in discretization? Give one example.  
4. When would you prefer stratified sampling over simple random?

**Homework:**  
- Take any dataset (Iris, Titanic from Kaggle)  
- Identify missing/noisy values, normalize one numeric column, discretize age using equal-width binning (hand or Python)  
- Submit next class.

**Next Class:** Associations and Correlations (Unit-2) – Market Basket Analysis.

**Motivation Quote:**  
"Clean data is the foundation of great insights – invest time in preprocessing, reap rewards in accurate mining!"

