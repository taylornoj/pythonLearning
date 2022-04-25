# Pandas
[ notes from LHL 21DDC ]

**Descriptive statistics** = brief descriptions that summarize datasets

A library we use to get descriptive statistics from numerical datasets is **Pandas**

## Using Pandas

Pandas library is external to base Python so it needs to be imported:

```python
import pandas as pd 

list_of_num = [1,2,3,4,5]

series = pd.Series(list_of_num)
#converting our list_of_num to a pandas series variable
#we need to do this to use some of pandas' useful descriptive statistics functions
```

In the 21DDC we are loading data from another doc

```python
import pandas as pd
df = pd.read_csv('fc_barcelona.csv')
#pd.read_csv() reads the path to a .csv files and stores it in a Pandas DataFrame (representation of data in a table)
df.head() 
#df.head() will give the first five rows
df.tail()
# displays bottom five rows of a dataframe, however adding a number in () will display the corresponding number of rows from the bottom
```
![image of data](https://github.com/taylornoj/pythonLearning/blob/main/docs/E88F879C-A7C3-4FA4-9AE5-8DFD86BBE232.jpeg?raw=true)

Then we create variables for different data in the table:

```python
points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna()
```

And we use those to find answers to our challenge questions:

What is the maximum amount of games Barcelona playes in 1 season?
```python
print(games_played.max())
```

What is the average attendance across the seasons?
```python
print(attendance.mean())
```

What is the difference between median value of wins and losses?
```python
print(wins.median() - losses.median())
```

What is the minimum number of games Barcelona managed to win in 1 season?
```python
print(wins.min())
```
What is the difference between max and min amount of points Barcelona was able to get in all seasons?
```python
print(points.max() - points.min())
```

## Functions
series.max()    #outputs maximum value in Pandas Series

series.min()    #outputs minimum value in Pandas Series

series.mean()   #outputs average value in Pandas Series

series.median() #outputs median value in Pandas Series

series.mode()   #outputs mode value in Pandas Series

***
## Challenge 8 with Paris Landmarks
![image of paris landmark data](https://github.com/taylornoj/pythonLearning/blob/main/docs/F6CDC0F9-FAD6-4230-926F-3A3FCDA3AA65_4_5005_c.jpeg?raw=true)

## More Functions to choose from
**DataFrame Functions**

```df.describe()``` provides descriptive statistics of all numerical columns

```df.unique()``` provides the number of unique items in a column

```df.shape()``` gets the number of rows and columns in the dataframe

```df.sort_values()``` sorts the dataframe by specific column [example ```df.sort_values(by=['column_name'], ascending = False)```]

**DataFrame Column Functions**

```.info()``` provides an overview of all the columns, number of non-nulls, and data types in a DataFrame [example ```df.info()```]

```.max()``` gets the max value from a column [example ```df['column_name'].max()```]

```.min()``` gets the min value from a column

```.mean()``` get the mean value from a column

```.idxmax()``` gets the integer index position of the max value from a column

```.idxmin()``` gets the integer index position of the min value from a column

```.loc()``` gets rows (or columns) with particular labels from the index

```.iloc()``` gets rows (or columns) with particular positions in the index (only takes integers)

So to answer today's questions:

What is the most expensive landmark in Paris?
```python
df.sort_values(by="price",ascending=False)
```

What is the average wait time for all landmarks?
```python 
df['queue_time'].mean() 
```
***

## Challenge 9 - Data Filtering
A two step process where 1) we are creating a boolean condition that works as a filter and 2) we pass the data through the filter

```python
#Example - Loading Data
user_filter = pd.read_csv('wine.csv')
df.head()

#Step 1: Create filter
user_filter = df['Alcohol'] >= 14

#Step 2: Feed the filter to the original DataFrame and store the result in a new variable
filtered_df = df[user_filter]

#Step 3: Display Variable
filtered_df
````

You can also combine step 1 and 2 in one step:
```python
# Step 1 and 2
filtered_df_2 = df[df['Alcohol'] >= 14]
```

Finally, use ```len()``` to see how many rows the DataFrame has.

My example from Challenge 9:
How many wines are there in class 3?

```python
import pandas as pd
df = pd.read_csv('wine.csv')
filtered_df_2 = df[df['Class'] == 3]
print(len(filtered_df_2)) # prints 48
```

***

## Challenge 10 - Group By in Pandas
group by function:
- groups the dataset according to catagorical column or columns
- grouping function can't stand on its own - user needs to apply a specific aggregate function to the dataset after using group by

Example:
```python
import pandas as pd

