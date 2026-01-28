# Approach 1: Using Static Discretization of Quantitative Attributes → Treat as categorical → Use mlxtend Apriori
# pip install mlxtend  (if not installed)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample customer data with quantitative attributes
data = {
    'age':    [22, 35, 28, 45, 19, 52, 31, 24, 39, 60],
    'income': [25, 80, 45, 120, 18, 200, 55, 30, 90, 150],   # in thousands
    'buys_computer': ['yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes']
}

df = pd.DataFrame(data)

# Step 1: Static discretization (manual bins - done BEFORE mining)
df['age_bin']    = pd.cut(df['age'],    bins=[0, 30, 45, 100], labels=['young', 'middle', 'senior'])
df['income_bin'] = pd.cut(df['income'], bins=[0, 50, 100, 500], labels=['low', 'medium', 'high'])

# Drop original numeric columns
df = df.drop(['age', 'income'], axis=1)

# Step 2: One-hot encode all categorical columns (including discretized ones)
df_onehot = pd.get_dummies(df, columns=['age_bin', 'income_bin', 'buys_computer'])

# Step 3: Mine frequent itemsets with Apriori
frequent_itemsets = apriori(df_onehot, min_support=0.3, use_colnames=True)

# Step 4: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nMulti-dimensional Association Rules (static discretization):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])