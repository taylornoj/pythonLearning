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

