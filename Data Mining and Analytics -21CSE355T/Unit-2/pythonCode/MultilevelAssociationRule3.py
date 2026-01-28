print("\n=== 3. Group-based Support Approach ===")

# Define different min_support for different product groups
group_support = {
    'Electronics': 0.15,   # Electronics sells less frequently → lower threshold
    'Food':        0.25,   # Food items appear more often → higher threshold
    'All':         0.30,
    # default for leaf items without group
    'default':     0.18
}

def get_group(item):
    if item in {'All'}: return 'All'
    if item in {'Electronics', 'Food'}: return item
    if item in item_hierarchy:
        parents = item_hierarchy[item]
        if 'Electronics' in parents: return 'Electronics'
        if 'Food' in parents: return 'Food'
    return 'default'

# Run with low global support
freq_group = apriori(df_multilevel, min_support=0.10, use_colnames=True)

# Filter based on the **highest** group support requirement in the itemset
def meets_group_support(itemset, support):
    groups = {get_group(item) for item in itemset}
    required = max(group_support.get(g, group_support['default']) for g in groups)
    return support >= required

freq_group = freq_group[freq_group.apply(
    lambda row: meets_group_support(row['itemsets'], row['support']), 
    axis=1
)]

rules_group = association_rules(freq_group, metric="confidence", min_threshold=0.6)

print("Frequent itemsets (group-based support):")
print(freq_group[['support', 'itemsets']])

print("\nRules (group-based support):")
print(rules_group[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
      .sort_values('lift', ascending=False)
      .head(10))