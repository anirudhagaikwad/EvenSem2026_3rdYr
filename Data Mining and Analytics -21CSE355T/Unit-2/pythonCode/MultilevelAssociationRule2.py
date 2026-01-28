print("\n=== 2. Reduced Support Approach (level-based decreasing support) ===")

# Define support thresholds per level (heuristic: lower levels → lower support)
level_support = {
    'level-0': 0.30,   # All
    'level-1': 0.25,
    'level-2': 0.15    # leaf items → most specific
}

# Function to assign min_support based on itemset level
def get_itemset_level(itemset):
    if any(x in {'All'} for x in itemset): return 'level-0'
    if any(x in {'Electronics', 'Food'} for x in itemset): return 'level-1'
    return 'level-2'

# Run Apriori with uniform low support first (catch everything)
freq_reduced = apriori(
    df_multilevel, 
    min_support=0.10,   # lowest possible to start
    use_colnames=True
)

# Filter itemsets according to level-specific support
freq_reduced['level'] = freq_reduced['itemsets'].apply(
    lambda s: get_itemset_level(s)
)
freq_reduced = freq_reduced[
    freq_reduced.apply(
        lambda row: row['support'] >= level_support[row['level']], 
        axis=1
    )
]

rules_reduced = association_rules(
    freq_reduced, 
    metric="confidence", 
    min_threshold=0.55
)

print("Frequent itemsets after level-based filtering:")
print(freq_reduced[['support', 'itemsets', 'level']])

print("\nInteresting rules (reduced support):")
print(rules_reduced[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
      .sort_values('lift', ascending=False)
      .head(10))