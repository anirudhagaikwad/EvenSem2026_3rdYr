**What is a Multi-dimensional Association Rule?**
In traditional (single-dimensional) association rules, we find patterns like {milk, bread} → {butter} (only items/products).
Multi-dimensional association rules involve multiple dimensions/attributes (often including quantitative/numeric ones like age, income, etc.).

> Examples:age(X, "young") ∧ income(X, "high") → buys(X, "laptop")
occupation(X, "student") ∧ marital_status(X, "single") → buys(X, "gaming console")

In Multi dimensional association rule Qualities can be absolute or quantitative.
➜ Quantitative characteristics are numeric and consolidates order.
➜ Numeric traits should be discretized.
➜ Multi dimensional affiliation rule comprises of more than one measurement.
➜ Example -buys(X, "IBM Laptop computer")buys(X, "HP Inkjet Printer")

**Approaches in mining multi dimensional affiliation rules** : Three approaches in mining multi dimensional affiliation rules are as following.
1. Using static discretization of quantitative qualities :
    ➜ Discretization is static and happens preceding mining.
    ➜ Discretized ascribes are treated as unmitigated.
    ➜ Use apriori calculation to locate all k-regular predicate sets(this requires k or k+1 table outputs). Each subset of regular predicate set should be continuous.

> Example - If in an information block the 3D cuboid (age, pay, purchases) is continuous suggests (age, pay), (age, purchases), (pay, purchases) are likewise regular. Note - Information blocks are appropriate for mining since they make mining quicker. The cells of an n-dimensional information cuboid relate to the predicate cells.

2. Using powerful discretization of quantitative traits :
    ➜ Known as mining Quantitative Association Rules.
    ➜ Numeric properties are progressively discretized.
    
> Example -:age(X, "20..25") Λ income(X, "30K..41K")buys ( X, "Laptop Computer") 

3. Grid FOR TUPLES : Using distance based discretization with bunching - This id dynamic discretization measure that considers the distance between information focuses. It includes a two stage mining measure as following.
    ➜ Perform bunching to discover the time period included.
    ➜ Get affiliation rules via looking for gatherings of groups that happen together.
>The resultant guidelines may fulfill -
>Bunches in the standard precursor are unequivocally connected with groups of rules in the subsequent.
>Bunches in the forerunner happen together.
>Bunches in the ensuing happen together.
