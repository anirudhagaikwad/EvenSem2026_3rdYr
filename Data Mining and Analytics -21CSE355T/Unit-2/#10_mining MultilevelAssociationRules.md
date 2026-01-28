**Multilevel Association Rule** : Association rules created from mining information at different degrees of reflection are called various level or staggered association rules. Multilevel association rules can be mined effectively utilizing idea progressions under a help certainty system. Rules at a high idea level may add to good judgment while rules at a low idea level may not be valuable consistently. Utilizing uniform least help for all levels :
➜ At the point when a uniform least help edge is utilized, the pursuit system is rearranged.
➜ The technique is likewise straightforward, in that clients are needed to indicate just a single least help edge.
➜ A similar least help edge is utilized when mining at each degree of deliberation. (for example for mining from "PC" down to "PC"). Both "PC" and "PC" discovered to be incessant, while "PC" isn't.

**Needs of Multidimensional Rule** :
➜ Sometimes at the low data level, data does not show any significant pattern but there is useful information hiding behind it.
➜ The aim is to find the hidden information in or between levels of abstraction.

**Approaches to multilevel association rule mining** :
➜ Uniform Support(Using uniform minimum support for all level)
➜ Reduced Support (Using reduced minimum support at lower levels)
➜ Group-based Support(Using item or group based support)

Let's discuss one by one.

**1. Uniform Support** - At the point when a uniform least help edge is used, the search methodology is simplified. The technique is likewise basic in that clients are needed to determine just a single least help threshold. An advancement technique can be adopted, based on the information that a progenitor is a superset of its descendant.   the search keeps away from analyzing item sets containing anything that doesn't have minimum support. The uniform support approach however has some difficulties. It is unlikely that items at lower levels of abstraction will occur as frequently as those at higher levels of abstraction. If the minimum support threshold is set too high it could miss several meaningful associations occurring at low abstraction levels.

**2. Reduce Support** - For mining various level relationship with diminished support, there are various elective hunt techniques as follows.
    ➜ Level-by-Level independence - This is a full-broadness search, where no foundation information on regular item sets is utilized for pruning. Each hub is examined, regardless of whether its parent hub is discovered to be incessant.
    ➜ Level - cross-separating by single thing - A thing at the I level is inspected if and just if its parent hub at the (I-1) level is regular .all in all, we research a more explicit relationship from a more broad one. If a hub is frequent, its kids will be examined; otherwise, its descendant is pruned from the inquiry.
    ➜ Level-cross separating by - K-itemset - A-itemset at the I level is inspected if and just if it's For mining various level relationship with diminished support, there are various elective hunt techniques.
    ➜ Level-by-Level independence - This is a full-broadness search, where no foundation information on regular item sets is utilized for pruning. Each hub is examined, regardless of whether its parent hub is discovered to be incessant.
    ➜ Level - cross-separating by single thing - A thing at the 1st level is inspected if and just if its parent hub at the (I-1) the level is regular .all in all, we research a more explicit relationship from a more broad one. If a hub is frequent, its kids will be examined otherwise, its descendant is pruned from the inquiry.
    ➜ Level-cross separating by - K-item set - A-item set at the I level is inspected if and just if its corresponding parents A item set (i-1) level is frequent.

**3.Group-based support** - The group-wise threshold value for support and confidence is input by the user or expert. The group is selected based on a product price or item set because often expert has insight as to which groups are more important than others. Example - For e.g. Experts are interested in purchase patterns of laptops or clothes in the non and electronic category. Therefore low support threshold is set for this group to give attention to these items' purchase patterns.

