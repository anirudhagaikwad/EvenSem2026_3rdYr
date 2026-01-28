# Approach 3: Distance-based clustering + Association rules on cluster labels

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from mlxtend.frequent_patterns import apriori, association_rules

# Sample data (more points help clustering)
np.random.seed(42)
n = 100
data = {
    'age':    np.random.normal(35, 12, n).clip(18, 70).astype(int),
    'income': np.random.normal(70, 40, n).clip(10, 250).astype(int),
    'buys_computer': np.random.choice(['yes', 'no'], n, p=[0.65, 0.35])
}
df = pd.DataFrame(data)

# Phase 1: Distance-based clustering (KMeans on numeric attributes)
X = df[['age', 'income']].values

# Choose number of clusters (can use elbow method in practice)
kmeans_age    = KMeans(n_clusters=4, random_state=42).fit(X[:, [0]])
kmeans_income = KMeans(n_clusters=4, random_state=42).fit(X[:, [1]])

df['age_cluster']    = [f"age_c{i}"    for i in kmeans_age.labels_]
df['income_cluster'] = [f"inc_c{i}" for i in kmeans_income.labels_]

# Phase 2: Treat cluster labels as "items" → mine association rules
df_clusters = df[['age_cluster', 'income_cluster', 'buys_computer']]

df_onehot = pd.get_dummies(df_clusters)

freq = apriori(df_onehot, min_support=0.15, use_colnames=True)

rules = association_rules(freq, metric="confidence", min_threshold=0.6)

print("Association Rules after distance-based clustering:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))