df = pd.read_csv('dubai_properties_data.csv', index_col = 0)

df.groupby(['quality']).mean()
# group dataset by quality column, then use mean() function to see the average of all numerical columns for each year
```

Other aggregate functions to use on group bys:
- count() – Number of non-null observations
- sum() – Sum of values
- mean() – Mean of values
- median() – Arithmetic median of values
- min() – Minimum
- max() – Maximum
- mode() – Mode
- std() – Standard deviation
- var() – Variance
- size() - Number of rows

You can also specify the columns we want to group by:
```df.groupby(['quality'])[['price','size_in_sqft','no_of_bedrooms']].mean()```
or
```df.groupby(['view_of_landmark','view_of_water'])[['price','no_of_bedrooms']].mean()```

Finding the neighbourhood with highest average price:
```python
grouped = df.groupby('neighborhood')[['price','size_in_sqft']].mean()
grouped.sort_values('price',ascending=False).head(1)
```

Finding the neighbourhood with highest average size_in_sqft:
```python
grouped.sort_values('size_in_sqft',ascending=False).head(1)
```
***
## Challenge 11 - Advanced Group By Uses in Pandas

wWhat if we wanted to apply different functions to different columns? Do we need to do each column individually? If you think there’s a more efficient way, you’re correct. Pandas has a better way.

```python
import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')

# old way - averages of both columns were computed for each neighborhood
df.groupby(['neighborhood'])[["price","price_per_sqft"]].mean()

# new way - using the aggregate function .agg()
df.groupby(['neighborhood']).agg({'price' : 'mean', 'price_per_sqft' : 'max'})
```

*.agg()* is used to select the aggregation we want to do for each column.  

We use a Python dictionary as a parameter of the .agg() function.  The keys are the column names and the values are functions we want to apply.

You can do two aggregations in one column:
```df.groupby(['neighborhood']).agg({'price' : ['mean','max']})```

*The Challenge:*
![challenge 11](https://github.com/taylornoj/pythonLearning/blob/main/docs/A8505081-638E-472F-B6D4-949BE0EB74D2_4_5005_c.jpeg?raw=true)

Using the functions described above, which neighborhood has the biggest difference between maximum and minimum property price?

```python
grouped = df.groupby('neighborhood').agg({'price':['min','max']})
grouped.head()
```

![challenge 11 result from .agg func](https://github.com/taylornoj/pythonLearning/blob/main/docs/807ED0F5-5332-45F0-B0D7-563D74758550_4_5005_c.jpeg?raw=true)

```python
(grouped.iloc[:,1] - grouped.iloc[:,0]).sort_values(ascending=False).head()
```

.iloc[] is primarily integer position based (from 0 to length-1 of the axis) but may also be used with a boolean array

So in this example we took the max [:,1] and took away the min [:,0] then sorted values to find neighbourhood with largest difference
```
neighborhood
Palm Jumeirah               34375112
Business Bay                30470000
Jumeirah                    26300000
Downtown Dubai              18688888
Jumeirah Beach Residence    14110000
```


***
## Challenge 12 - stack and unstack

```python
import pandas as pd

# we define the dataframe
df = pd.DataFrame([[25.69, 7692000], [5.084, 268021]],
            index=['Australia', 'New  Zealand'],
            columns=['population', 'area'])

# we apply the function stack()
stacked = df.stack()

print(stacked.index)
```
The stack() function stacks both columns into one, and creates something we call a MultiIndex.

You can think of MultiIndex as an array of tuples where each tuple is unique

A MultiIndex can be created from a list of arrays (using MultiIndex.from_arrays()), an array of tuples (using MultiIndex.from_tuples()), a crossed set of iterables (using MultiIndex.from_product()), or a DataFrame (using MultiIndex.from_frame()). 


***
## Challenge 13 - 

import pandas as pd
df = pd.read_csv('aus_weather.csv')
df_date = df.set_index("Date")
df_date.head()
df_date[df_date['Location'] == 'Melbourne']["Temp9am"].hist(edgecolor="black", linewidth=1.2)