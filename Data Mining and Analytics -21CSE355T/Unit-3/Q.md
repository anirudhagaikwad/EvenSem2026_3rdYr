# Unit-3: Classification and Prediction 

**Approximate Weightage Distribution:**
* **Basic Concepts & Decision Tree Induction:** ~25% (ID3, CART, and Attribute Selection are frequent 10/16 mark questions).
* **Bayes Classification Methods:** ~20% (Bayes’ Theorem and Naive Bayes numericals/theory).
* **Neural Networks & SVM:** ~20% (Complex but high-value for long answers).
* **Evaluation Metrics:** ~15% (Confusion Matrix, Precision, Recall—compulsory short/medium questions).
* **Techniques to Improve Accuracy & Regression:** ~20% (Ensemble methods like Bagging/Boosting).

---

## **Section A: Basic Concepts & Decision Trees**
1. **Define Classification and Prediction.** Differentiate between them with suitable examples.
2. **Explain the two-step process of Classification** (Model Construction and Model Usage).
3. **What is Decision Tree Induction?** Describe the general algorithm for building a tree.
4. **Compare ID3 and CART algorithms.** List their selection measures and branching styles.
5. **What is Tree Pruning?** Differentiate between pre-pruning and post-pruning. Why is it necessary?
6. **Explain the "Greedy" nature of decision tree algorithms.**



---

## **Section B: Attribute Selection Measures (High Weightage)**
7. **What are Attribute Selection Measures (ASM)?** Why are they called the "brain" of the tree?
8. **Explain Information Gain.** Define Entropy and provide the mathematical formula:
   $$Info(D) = -\sum_{i=1}^{m} p_i \log_2(p_i)$$
9. **Discuss Gain Ratio.** How does it address the bias of Information Gain toward many-valued attributes?
10. **Define Gini Index.** How is it used in the CART algorithm to find the best binary split?
    $$Gini(D) = 1 - \sum_{i=1}^{m} p_i^2$$
11. **Numerical Challenge:** Practice calculating Information Gain for a small dataset (e.g., the "Weather/Play Tennis" dataset).



---

## **Section C: Bayesian Classification**
12. **State and explain Bayes’ Theorem.** Define Posterior probability, Likelihood, and Prior probability.
    $$P(H|X) = \frac{P(X|H) P(H)}{P(X)}$$
13. **Explain Naive Bayesian Classification.** Why is the assumption of "class conditional independence" considered "naive"?
14. **What is Laplacian Correction (Smoothing)?** Explain its importance in handling zero-probability issues.
15. **Discuss the advantages and disadvantages of Naive Bayes**, especially regarding high-dimensional text data.

---

## **Section D: Neural Networks & SVM**
16. **Explain Classification by Backpropagation.** Describe the architecture of a Multilayer Feedforward Neural Network.
17. **Describe the Forward Pass and Backward Pass** in the Backpropagation algorithm.
18. **What are Activation Functions?** Explain the role of Sigmoid or ReLU in introducing non-linearity.
19. **Define Support Vector Machines (SVM).** What are "Support Vectors" and why are they critical?
20. **Explain the "Kernel Trick" in SVM.** How does it help in classifying non-linearly separable data?
21. **What is the Maximum Margin Hyperplane?** Illustrate how it separates two classes.



---

## **Section E: Evaluation & Accuracy Improvement**
22. **Define a Confusion Matrix.** Explain the four outcomes: TP, TN, FP, and FN.
23. **Explain the following metrics with formulas:**
    * **Accuracy:** $(TP + TN) / \text{Total}$
    * **Precision:** $TP / (TP + FP)$
    * **Recall:** $TP / (TP + FN)$
    * **F1-Score:** $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$
24. **Why is Accuracy not always a reliable metric?** Justify using the "Imbalanced Data" example.
25. **What are Ensemble Methods?** Explain Bagging and Boosting.
26. **Differentiate between Random Forest (Bagging) and AdaBoost (Boosting).**
27. **Explain K-Fold Cross-Validation.** How does it ensure the reliability of a model?



---

## **Section F: Prediction & Regression**
28. **Define Regression Analysis.** How does it differ from Classification?
29. **Explain Simple Linear Regression vs. Multiple Linear Regression.**
30. **What is the Method of Least Squares?** Explain how it minimizes the sum of squared residuals.
31. **List the evaluation metrics for Regression:** MAE, MSE, RMSE, and $R^2$.

---

# **MCQs on Classification and Prediction (Unit 3)**

1. Which of the following is a "Lazy Learner"?
   A. Decision Tree  **B. K-Nearest Neighbor** C. SVM  D. Neural Network

2. In Information Gain, a perfectly pure node has an Entropy of:
   **A. 0** B. 1  C. 0.5  D. Infinity

