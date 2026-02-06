Classification and prediction are essential techniques in data mining, widely applied in industries like finance, healthcare, and marketing to tackle challenges such as fraud detection and customer targeting.
The difference lies in their approach: classification in data mining assigns data to predefined categories (e.g., spam detection), while prediction estimates continuous values (e.g., stock price forecasting).

There are two forms of data analysis that can be used for extracting models describing important classes or to predict future data trends. These two forms are as follows −
1) Classification
2) Prediction

Classification models predict categorical class labels; and prediction models predict continuous valued functions. For example, we can build a classification model to categorize bank loan applications as either safe or risky, or a prediction model to predict the expenditures in dollars of potential customers on computer equipment given their income and occupation.

# **What is classification?**
Classification is a technique in data mining that involves categorizing or classifying data objects into predefined classes, categories, or groups based on their features or attributes. It is a supervised learning technique that uses labelled data to build a model that can predict the class of new, unseen data. It is an important task in data mining because it enables organizations to make informed decisions based on their data. For example, a retailer may use data classification to group customers into different segments based on their purchase history and demographic data. This information can be used to target specific marketing campaigns for each segment and improve customer satisfaction.

**Classification techniques can be divided into categories**
1) binary classification and multi-class classification. Binary classification assigns labels to instances into two classes, such as fraudulent or non-fraudulent. 
2) Multi-class classification assigns labels into more than two classes, such as happy, neutral, or sad.

![ClassificationsTypes](../imgs/ClassificationsTypes.png)

**Steps to Build a Classification Model**
There are several steps involved in building a classification model, as shown below -
➜ Data preparation - The first step in building a classification model is to prepare the data. This involves collecting, cleaning, and transforming the data into a suitable format for further analysis.
➜ Feature selection - The next step is to select the most important and relevant features that will be used to build the classification model. This can be done using various techniques, such as correlation, feature importance analysis, or domain knowledge.
➜ Prepare train and test data - Once the data is prepared and relevant features are selected, the dataset is divided into two parts - training and test datasets. The training set is used to build the model, while the testing set is used to evaluate the model's performance.
➜ Model selection - Many algorithms can be used to build a classification model, such as decision trees, logistic regression, k-nearest neighbors, and neural networks. The choice of algorithm depends on the type of data, the number of features, and the desired accuracy.
➜ Model training - Once the algorithm is selected, the model is trained on the training dataset. This involves adjusting the model parameters to minimize the error between the predicted and actual class labels.
➜ Model evaluation - The model's performance is evaluated using the test dataset. The accuracy, precision, recall, and F1 score are commonly used metrics to evaluate the model performance.
➜ Model tuning - If the model's performance is not satisfactory, the model can be tuned by adjusting the parameters or selecting a different algorithm. This process is repeated until the desired performance is achieved.
➜ Model deployment - Once the model is built and evaluated, it can be deployed in production to classify new data. The model should be monitored regularly to ensure its accuracy and effectiveness over time.

**Syntaxes Used**
Here are some common notations and syntax used for classification in data mining -
➜ X - Input data matrix or feature matrix, where each row represents an observation or data point, and each column represents a feature or attribute.
➜ y - Output or target variable vector, where each element represents the class label or target variable for the corresponding data point in X.
➜ p(y|x) - Probability of class y given input x.
➜ θ - Model parameters or coefficients that are learned during the training process.
➜ J(θ) - Cost function that measures the overall error or loss of the model on the training data and is typically a function of the model parameters θ.

# **Categorization of Classification in Data Mining**
There are different types of classification algorithms based on their approach, complexity, and performance. Here are some common categorizations of classification in data mining -
➜ Decision tree-based classification - This type of classification algorithm builds a tree-like model of decisions and their possible consequences. Decision trees are easy to understand and interpret, making them a popular choice for classification problems.
➜ Rule-based classification - This type of classification algorithm uses a set of rules to determine the class label of an observation. The rules are typically expressed in the form of IF-THEN statements, where each statement represents a condition and a corresponding action.
➜ Instance-based classification - This type of classification algorithm uses a set of training instances to classify new, unseen instances. The classification is based on the similarity between the training instances' features and the new instances' features.
➜ Bayesian classification - This classification algorithm uses Bayes' theorem to compute the probability of each class label given the observed features. Bayesian classification is particularly useful when dealing with incomplete or uncertain data.
➜ Neural network-based classification - This classification algorithm uses a network of interconnected nodes or neurons to learn a mapping between the input features and the output class labels. Neural networks can handle complex and nonlinear relationships between the features and the class labels.
➜ Ensemble-based classification - This classification algorithm combines the predictions of multiple classifiers to improve the overall accuracy and robustness of the classification model. Ensemble methods include bagging, boosting, and stacking.

