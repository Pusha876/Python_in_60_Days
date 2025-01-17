# Data Analysis and Visualization Theory


1. Insight Needs
1. Data Acquisition
1. Data Analysis *(exploratory phase)*
1. Data Visualization *(exploratory phase)*


---

### Data Frames Definitions:
**.loc** - In Jupyter Notebooks, ```.loc``` is a method used with Pandas DataFrames to access and manipulate data based on labels.

**len** - In Jupyter Notebooks, ```len``` is the same as in Python. It's a built-in function that returns the number of items in an object, such as:
* **Strings:** Returns the number of characters in the string.
* **Lists:** Returns the number of elements in the list.
* **Tuples:** Returns the number of elements in the tuple.
* **Dictionaries:** Returns the number of key-value pairs in the dictionary.

**.squeeze** - In Jupyter (specifically when working with Pandas). ```.squeeze()``` is a method used to reduce the dimensionality of a DataFrame or Series object when it has ony one element along a particular axis.

***Here's how it works:***

**For DataFrames:**

* If a DataFrame has only one column, ```.squeeze('columns')``` will convert it into a Series.
* If a DataFrame has only one row, ```.squeeze('index')``` will convert in t into a Series.
* If a DataFrame has only one row and one column, ```.squeeze()``` (without any arguments) will return a scalar value.
