# Unit-1: Data Mining Introduction – Detailed Lecture Notes  
**Topic: Data Objects & Attribute Types (with Examples)**  
**Course: 21CSE355T - Data Mining and Analytics**  
**Reference:** Jiawei Han & Micheline Kamber, "Data Mining: Concepts and Techniques", 3rd Edition, Chapter 2 (Getting to Know Your Data)  

**Objective:** By the end of this lecture, students will be able to:  
- Define **data objects** and explain their role in datasets  
- Classify and describe all major **types of attributes** with real-world examples  
- Understand the **operations allowed**, **distance/similarity measures**, and **differences** between attribute types  
- Appreciate why attribute types matter in preprocessing, similarity calculation, and algorithm selection  

## 1. Introduction – Why Study Data Objects & Attribute Types?

Before we mine data, we must **understand the data**!  
- Data is not just numbers — it's **entities** (objects) described by **characteristics** (attributes).  
- Wrong understanding of attribute types → Wrong preprocessing, wrong distance measures → Poor mining results (e.g., using Euclidean distance on gender = disaster!).  

**Key Terms:**  
- **Data Object** (also called: instance, sample, example, tuple, record, data point) → Represents a real-world **entity**  
- **Attribute** (also called: feature, variable, dimension, field) → Describes a **characteristic/property** of the data object  

**Real-life Analogy:**  
Think of a student database:  
- Each **row** = one student = **data object** (entity)  
- Each **column** = attribute like name, roll no., gender, marks, etc.  

## 2. What is a Data Object? 

Data sets are made up of data objects. A data object represents an entity.
In a sales database, the objects could be customers, store items, or sales, for instance. In a medical database, the objects may be patients. In a university database, the objects could be students, professors, and courses. Data objects are typically described by attributes. Data objects can also be referred to as samples, examples, instances, data points, or objects. If the data objects are stored in a database, they are data tuples. That is, the rows of a database correspond to the data objects, and the columns correspond to the attributes.

**Definition:**  
A **data object** is an entity (person, place, thing, event) in the dataset that is described by a set of attributes.  
In a database, data objects correspond to **rows** (tuples/records), while attributes are **columns**.

**Examples of Data Objects in Different Domains:**

| Domain                  | Data Object (Entity)          | Typical Attributes (Examples)                              |
|-------------------------|-------------------------------|------------------------------------------------------------|
| Sales/Retail            | Customer                      | Customer_ID, Name, Age, Gender, Purchase History           |
| Sales/Retail            | Item/Product                  | Product_ID, Name, Category, Price, Brand                   |
| Sales/Retail            | Transaction                   | Transaction_ID, Date, Customer_ID, Items Bought, Total     |
| Medical/Healthcare      | Patient                       | Patient_ID, Name, Age, Gender, Diagnosis, Treatment        |
| University/Education    | Student                       | Roll_No, Name, Branch, Semester, CGPA, Attendance          |
| University/Education    | Course                        | Course_Code, Name, Credits, Instructor                     |
| Social Media            | User                          | User_ID, Username, Age, Location, Interests                |

**Important Points for Exams:**  
- Data objects are the **basic units** for mining (e.g., we cluster customers, classify transactions, find outliers in patients).  
- In transactional databases → each **basket** is a data object.  
- In relational databases → each **tuple/row** is a data object.

## 3. What is an Attribute? Types of Attributes 

An attribute is a data field, representing a characteristic or feature of a data object. The nouns attribute, dimension, feature, and variable are often used interchangeably in literature. The term dimension is commonly used in data warehousing. Machine learning literature tends to use the term feature, while statisticians prefer the term variable. Data mining and database professionals commonly use the term attribute. We use the term attribute here as well. Attributes describing a customer object can include, for example, customer ID,name, and address. 

The type of an attribute is determined by the set of possible values the
attribute can have. Attributes can be nominal, binary, ordinal, or numeric.
The **type** of an attribute determines:  
- What operations are allowed (e.g., +, −, mean, ranking)  
- Which distance/similarity measures can be used  
- How to preprocess (e.g., normalization, encoding)

**Main Categories:**

### 3.1 Qualitative / Categorical Attributes

#### A. Nominal Attributes  
Nominal means “relating to names.” The values of a nominal attribute are
symbols or names of things. Each value represents some kind of category, code,or state and so nominal attributes are also referred to as categorical. The values do not have any meaningful order about them. In computer science, the values are also known as enumerations.

**Example**: Nominal attributes. Suppose that Hair color and Marital status are two attributes describing person objects. In our application, possible values for Hair color are black, brown blond, red, auburn, grey, and white. Marital status can take on the values single, married, divorced, and widowed. Both Hair color and Marital status are nominal attributes. Occupation is another example, with the values teacher, dentist, programmer, farmer, and so on.

Because nominal attribute values do not have any meaningful order about
them and are not quantitative, it makes no sense to find the mean (average)
value or median (middle) value for such an attribute, given a set of objects. 