**Following are the examples of cases where the data analysis task is Classification −**
> A bank loan officer wants to analyze the data in order to know which customer (loan applicant) are risky or which are safe.
> A marketing manager at a company needs to analyze a customer with a given profile, who will buy a new computer.

In both of the above examples, a model or classifier is constructed to predict the categorical labels. These labels are risky or safe for loan application data and yes or no for marketing data.

**Real-Life Examples**
There are many real-life examples and applications of classification in data mining. Some of the most common examples of applications include -
➜ Email spam classification - This involves classifying emails as spam or non-spam based on their content and metadata.
➜ Image classification - This involves classifying images into different categories, such as animals, plants, buildings, and people.
➜ Medical diagnosis - This involves classifying patients into different categories based on their symptoms, medical history, and test results.
➜ Credit risk analysis - This involves classifying loan applications into different categories, such as low-risk, medium-risk, and high-risk, based on the applicant's credit score, income, and other factors.
➜ Sentiment analysis - This involves classifying text data, such as reviews or social media posts, into positive, negative, or neutral categories based on the language used.
➜ Customer segmentation - This involves classifying customers into different segments based on their demographic information, purchasing behavior, and other factors.
➜ Fraud detection - This involves classifying transactions as fraudulent or non-fraudulent based on various features such as transaction amount, location, and frequency.

# **Classification Vs. Regression in Data Mining**
Regression in data mining is a supervised learning technique that models the relationship between a dependent (target) variable and one or more independent (predictor) variables to predict continuous numerical values, like sales, prices, or temperatures. It works by fitting a line or curve to data points, finding the best fit to forecast future outcomes, understand variable impact, and identify trends, with common types including linear, logistic, and polynomial regression.  


![Classification Vs. Regression](../imgs/ClassVSRegra.png)

| Factor                  | Classification                                                                                       | Regression                                                                                   |
|-------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **Task / Objective**    | Predicting a **categorical** class label for a new instance based on its features                    | Predicting a **continuous** (or sometimes discrete numeric) value based on features          |
| **Outcome Type**        | Categorical (class label / category)                                                                 | Continuous / numeric                                                                         |
| **Typical Evaluation**  | Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix                                     | MSE, RMSE, MAE, R², Correlation coefficient                                                 |
| **Key Algorithms**      | - Decision Trees (ID3, CART)<br>- Naive Bayes<br>- SVM<br>- KNN<br>- Neural Networks (Backpropagation) | - Linear Regression<br>- Polynomial Regression<br>- Regression Trees<br>- Neural Networks   |
| **Real-world Examples** | - Email spam detection<br>- Disease diagnosis<br>- Sentiment analysis<br>- Customer churn prediction | - House price prediction<br>- Sales forecasting<br>- Temperature prediction<br>- Stock price estimation |

# **Issues in Classification and Regression Techniques**
Classification and regression are two important tasks in data mining. They involve predicting a new observation's class label or numeric value based on its features or attributes. Here are some issues related to regression and classification in data mining -
➜ Data quality - The accuracy and effectiveness of classification and regression techniques heavily depend on data quality. Noisy, incomplete, or inconsistent data can lead to poor classification or regression models.
➜ Overfitting - Overfitting occurs when a classification or regression model is too complex and fits the training data too closely, leading to poor performance on new, unseen data. To address overfitting, various techniques such as regularization, early stopping, and cross-validation can be used.
➜ Bias - Bias refers to the tendency of a model to make errors in its predictions consistently. This can happen if the model is too simple or lacks enough data to learn from. It is also called the underfitting of ML models.
➜ Imbalanced data - In classification, imbalanced data occurs when one class label is much more prevalent than the others, leading to biased classification. To address imbalanced data, various techniques such as resampling, cost-sensitive learning, and ensemble methods can be used.
➜ Interpretability - Interpretability refers to the ability to understand and explain the decisions made by a classification or prediction model. Some methods, such as decision trees, linear regression, logistic regression, etc., are more interpretable than others, such as neural networks, support vector machines, etc.

