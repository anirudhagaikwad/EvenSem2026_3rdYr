# Approach 2: Dynamic Discretization → Quantitative Association Rules
# We manually create small bins (or could use clustering/entropy-based methods)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Same sample data
data = {
    'age':    [22, 35, 28, 45, 19, 52, 31, 24, 39, 60],
    'income': [25, 80, 45, 120, 18, 200, 55, 30, 90, 150],
    'buys_computer': ['yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes']
}
df = pd.DataFrame(data)

# Step 1: Dynamic-style discretization with finer/more adaptive bins
# Here we use many small fixed intervals (simulating dynamic partitioning)
age_bins = [0, 20, 25, 30, 35, 40, 45, 50, 60, 100]
income_bins = [0, 20, 30, 40, 50, 70, 100, 150, 500]

df['age_range']    = pd.cut(df['age'],    bins=age_bins,    right=False, labels=[f"{a}..{b-1}" for a,b in zip(age_bins[:-1], age_bins[1:])])
df['income_range'] = pd.cut(df['income'], bins=income_bins, right=False, labels=[f"{a}..{b-1}K" for a,b in zip(income_bins[:-1], income_bins[1:])])

df = df.drop(['age', 'income'], axis=1)

# One-hot encode
df_onehot = pd.get_dummies(df)

# Frequent itemsets
freq = apriori(df_onehot, min_support=0.2, use_colnames=True)

# Rules - look for patterns like age_range(X, "20..25") ^ income_range(X, "30..40K") → buys_computer(yes)
rules = association_rules(freq, metric="confidence", min_threshold=0.5)

print("Quantitative Association Rules (dynamic/fine bins):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(8))