**Definition:** Values are **names/symbols/categories** with **no meaningful order** or ranking.  
**Operations allowed:** =, ≠ (equality only)  
**Distance measure:** Simple matching coefficient, Hamming distance  
**Examples:**  
- Color: {red, blue, green, yellow}  
- Gender: {Male, Female, Other}  
- Blood Group: {A+, A-, B+, B-, O+, O-, AB+, AB-}  
- Marital Status: {Single, Married, Divorced, Widowed}  
- Occupation: {Engineer, Doctor, Teacher, Student}  

**Exam Tip:** No arithmetic operations! Cannot say "red > blue".

#### B. Binary Attributes 
A binary attribute is a nominal attribute with only two categories or states:
0 or 1, where 0 typically means that the attribute is absent, and 1 means that it is present. Binary attributes are referred to as Boolean if the two states correspond to true and false.
**Example** Binary attributes. Given the attribute Smoker describing a patient object,1 indicates that the patient smokes, while 0 indicates that the patient does not.
Similarly, suppose the patient undergoes a medical test that has two possible
outcomes. The attribute Medical test is binary, where a value of 1 means the
result of the test for the patient is positive, while 0 means the result is negative.

A binary attribute is symmetric if both of its states are equally valuable and carry the same weight; that is, there is no preference on which outcome should be coded as 0 or 1
**Special case of nominal** — only **two states** (usually 0 & 1)  

**Two Subtypes:**

| Subtype              | Description                                      | Both states equally important? | Example                                      | Distance Measure          |
|----------------------|--------------------------------------------------|--------------------------------|----------------------------------------------|---------------------------|
| Symmetric Binary     | Both outcomes have same importance               | Yes                            | Gender: 0=Male, 1=Female                     | Hamming distance          |
| Asymmetric Binary    | One outcome (usually rare/positive) is important | No                             | Medical test: 0=Negative, 1=Positive (HIV)   | Jaccard coefficient       |

**Real-world:** In fraud detection → 0=normal transaction, 1=fraud → **asymmetric** (fraud is rare & important).

#### C. Ordinal Attributes  
An ordinal attribute is an attribute whose possible values have a meaningful
order or ranking among them, but the magnitude between successive values is
not known.
**Example** Ordinal attributes. Suppose that Drink size corresponds to the size of drinks available at a fast food restaurant. This nominal attribute has three possible
values – small, medium, and large. The values have a meaningful sequence
(which corresponds to increasing drink size), however, we cannot tell from the values how much bigger, say, a medium is from a large. Other examples of
ordinal attributes include Grade (e.g., A+, A, A−, B+, and so on) and Profes-
sional rank. Professional ranks can be enumerated in a sequential order, such
as assistant, associate, and full for professors, and private, private first class,specialist, corporal, sergeant for army ranks.
Ordinal attributes are useful for registering subjective assessments of qual-
ities that cannot be measured objectively. Hence, ordinal attributes are often used in surveys for ratings. In one survey, participants were asked to rate how satisfied they were as customers. Customer satisfaction had the following ordinal categories: 0: very dissatisfied, 1: somewhat dissatisfied, 2: neutral, 3:satisfied, and 4: very satisfied.

Ordinal attributes may also be obtained from the discretization of numeric
quantities by splitting the value range into a finite number of ordered categories

**Definition:** Categorical values with **meaningful order/ranking**, but **difference between ranks is not known/equal**.  
**Operations allowed:** =, ≠, <, >, ranking  
**No arithmetic** (cannot add ranks meaningfully)  
**Examples:**  
- Education Level: {High School, Bachelor, Master, PhD}  
- Satisfaction: {Very Poor, Poor, Average, Good, Excellent}  
- Military Rank: {Private, Sergeant, Captain, Major, Colonel}  
- Size: {Small, Medium, Large, Extra Large}  

**Exam Tip:** We can sort, but cannot say "PhD – Master = Master – Bachelor".

### 3.2 Quantitative / Numeric Attributes
A numeric attribute is quantitative, that is, it is a measurable quantity, represented in integer or real values. Numeric attributes can be interval-scaled or ratio-scaled.

#### D. Interval-Scaled Attributes  
Interval-Scaled Attributes Interval-scaled attributes are measured on a scale of equal-sized units. The values of interval-scaled attributes have order and can be positive, 0, or negative.
Thus, in addition to providing a ranking of values, such attributes allow us to compare and quantify the difference between values