# **What is prediction?**
Prediction is the act of forecasting or estimating a future event or outcome based on current knowledge, data, or trends. It involves making informed guesses or projections about what is likely to happen in the future. Predictions can be made using a variety of methods, including statistical analysis, machine learning models, expert judgment, and historical data analysis.

**The process of making a prediction typically involves the following steps:**
➜ Data Collection: Gathering relevant data that can inform the prediction. This data can come from various sources such as historical records, real-time sensors, market trends, or expert opinions.
➜ Analysis: Analyzing the collected data to identify patterns, correlations, or trends that can be used to make a prediction. This analysis can be done manually or with the help of advanced tools like statistical software or machine learning algorithms.
➜ Modeling: Developing a predictive model that can process the data and generate an estimate of the future outcome. The model may rely on mathematical equations, simulations, or artificial intelligence techniques to make its predictions.
➜ Evaluation: Assessing the accuracy and reliability of the prediction by comparing it with actual outcomes, when possible. This step is crucial for refining the predictive model and improving future predictions.
➜ Decision-Making: Using the prediction to guide decisions and actions. Whether in business, science, or everyday life, predictions are valuable tools for planning and risk management.

**Predictions are widely used in various fields, including:**
➜ Meteorology: Predicting weather patterns to inform the public and guide agricultural activities.
➜ Finance: Forecasting stock prices, currency exchange rates, and economic trends to inform investment decisions.
➜ Healthcare: Predicting disease outbreaks, patient outcomes, and the effectiveness of treatments.
➜ Sports: Anticipating the outcomes of games or the performance of athletes based on past performances and statistical analysis.
➜ Technology: Predicting the future behavior of systems, such as software performance or user behavior in digital platforms.

**Following are the examples of cases where the data analysis task is Prediction −**
Suppose the marketing manager needs to predict how much a given customer will spend during a sale at his company. In this example we are bothered to predict a numeric value. Therefore the data analysis task is an example of numeric prediction. In this case, a model or a predictor will be constructed that predicts a continuous-valued-function or ordered value.

> Note − Regression analysis is a statistical methodology that is most often used for numeric prediction

# **How Does Classification Works?**
With the help of the bank loan application that we have discussed above, let us understand the working of classification. The Data Classification process includes two steps −
➜ Building the Classifier or Model
➜ Using Classifier for Classification

**Building the Classifier or Model**
➜ This step is the learning step or the learning phase.
➜ In this step the classification algorithms build the classifier.
➜ The classifier is built from the training set made up of database tuples and their associated class labels.
➜ Each tuple that constitutes the training set is referred to as a category or class. These tuples can also be referred to as sample, object or data points.

![build_classifier](../imgs/dm_build_classifier.jpg)

**Using Classifier for Classification**
In this step, the classifier is used for classification. Here the test data is used to estimate the accuracy of classification rules. The classification rules can be applied to the new data tuples if the accuracy is considered acceptable.

![using_classifier](../imgs/dm_using_classifier.jpg)

**Classification and Prediction Issues**
The major issue is preparing the data for Classification and Prediction. Preparing the data involves the following activities −
➜ Data Cleaning − Data cleaning involves removing the noise and treatment of missing values. The noise is removed by applying smoothing techniques and the problem of missing values is solved by replacing a missing value with most commonly occurring value for that attribute.
➜ Relevance Analysis − Database may also have the irrelevant attributes. Correlation analysis is used to know whether any two given attributes are related.
➜ Data Transformation and reduction − The data can be transformed by any of the following methods.
    ➜ Normalization − The data is transformed using normalization. Normalization involves scaling all values for given attribute in order to make them fall within a small specified range. Normalization is used when in the learning step, the neural networks or the methods involving measurements are used.
    ➜ Generalization − The data can also be transformed by generalizing it to the higher concept. For this purpose we can use the concept hierarchies.


# **Comparison of Classification and Prediction Methods**
Here is the criteria for comparing the methods of Classification and Prediction −
➜ Accuracy − Accuracy of classifier refers to the ability of classifier. It predict the class label correctly and the accuracy of the predictor refers to how well a given predictor can guess the value of predicted attribute for a new data.
➜ Speed − This refers to the computational cost in generating and using the classifier or predictor.
➜ Robustness − It refers to the ability of classifier or predictor to make correct predictions from given noisy data.
➜ Scalability − Scalability refers to the ability to construct the classifier or predictor efficiently; given large amount of data.
➜ Interpretability − It refers to what extent the classifier or predictor understands.




