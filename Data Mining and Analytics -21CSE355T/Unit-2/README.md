# Unit-2: Associations and Correlations

## Overview
This unit covers the concepts of association rule mining and correlation analysis in data mining. It focuses on techniques for discovering interesting relationships hidden in large datasets, such as those from market basket analysis. The unit is allocated 9 hours and builds on foundational data mining principles to explore algorithms for frequent itemset mining and rule generation.

## Key Topics

### Market Basket Analysis
- Analyzes customer purchasing patterns to identify associations between items (e.g., items frequently bought together).
- Forms the basis for recommendation systems and cross-selling strategies.

### Apriori Algorithm
- A classic algorithm for mining frequent itemsets.
- Uses a level-wise approach: Generates candidate itemsets and prunes them based on support thresholds.
- Key concepts: Support, confidence, and lift for evaluating association rules.

### Mining Frequent Itemsets without Candidate Generation
- Introduces efficient alternatives to Apriori, such as the FP-Growth (Frequent Pattern Growth) algorithm.
- Builds a compact FP-tree structure to avoid generating candidates, improving performance on large datasets.

### Mining Frequent Itemsets Using Vertical Data Format
- Represents data in a vertical layout (item-based lists of transactions) for faster intersection operations.
- Enhances efficiency in counting support for itemsets.

### Mining Closed Frequent Itemsets
- Focuses on closed itemsets, which are maximal frequent itemsets without supersets having the same support.
- Reduces redundancy in the output by mining only non-redundant patterns.

### Mining Multilevel Association Rules
- Discovers rules at multiple levels of abstraction (e.g., using hierarchies like "milk" → "dairy product").
- Allows for more generalized and insightful rules.

### Mining Multidimensional Association Rules
- Extends association mining to datasets with multiple dimensions or attributes (e.g., quantitative attributes like age or income).
- Handles complex data beyond binary transactional items.

### Correlation Analysis
- Measures the strength and direction of relationships between variables.
- Includes techniques like Pearson's correlation coefficient, chi-square tests, and lift to distinguish between association and actual correlation.

### Constraint-Based Association Mining
- Incorporates user-specified constraints (e.g., on items, support, or rule types) to focus mining efforts.
- Improves efficiency and relevance by pruning irrelevant patterns early.

## Learning Objectives
- Understand how to frame association rules using algorithms like Apriori.
- Apply correlation measures to validate associations.
- Utilize advanced techniques for efficient and targeted mining.

## References
- Jiawei Han and Micheline Kamber, "Data Mining Concepts and Techniques", Third Edition, Elsevier, 2012.
- Ian H. Witten, Eibe Frank and Mark A. Hall, "Data Mining: Practical Machine Learning Tools and Techniques", Fourth Edition, Elsevier, 2017.
