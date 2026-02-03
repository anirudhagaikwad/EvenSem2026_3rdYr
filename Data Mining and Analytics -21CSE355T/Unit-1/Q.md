**Approximate Weightage Distribution** (based on topics and time allocation:  
- Introduction + Kinds of Data + Kinds of Patterns → ~20%  
- Data Objects and Attribute Types → ~25% (very important, frequent 10/16 mark questions)  
- Data Visualization → ~10–15%  
- Basic Statistical Descriptions → ~10%  
- Data Preprocessing (Cleaning, Integration, Transformation, Reduction) → **~35–40%** (highest weightage, most detailed topic)

**Question Types:**  
- Short answer (2/5 marks)  
- Descriptive (8/10/16 marks)  
- Differences/Comparisons  
- Explain with examples  

###  Question Bank – Unit-1

**Section A: Introduction & Basic Concepts**  
1. Define data mining. How is it different from traditional data analysis?  
2. What is Knowledge Discovery in Databases (KDD)? Explain the steps in KDD process.  
3. What are the different kinds of data on which data mining can be performed? Give examples for each.  
4. List and explain the various kinds of patterns that can be discovered in data mining.  
5. Differentiate between descriptive and predictive data mining tasks with suitable examples.  
6. What is the importance of data mining in the current era of big data? Give two real-world applications.  
7. Explain the challenges and issues in data mining.  

**Section B: Data Objects and Attribute Types** (High weightage)  
8. Define data object and attribute. Explain their role in a dataset with an example.  
9. Classify the different types of attributes in data mining with examples for each type.  
10. Explain nominal, ordinal, interval-scaled, and ratio-scaled attributes with suitable examples.  
11. What is the difference between symmetric and asymmetric binary attributes? Give examples.  
12. Why is it important to know the type of attribute before applying data mining techniques?  
13. Compare nominal and ordinal attributes. Can arithmetic operations be performed on them?  
14. Explain interval-scaled and ratio-scaled attributes. Why ratio-scaled is more powerful?  
15. Give examples of real-world datasets and classify at least 5 attributes in each according to their types.  

**Section C: Data Visualization**  
16. What is the role of data visualization in data preprocessing and exploratory data analysis?  
17. Explain histogram with an example. How does it help in understanding data distribution?  
18. Describe box plot (box-and-whisker plot). What information can be obtained from it?  
19. What is a quantile plot (Q-Q plot)? Explain its use in checking normality of data.  
20. Explain scatter plot and its importance in detecting correlation and clusters.  
21. Differentiate between histogram and box plot. When would you prefer one over the other?  

**Section D: Basic Statistical Descriptions**  
22. Explain the measures of central tendency (mean, median, mode) with examples.  
23. When would you prefer median over mean? Justify with an example.  
24. Define measures of dispersion. Explain range, variance, standard deviation, and IQR.  
25. What is skewness? Explain positive, negative, and zero skewness with sketches.  
26. Define kurtosis. Differentiate between leptokurtic, mesokurtic, and platykurtic distributions.  
27. How do basic statistical descriptions help in identifying noise and outliers in data?  

**Section E: Data Preprocessing** (Highest weightage – most questions)  
28. What is data preprocessing? Why is it considered the most important and time-consuming step in data mining?  
29. List and explain the major tasks in data preprocessing.  
30. Explain data cleaning in detail. What are the different ways to handle missing values?  
31. Describe binning methods for smoothing noisy data. Explain smoothing by bin means with an example.  
32. What are outliers? How can they be detected and handled during data cleaning?  
33. Explain data integration. What are the major issues in data integration?  
34. What is entity identification and redundancy detection in data integration?  
35. Define data transformation. Explain normalization techniques (min-max, z-score, decimal scaling) with formulas and examples.  
36. What is data discretization? Explain equal-width and equal-frequency binning with examples.  
37. Explain data reduction. Why is it necessary?  
38. Describe attribute subset selection in dimensionality reduction. What are filter and wrapper methods?  
39. Explain numerosity reduction techniques: histograms, clustering, sampling.  
40. What are the different types of sampling methods in data reduction? Explain stratified sampling with an example.  
41. Differentiate between data cleaning and data transformation.  
42. Compare data reduction and data transformation. Give situations where each is preferred.  
43. Explain the concept of concept hierarchy generation in data preprocessing.  
44. How does data preprocessing affect the performance of classification and clustering algorithms?  
45. Draw and explain the flowchart of major steps in data preprocessing.  

**Mixed / Important Long-Answer Type Questions**  
46. Explain data objects and attribute types in detail. Why is the knowledge of attribute types essential before mining? (16 marks)  
47. Discuss data visualization techniques in detail. How do they help in data understanding? (10/16 marks)  
48. What are the measures of central tendency and dispersion? Explain with examples and their significance in data mining. (10 marks)  
49. Describe data preprocessing in detail. Explain cleaning, integration, transformation, and reduction with techniques and examples. (16 marks – most repeated)  
50. Write a detailed note on data preprocessing tasks, challenges in real-world data, and how preprocessing improves mining results. (16 marks)
51. Explain the different kinds of data and patterns in data mining with examples.
52. Describe any four data preprocessing techniques with their purpose.
53. Differentiate between data discretization and data reduction. Give one method for each.
53. Explain the steps of the Apriori algorithm with a small example.
54. What is market basket analysis? Define support and confidence with formulas.
55. Describe the advantages of FP-growth over Apriori.
56. Discuss the complete data preprocessing process in detail, including cleaning, integration, transformation, and reduction techniques. Illustrate with suitable examples.
57. Explain attribute subset selection methods and data visualization techniques used in data preparation for mining. Provide examples of each.
58. Describe the Apriori algorithm in detail. Discuss its limitations and how mining frequent itemsets without candidate generation addresses them.
59. Explain multilevel and multidimensional association rules. Discuss constraint-based association mining with examples.




**Preparation Tips for Exam**  
- Focus maximum on **Data Preprocessing** (questions 28–50) – usually 1 full 16-mark question + many short ones.  
- **Data Objects & Attribute Types** (questions 8–15) – compulsory short + long.  
- Memorize **tables** (attribute types, preprocessing tasks) and **examples**.  
- Practice diagrams: Histogram, Box plot, Preprocessing flowchart, Attribute type hierarchy.  
- Use diagrams/tables for attributes, preprocessing steps, reduction techniques  
- Give real-life examples (market basket, customer data)  
- Write definitions first → explanation → example → advantages  
- Revise from **Han & Kamber** book – Chapter 2 & 3 (most questions come from there)

## Some other Questions 


# MCQs on Data Mining and Analytics  
**(Unit 1 & Unit 2 – Based on Syllabus: 21CSE355T)**

These 50 multiple-choice questions cover **Unit 1** (Data Mining Introduction & Preprocessing) and **Unit 2** (Associations and Correlations).  

### Unit 1: Data Mining Introduction & Preprocessing

1. Which of the following best describes data mining?  
   A. Storing large amounts of data in a database  
   **B.** Extracting useful patterns and knowledge from large datasets  
   C. Deleting redundant data records  
   D. Creating backups of data files  

2. What are the main kinds of patterns discovered in data mining?  
   **A.** Classification, clustering, association, outliers, trends  
   B. Only classification and regression  
   C. Only data storage and retrieval  
   D. Only visualization patterns  

3. Data objects in a dataset are also commonly referred to as:  
   **A.** Tuples or records  
   B. Attributes only  
   C. Dimensions  
   D. Classes  

4. Which attribute type has meaningful differences but no true zero point?  
   A. Nominal  
   B. Ordinal  
   **C.** Interval  
   D. Ratio  

5. Data visualization is primarily used to:  
   A. Store data permanently  
   **B.** Help users understand complex data through graphical representation  
   C. Encrypt data  
   D. Reduce data size  

6. Which step in data preprocessing involves filling missing values or smoothing noisy data?  
   **A.** Data cleaning  
   B. Data integration  
   C. Data transformation  
   D. Data reduction  

7. Merging data from multiple sources (e.g., databases) is called:  
   A. Data cleaning  
   **B.** Data integration  
   C. Data discretization  
   D. Data sampling  

8. Normalization and aggregation are examples of:  
   A. Data cleaning  
   B. Data integration  
   **C.** Data transformation  
   D. Attribute subset selection  

9. Dividing continuous data into bins or intervals is known as:  
   A. Data integration  
   **B.** Data discretization  
   C. Data cleaning  
   D. Sampling  

10. Which data reduction technique removes irrelevant or redundant attributes?  
    **A.** Attribute subset selection  
    B. Clustering  
    C. Sampling  
    D. Histogram  

11. Histograms are used in data reduction primarily for:  
    A. Attribute selection  
    **B.** Data summarization and discretization  
    C. Data integration  
    D. Outlier detection  

12. Using clustering for data reduction involves:  
    A. Replacing data with cluster representatives  
    B. Removing all clusters  
    **C.** Representing data points by their cluster centroids  
    D. Increasing data size  

13. Random sampling is a technique used for:  
    A. Data cleaning  
    B. Data integration  
    **C.** Data reduction  
    D. Data visualization  

14. Which of the following is NOT a data preprocessing step?  
    A. Data cleaning  
    B. Data transformation  
    **C.** Model training  
    D. Data discretization  

15. What is the purpose of data discretization in preprocessing?  
    A. To increase data size  
    **B.** To convert continuous attributes into categorical ones  
    C. To merge databases  
    D. To visualize data  

16. Which attribute type has order but no fixed differences (e.g., rankings)?  
    A. Nominal  
    **B.** Ordinal  
    C. Interval  
    D. Ratio  

17. Data objects with many attributes are often called:  
    A. Low-dimensional  
    **B.** High-dimensional  
    C. Single-dimensional  
    D. Zero-dimensional  

18. Which of the following is a kind of data?  
    **A.** Transactional data  
    B. Only structured data  
    C. Only text data  
    D. Only image data  

19. In data preprocessing, handling inconsistent data falls under:  
    **A.** Data cleaning  
    B. Data reduction  
    C. Data visualization  
    D. Data integration  

20. Sampling can be used to:  
    **A.** Reduce the dataset size while preserving patterns  
    B. Increase dataset size  
    C. Encrypt data  
    D. Change attribute types  

21. Which technique selects a subset of attributes to reduce dimensionality?  
    **A.** Attribute subset selection  
    B. Data integration  
    C. Data transformation  
    D. Clustering  

22. What is the main goal of data preprocessing before mining?  
    **A.** Improve data quality for accurate pattern discovery  
    B. Delete all data  
    C. Visualize only  
    D. Store data  

23. Ratio-scaled attributes have:  
    A. No true zero  
    **B.** A true zero point and meaningful ratios  
    C. Only order  
    D. Only categories  

24. Which is NOT a data reduction method mentioned in the syllabus?  
    A. Histograms  
    B. Clustering  
    C. Sampling  
    **D.** Encryption  

25. Data visualization techniques include:  
    **A.** Scatter plots, histograms, box plots  
    B. Only tables  
    C. Only text summaries  
    D. Only databases  

### Unit 2: Associations and Correlations

26. Market basket analysis is commonly used for:  
    **A.** Finding frequent itemsets in transaction data  
    B. Classification  
    C. Clustering  
    D. Outlier detection  

27. The Apriori algorithm is used to:  
    **A.** Generate frequent itemsets using candidate generation  
    B. Avoid candidate generation  
    C. Only compute correlation  
    D. Cluster data  

28. In association rules, support of an itemset is:  
    **A.** The proportion of transactions containing the itemset  
    B. The confidence level  
    C. The lift value  
    D. The correlation coefficient  

29. Which algorithm mines frequent itemsets without candidate generation?  
    A. Apriori  
    **B.** FP-growth (Mining Frequent Itemsets without Candidate Generation)  
    C. Vertical data format method  
    D. Constraint-based mining  

30. The vertical data format represents:  
    **A.** Items with lists of transaction IDs (tidlists)  
    B. Transactions with items  
    C. Only horizontal tables  
    D. Only candidate sets  

31. Closed frequent itemsets are:  
    **A.** Frequent itemsets with no proper superset having the same support  
    B. All frequent itemsets  
    C. Maximal itemsets only  
    D. Minimal itemsets  

32. Mining multilevel association rules involves:  
    **A.** Using item taxonomies or hierarchies  
    B. Only single-level items  
    C. Only binary attributes  
    D. Only quantitative data  

33. Multidimensional association rules involve:  
    **A.** Rules across multiple dimensions (e.g., age, income, purchase)  
    B. Only one dimension  
    C. Only transactional data  
    D. Only categorical data  

34. Correlation analysis in association rules uses measures like:  
    A. Only support  
    **B.** Lift, chi-square, all-confidence  
    C. Only confidence  
    D. Only conviction  

35. Constraint-based association mining allows:  
    **A.** User-specified constraints on rules (e.g., items, min support)  
    B. No constraints  
    C. Only automatic rules  
    D. Only random mining  

36. The main drawback of the Apriori algorithm is:  
    **A.** Large number of candidate itemsets  
    B. No candidate generation  
    C. Vertical format only  
    D. Multilevel only  

37. FP-growth uses:  
    **A.** FP-tree (frequent pattern tree)  
    B. Candidate pruning  
    C. Only vertical format  
    D. Only correlation  

38. Mining frequent itemsets using vertical data format is efficient for:  
    **A.** Intersection-based support counting  
    B. Horizontal scanning  
    C. Candidate generation  
    D. Clustering  

39. In market basket analysis, a rule like {bread} → {butter} has high:  
    **A.** Support and confidence  
    B. Only lift  
    C. Only correlation  
    D. No meaning  

40. Lift > 1 in correlation analysis indicates:  
    **A.** Positive correlation (items occur together more than expected)  
    B. Negative correlation  
    C. No correlation  
    D. Independence  

41. Which is NOT a technique in Unit 2?  
    A. Apriori  
    B. FP-growth  
    **C.** Decision tree induction  
    D. Constraint-based mining  

42. Mining closed frequent itemsets helps in:  
    **A.** Reducing redundancy in frequent itemsets  
    B. Increasing itemsets  
    C. Clustering  
    D. Classification  

43. Multilevel association rules are useful when items have:  
    **A.** Hierarchical relationships (e.g., milk → dairy → food)  
    B. No hierarchy  
    C. Only flat structure  
    D. Only numerical values  

44. In constraint-based mining, a rule can be constrained by:  
    **A.** Item names, min support, min confidence, etc.  
    B. Only random constraints  
    C. No constraints  
    D. Only maximum length  

45. The Apriori property states that:  
    **A.** All subsets of a frequent itemset are frequent  
    B. All supersets are frequent  
    C. Only maximal sets are frequent  
    D. Only closed sets  

46. Vertical data format is also known as:  
    **A.** Item-TID list format  
    B. Transaction-item format  
    C. Horizontal format  
    D. Matrix format  

47. Correlation analysis helps to:  
    **A.** Find if items are statistically independent or correlated  
    B. Only find frequent items  
    C. Cluster data  
    D. Classify data  

48. Which method does NOT require candidate generation?  
    **A.** Mining Frequent Itemsets without Candidate Generation (FP-growth)  
    B. Apriori  
    C. Vertical data format (partial)  
    D. Multilevel  

49. In association rules, confidence measures:  
    **A.** Strength of implication (P(Y|X))  
    B. Frequency of itemset  
    C. Correlation only  
    D. Lift only  

50. Constraint-based association mining is useful for:  
    **A.** Guiding the search to interesting rules only  
    B. Generating all possible rules  
    C. Ignoring user input  
    D. Only multilevel rules  

51. Which of the following is a nominal attribute type?  
   a) Age b) Temperature c) Gender d) Salary 

