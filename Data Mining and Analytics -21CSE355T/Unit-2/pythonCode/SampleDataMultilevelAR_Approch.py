import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transactions (using leaf-level items + some higher-level codes)
transactions = [
    ['Laptop', 'Smartphone', 'Milk', 'Chips'],
    ['Tablet', 'Milk', 'Coke', 'Cookies'],
    ['Laptop', 'Yogurt', 'Chips'],
    ['Smartphone', 'Tablet', 'Coke'],
    ['Laptop', 'Smartphone', 'Milk', 'Cookies'],
    ['Yogurt', 'Chips', 'Coke'],
    ['Tablet', 'Milk', 'Cookies'],
]

# Multilevel item mapping (for encoding)
item_hierarchy = {
    # level-2 (leaf)
    'Laptop':     ('Electronics', 'All'),
    'Smartphone': ('Electronics', 'All'),
    'Tablet':     ('Electronics', 'All'),
    'Milk':       ('Dairy', 'Food', 'All'),
    'Yogurt':     ('Dairy', 'Food', 'All'),
    'Chips':      ('Snacks', 'Food', 'All'),
    'Cookies':    ('Snacks', 'Food', 'All'),
    'Coke':       ('Beverages', 'Food', 'All'),
}

# Create one-hot encoded dataframe with all levels
def encode_multilevel(transactions, min_level=0):
    all_items = set()
    for trans in transactions:
        for item in trans:
            all_items.add(item)
            if item in item_hierarchy:
                parent = item_hierarchy[item]
                for p in parent:
                    all_items.add(p)
    
    encoded = []
    for trans in transactions:
        row = {item: 0 for item in all_items}
        present = set(trans)
        for item in trans:
            row[item] = 1
            if item in item_hierarchy:
                for parent in item_hierarchy[item]:
                    row[parent] = 1
        encoded.append(row)
    
    return pd.DataFrame(encoded).fillna(0).astype(int)

df_multilevel = encode_multilevel(transactions)
print("Multilevel encoded data shape:", df_multilevel.shape)
print(df_multilevel.columns.tolist())