3. Which algorithm is strictly restricted to binary splits?
   A. ID3  **B. CART** C. C4.5  D. Naive Bayes

4. The problem of a model performing well on training data but poorly on test data is called:
   A. Underfitting  **B. Overfitting** C. Pruning  D. Scaling

5. Which metric is most important for a medical test where we cannot afford to miss a sick patient?
   A. Precision  **B. Recall (Sensitivity)** C. Accuracy  D. Specificity

6. SVM finds the hyperplane that:
   A. Minimizes the error  **B. Maximizes the margin** C. Minimizes the margin  D. Ignores outliers

7. Laplacian correction is used to:
   A. Reduce noise  **B. Avoid zero probabilities** C. Prune trees  D. Normalize data

8. Random Forest is an example of:
   **A. Bagging** B. Boosting  C. Pruning  D. Regression

9. The "Kernel Trick" is associated with:
   A. Naive Bayes  B. ID3  **C. SVM** D. KNN

10. Which activation function squashes values between 0 and 1?
    **A. Sigmoid** B. ReLU  C. Tanh  D. Linear

---

# **Mixed / Important Long-Answer Questions**

1.  **Decision Tree Induction:** Explain the building process, attribute selection (Information Gain), and the role of pruning. (16 marks)
2.  **Naive Bayes Numericals:** Given a dataset table, predict the class of a new tuple $X$ using Bayesian probabilities. (16 marks)
3.  **Neural Network Architecture:** Draw and explain the Backpropagation algorithm, including the weight update rule. (16 marks)
4.  **Evaluation Metrics:** Discuss the Confusion Matrix and derive formulas for Accuracy, Precision, Recall, and F1-score. (10 marks)
5.  **Ensemble Methods:** Compare Bagging and Boosting in detail. Explain how Random Forest improves results. (16 marks)

---

Here are **50 unique questions** from **Unit 3: Classification and Prediction** of the course 21CSE355T (Data Mining and Analytics).  

Questions 1–40 are theoretical (definitions, explanations, comparisons, derivations, advantages/disadvantages, etc.).  
**Questions 41–50** are designed as “solve the algorithm” type questions. Each provides a small, unique example dataset or values and asks you to perform the step-by-step computation (ID3, CART, Naïve Bayes, KNN, etc.). No question is repeated; every question covers a distinct aspect or variation of the unit topics.

### Questions 1–40 (Theoretical)

1. Define classification and prediction in the context of data mining.  
2. Differentiate between classification and prediction with suitable examples.  
3. Explain the basic process of decision tree induction.  
4. Describe how a decision tree is used for both classification and prediction.  
5. What are the major issues in decision tree induction?  
6. List and explain the three common attribute selection measures used in decision tree construction.  
7. Derive the formula for information gain and explain its role in attribute selection.  
8. Explain gain ratio and why it is preferred over information gain in some cases.  
9. Define Gini index and derive its formula for a binary split.  
10. Compare information gain, gain ratio, and Gini index as attribute selection measures.  
11. Write the step-by-step working of the ID3 algorithm.  
12. State the advantages and limitations of the ID3 algorithm.  
13. Explain how the CART algorithm differs from ID3 in splitting criteria and tree structure.  
14. Describe the stopping criteria used in CART algorithm construction.  
15. Explain the concept of tree pruning and why it is necessary.  
16. Differentiate between pre-pruning and post-pruning techniques.  
17. State Bayes’ theorem and explain its application in classification.  
18. Explain the Naïve Bayesian classification method and its underlying assumption.  
19. List the advantages and disadvantages of Naïve Bayes classifier.  
20. Describe the working of classification by backpropagation.  
21. Explain the role of learning rate and momentum in backpropagation algorithm.  
22. State the advantages and limitations of backpropagation-based neural network classifiers.  
23. Explain the basic principle of Support Vector Machines (SVM) for classification.  
24. Describe how a linear SVM finds the maximum-margin hyperplane.  
25. Explain the concept of kernel trick in non-linear SVM.  
26. List the advantages and disadvantages of SVM classifiers.  
27. Define lazy learners and give an example.  
28. Explain the k-Nearest Neighbour (KNN) algorithm in detail.  
29. Discuss the effect of choosing different values of k in KNN.  
30. State the advantages and limitations of KNN classifier.  
31. List and explain any five metrics used for evaluating classifier performance.  
32. Explain how a confusion matrix is constructed and used to compute accuracy, precision, recall and F1-score.  
33. Derive the formula for ROC curve and AUC and state its significance.  
34. Explain cross-validation techniques for reliable classifier evaluation.  
35. Describe how regression analysis can be used as a technique to improve classification accuracy.  
36. Differentiate between linear regression and logistic regression in the context of classification.  
37. Explain the concept of overfitting in classifiers and how pruning or regularization helps.  
38. Compare decision tree classifiers with SVM in terms of interpretability and performance.  
39. Compare Naïve Bayes with KNN with respect to speed, accuracy and assumptions.  
40. Discuss the role of ensemble methods (briefly) as a way to improve classification accuracy using regression or other techniques.

