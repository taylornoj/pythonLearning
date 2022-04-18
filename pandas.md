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