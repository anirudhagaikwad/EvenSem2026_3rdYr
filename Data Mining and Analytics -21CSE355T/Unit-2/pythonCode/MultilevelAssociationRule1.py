print("\n=== 1. Uniform Support Approach ===")

# Same threshold for all levels
min_support_uniform = 0.3   # quite high → only strong patterns

freq_uniform = apriori(
    df_multilevel, 
    min_support=min_support_uniform, 
    use_colnames=True
)

rules_uniform = association_rules(
    freq_uniform, 
    metric="confidence", 
    min_threshold=0.6
)

print(f"\nFrequent itemsets (uniform support = {min_support_uniform}):")
print(freq_uniform[['support', 'itemsets']])

print("\nRules:")
print(rules_uniform[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values('lift', ascending=False).head(8))