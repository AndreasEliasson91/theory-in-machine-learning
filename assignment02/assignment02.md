# Assignment 02 - Theory in Machine Learning
This is the second assignment for the course _Theory in Machine Learning_<br>
The assignment is to analyse a flower data set, and create clusters from the data using the K-Means Algorithm.<br><br>
Like the previous assignment, I'm using __Python__, but this time also libraries such as __Pandas__, __NumPy__, __SciKit-Learn__ and __Seaborn__.<br>

# The Assignment:
### For a passing grade:
Handle and analyse the iris data set from the SciKit-Learn library, containing data about different iris flowers.<br>
Every data point contains four attributes:
- _sepal width_
- _sepal length_
- _petal width_
- _petal length_

<br>The assignment is to experiment and analyse the data set and answer some questions about the results.
I will present the result in a __Jupyter Notebook__ and a report as a __PDF__, as well as the code I tested in my __IDE__.
<br><br>

### Questions to answer
- #### Analysis of the data set
  - How many data points are there?
  - What is the distribution for all attributes?<br>
- #### Explain the K-Means Algorithm
- #### By run two attributes at a time through the algorithm, answer the following:
  - How many clusters the most logical to use?
  - Which attributes are the best to use, if only two attributes are allowed?
  - Show the clusters you created

### For a higher grade:
This is divided into two sub parts. The first is based on the previous iris data set and the second one is based on a data set from a __CSV__-file.<br>
#### First part:
The data points has four attributes, therefore is it impossible to visualize them in a plane.
Use a Principal Component Analyze tool to transform them to two dimensions.
- #### Use all attributes from the data set and cluster them with the K-Means Algorithm
  - How many clusters is the most logical to use?
  - Does the number of clusters differ from before, when only two attributes where used?
- #### Show your created clusters

<br>

#### Second part:
Use the data set from the _special_iris.csv_-file (you need to unzip it to the data directory) and analyze the data.
- #### Analysis of the data set
  - How many data points are there?
  - How many attributes contains each data point of?
- #### Use all attributes from the data set and cluster them with the K-Means Algorithm
  - Time the algorithm. How much does the time differ between this data set and the basic iris data set?
  - Why does the time differ?

<br>

_24/03 2022_
Assignment for the Theory in Machine Learning course - Teknikhögskolan