**Example** Interval-scaled attributes. Temperature is an interval-scaled attribute. Suppose that we have the outdoor temperature value for a number of different days,where each day is an object. By ordering the values, we obtain a ranking of the objects with respect to temperature. In addition, we can quantify the difference between values. 
For example, a temperature of 20◦C is 5 degrees higher than
a temperature of 15◦C. 
Calendar dates are another example. For instance, the years 2018 and 2025 are 8 years apart.
Temperatures in Celsius and Fahrenheit do not have a true zero-point, that
is, neither 0◦C nor 0◦F indicates “no temperature.” (On the Celsius scale, for example, the unit of measurement is 1/100 of the difference between the melting temperature and the boiling temperature of water in atmospheric pressure.)
Although we can compute the difference between temperature values, we cannot
talk of one temperature value as being a multiple of another. Without a true
zero, we cannot say, for instance, that 10◦C is twice as warm as 5◦C. That
is, we cannot speak of the values in terms of ratios. Similarly, there is no true zero-point for calendar dates. (The year 0 does not correspond to the beginning of time.) This brings us to the next type of attribute – ratio-scaled attributes,for which a true zero-point exits.

Because interval-scaled attributes are numeric, we can compute their mean
value, in addition to the median and mode measures of central tendency.

**Definition:** Numeric values measured on a **scale with equal intervals**, but **no true zero point** (zero is arbitrary).  
**Operations allowed:** +, −, mean, standard deviation  
**Cannot** say "twice as much" (no ratio).  
**Examples:**  
- Temperature in °C or °F (0°C ≠ absence of temperature)  
- Calendar dates (year 0 is arbitrary)  
- IQ scores  

**Distance:** Euclidean, Manhattan

#### E. Ratio-Scaled Attributes  
A ratio-scaled attribute is a numeric attribute with an inherent zero-point.
That is, if a measurement is ratio-scaled, we can speak of a value as being a
multiple (or ratio) of another value. In addition, the values are ordered, and we can also compute the difference between values. The mean, median, and mode can be computed as well.

**Example** Ratio-scaled attributes. Unlike temperatures in Celsius and Fahrenheit, the Kelvin (K) temperature scale has what is considered a true zero-point (0 degrees K = −273.15◦C): It is the point at which the particles that comprise matter have zero kinetic energy. Other examples of ratio-scaled attributes include Count attributes such as Years of experience (where the objects are employees, for example) and Number of words (where the objects are documents). 
**Additional examples** include attributes to measure weight, height, latitude and longitude coordinates (e.g., when clustering houses), and monetary quantities (e.g., you are 100 times richer with ₹100 than with ₹1).

**Definition:** Numeric values with **equal intervals** + **true zero point** (zero means absence).  
**Operations allowed:** All (+, −, ×, ÷, ratios, mean, geometric mean, etc.)  
**Examples:**  
- Age, Height, Weight, Salary  
- Temperature in Kelvin (0 K = absolute zero)  
- Number of children  
- Income, Distance (km), Time duration (seconds)  

**Distance:** Euclidean, Manhattan, Minkowski

## 4. Summary Table – Quick Revision (Very Important for Exams!)

| Attribute Type       | Category     | Order? | Equal Intervals? | True Zero? | Operations Allowed              | Example                              | Distance Measure             |
|----------------------|--------------|--------|------------------|------------|---------------------------------|--------------------------------------|------------------------------|
| Nominal              | Qualitative  | No     | No               | No         | =, ≠                            | Color, Gender, Blood Group           | Simple matching              |
| Binary (Symmetric)   | Qualitative  | No     | No               | No         | =, ≠                            | Gender (M/F)                         | Hamming                      |
| Binary (Asymmetric)  | Qualitative  | No     | No               | No         | =, ≠ (focus on 1)               | Test Result (Pos/Neg)                | Jaccard                      |
| Ordinal              | Qualitative  | Yes    | No               | No         | =, ≠, <, >, ranking             | Education Level, Satisfaction        | Rank-based                   |
| Interval             | Quantitative | Yes    | Yes              | No         | +, −, mean, std dev             | Temperature °C, Dates                | Euclidean/Manhattan          |
| Ratio                | Quantitative | Yes    | Yes              | Yes        | All (+, −, ×, ÷, ratios)        | Age, Height, Salary, Weight          | Euclidean/Manhattan          |

**Hierarchy of Precision (Exam Point):**  
Nominal < Ordinal < Interval < Ratio  
(More precise → more powerful statistical analysis possible)

## 5. Why Attribute Types Matter in Data Mining? 

- **Preprocessing** → Nominal → One-hot encoding; Ratio → Normalization  
- **Similarity/Distance** → Wrong measure ruins clustering/classification  
- **Algorithm Selection** → Decision trees handle all; KNN needs proper distance  
- **Interpretation** → Cannot compute mean of gender or education level!

## 6. Class Activity + Q&A 

**Quick Questions for Students:**  
1. Is "Pin Code" nominal or ordinal? Why?  
2. Is "Temperature in °C" interval or ratio? Why?  
3. In fraud detection (fraud=1, normal=0), which binary type? Why?  
4. Can we say "PhD is twice as educated as Bachelor"? Why/why not?

**Homework:**  
- Take any real dataset (e.g., from Kaggle) → List 5 attributes & classify their types.  
- Submit next class.

**Motivation Quote:**  
"Know your data before you mine it – attribute types are the DNA of your dataset!"