52. Data visualization is primarily used to:  
   a) Clean data b) Discover patterns c) Reduce dimensions d) Transform values 

53. Which step in data preprocessing handles missing values?  
   a) Data integration b) Data cleaning c) Data discretization d) Sampling 

54. Histogram is a technique used in:  
   a) Data cleaning b) Data reduction c) Data transformation d) Attribute selection  

55. Clustering for data reduction belongs to:  
   a) Numerosity reduction b) Dimensionality reduction c) Data integration d) Discretization

56. In market basket analysis, support of an itemset is defined as:  
   a) Confidence / Lift b) Frequency of occurrence / Total transactions c) Probability of co-occurrence d) Correlation coefficient

57. The Apriori algorithm uses which property to prune candidates?  
   a) Downward closure b) Upward closure c) Monotonicity d) Apriori property

58. FP-growth algorithm avoids:  
   a) Candidate generation b) Support counting c) Tree construction d) Pattern mining

59. Correlation analysis in association mining is used to:  
   a) Find frequent itemsets b) Identify interesting rules c) Generate candidates d) Prune rules 

60. Multidimensional association rules involve:  
    a) Single dimension b) Multiple dimensions c) Binary attributes only d) Transactional data only 


**Short Notes:**  
1. Kinds of Data in Data Mining  
2. Types of Attributes with examples  
3. Data Preprocessing – Need & Tasks  
4. Data Visualization Techniques  
5. Attribute Subset Selection  
6. Sampling Methods in Data Reduction  

**Long Answers :**  
1. Explain Data Preprocessing in detail with techniques for Cleaning, Integration, Transformation & Reduction.  
2. Discuss Data Reduction strategies with focus on Histograms, Clustering & Sampling.  
3. What are kinds of patterns in data mining? Explain with examples.  
4. Describe Data Objects & Attribute Types in detail.