### Questions 41–50 (Solve the Algorithm – with unique example data)

41. **Solve using ID3 algorithm**  
Consider the following training dataset (PlayTennis variant):  

| Outlook | Temperature | Humidity | Wind | Play |
|---------|-------------|----------|------|------|
| Sunny   | Hot         | High     | Weak | No   |
| Sunny   | Hot         | High     | Strong | No |
| Overcast| Hot         | High     | Weak | Yes  |
| Rain    | Mild        | High     | Weak | Yes  |
| Rain    | Cool        | Normal   | Weak | Yes  |
| Rain    | Cool        | Normal   | Strong | No |
| Overcast| Cool        | Normal   | Strong | Yes |
| Sunny   | Mild        | High     | Weak | No   |
| Sunny   | Cool        | Normal   | Weak | Yes  |
| Rain    | Mild        | Normal   | Weak | Yes  |

Build the decision tree step-by-step using information gain. Show entropy calculations and the final tree structure.

42. **Solve using CART algorithm (Gini index)**  
Use the same dataset as Q41 but compute Gini index for the first split. Show Gini calculations for Outlook, Temperature, Humidity and Wind. Select the best attribute and draw the first-level split.

43. **Solve using Naïve Bayesian Classification**  
Given the following summarized training data for class “Buys_Computer”:  

- Total instances: 14  
- P(Yes) = 9/14, P(No) = 5/14  
- For attribute Age: Young (Yes=2, No=3), Middle (Yes=4, No=1), Old (Yes=3, No=1)  
- For attribute Income: High (Yes=2, No=3), Medium (Yes=4, No=1), Low (Yes=3, No=1)  

A new customer has Age = Middle and Income = Medium. Compute the posterior probabilities P(Yes | Middle, Medium) and P(No | Middle, Medium) step-by-step and classify the customer.

44. **Solve using Bayes’ theorem directly**  
A disease occurs in 1% of the population. A test is 95% accurate for positive cases and 90% accurate for negative cases. If a person tests positive, calculate the probability that the person actually has the disease. Show all steps using Bayes’ theorem.

45. **Solve using k-Nearest Neighbour (KNN)**  
Given 2D points:  
A(1,1) class +, B(2,2) class +, C(3,1) class +, D(1,3) class –, E(2,3) class –, F(3,3) class –  
Classify the new point P(2.5, 2.5) using Euclidean distance and k=3. Show distance calculations and majority vote.

46. **Solve using Backpropagation (simple single neuron)**  
A single neuron with sigmoid activation, initial weights w1=0.1, w2=0.2, bias b=0.3. Input (x1=1, x2=1), target output t=1. Learning rate η=0.5. Perform one iteration of backpropagation: compute net input, output, error, delta, and updated weights.

47. **Solve using Support Vector Machine (linear separable case)**  
Given points: Class + : (1,1), (2,2); Class – : (3,1), (4,2). Find the equation of the maximum-margin separating hyperplane (w·x + b = 0) by solving the margin maximization manually (show support vectors and margin calculation).

48. **Solve Tree Pruning (post-pruning)**  
A decision tree has a leaf node with 4 Yes and 1 No (error rate on validation set = 0.2). After pruning this leaf to the parent, the parent node now has 10 Yes and 6 No (error rate = 0.375). Using reduced error pruning, decide whether to prune this subtree and justify with error comparison.

49. **Solve using Linear Regression (for prediction/classification improvement)**  
Given data points (x,y): (1,2), (2,4), (3,5), (4,7). Compute the least-squares regression line y = mx + c. Show all summation calculations and the final equation. Explain how this line can be used for prediction.

50. **Solve Classifier Evaluation Metrics**  
A classifier produces the following confusion matrix on a test set of 100 instances:  

|          | Predicted Yes | Predicted No |
|----------|---------------|--------------|
| Actual Yes | 40            | 10           |
| Actual No  | 5             | 45           |

Compute: Accuracy, Precision, Recall, F1-score and Specificity. Show each formula and calculation.


**Preparation Tips for Exam:**
* **Focus on ASM:** Expect a 16-mark question combining Information Gain and Gini Index logic.
* **Formulas are Key:** Memorize the Bayes' formula and the evaluation metrics (Precision/Recall). 
* **Diagrams:** Always draw the Decision Tree structure and the SVM Hyperplane.
* **Practice Numericals:** Be ready to calculate Entropy and Gain for a small table.