<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 5 - Data Analysis

## Jupyter

Open-source web application.

```sh
cd <path_to_folder>
jupyter notebook
```

Once open you cannot move one level up, only from that folder forward.

Each element is a cell.

### Code cell

The last expression is the one that is printed, unless a `print()` statement exists.

We can run terminal commands in code cells adding `%%bash` in the beginning

### Markdown cell

Displays formatted markdown language.

### Raw NBConvert cell

Cell for information. Not usually used.

## Numpy

Python module for high-performance data manipulation.

```py
import numpy as np
```

Inside a _Jupyter Notebook_, you can press _tab_ after np to see all the possible methods. Once a methos is selected, you can press _shift+tab_ iinside the parenthesis to see the method implementation.

```py
l = [[1, 2, 3], [4, 5, 6]]
l[0][2] # 3
type(l) # list
```

In Numpy we can do operations to full arrays

```py
A = np.array(l)
A[0] # array([1, 2, 3])
A[0] * 2 # array([2, 4, 6])
```

NumPy is much faster than Python, around two orders of magnitude.

### ndarray

**N-dimension Array**.

- Multidimensional
- Homogenous data
- Has a fixed size since creation

#### Methods

`.ndim()`:
`.shape()`:
`.size()`:
`.dtype()`:

#### Slicing

**Slicing general syntax** `ndarray[start:stop:step]`

Second row from first to third columns.
In pure Python:

```py
l[2][1:4]
```

In NumPy:

```py
A[2, 1:4]
```

We can check the time of execution for a cell adding `%%time` in the beginning.

#### Vectorized Operations

```py
my_list = [
    [6, 5],
    [1, 3],
    [5, 6],
    [1, 4]]
A = np.array(my_list)
my_sum = A[:,0] + A[:,1] # Vectorial "+" operator
my_sum
```

##### Axis

Can be used for _ndarray_ calculations.

```py
np.sum(A, axis=0) # sum of rows
np.sum(A, axis=1) # sum of cols
```

#### Boolean indexing

We can compare _ndarrays_ and get a boolean index _ndarray_

```py
A = np.array(np.arange(0, 3), np.arange(3, 6), np.arange(6, 9))
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
A > 3 # [[False, False, False], [False, True, True], [True, True, True]]
A[A > 3] = 0 # [[0, 1, 2], [3, 0, 0], [0, 0, 0]]
```

## Pandas

```py
import pandas as pd
```

### Series

Equivalent to _1D ndarray_.
Supports multiple data types.

Two ways of defining a series:

```py
s = pd.Series(data=[1,2,'three'], index=['id1', 'id2', 'id3'])
s = pd.Series({'id1': 1, 'id2': 2, 'id3': 'three'})
```

#### Methods

`.value_counts()`: Counts the occurences of each value.
`.unique()`: Returns a list of unique values

### DataFrames

Equivalent to _2D ndarrays_ with labels in both axes and multiple data types.
_DataFrames_ are dictionaries of _Series_

Default names are `0` to `n`.

```py
df = pd.DataFrame(
    [[4, 7, 10],
     [5, 8, 11],
     [6, 9, 12]],
    index=['row_1', 'row_2', 'row_3'],
    columns=["col_a", "col_b", "col_c"]
)
```

```py
apples  = pd.Series(data=[1, 2, 3], index=["id1", "id2", "id3"])
oranges = pd.Series(data=[4, 5, 6], index=["id1", "id2", "id3"])
d = {
    "apples": apples,
    "oranges": oranges,
}
pd.DataFrame(d)
```

If indexes do not match, an entry is created for each index with `NaN` value in the non-existing values for the indexes.

To convert a df column to a _Series_

```py
series = countries_df['Country'] # Shape is (227,)
new_df = countries_df[['Country']] # Shape is (227,1)
```

#### Merge & Join

You can use `.merge()` when you want to merge based on a given column and `.join()` when you want to join on the index.

#### Methods

`.describe()`: Gives you statistical data for each column. `count`, `mean`, `standard deviation`, `min`, `max`, ...
`.nunique()`: Tells you how many unique values there are per column.
`.info()`: Tells you column data types and non-null counts for each column.
`.isnull()`: returns True or False for each value if value is null. Can be combined with sum `.isnull().sum()` to see the count of null values for each column.
`.shape()`: Returns a tuple with the number of rows and columns.
`.head()`: Displays first rows
`.tail()`: Displays last rows
`.setindex()`: Sets the name of a row. More below.
`.iloc()`:
`.str`: Converts to string
`.dtypes`: Column data types

Percentage of null values per column

```py
countries_df.isnull().sum() / countries_df[0] * 100
```

#### Boolean indexing

Countries with over 1 billion people.

```py
countries_df[countries_df["Population"] >= 1_000_000_000]
```

Countries that belong to America.

```py
american = countries_df['Region'].str.contains('AMER')
countries_df[american]
```

Countries in europe

```py
countries_df[countries_df["Region"].isin(["WESTERN EUROPE", "EASTERN EUROPE"])]
```

#### Set index

You can set indexes inplace (same df) or not.

```py
countries_df['Country'] = countries_df['Country'].map(str.strip)
countries_df.set_index('Country', inplace=True)
```

#### Sorting

_DataFrames_ can be sorted by indexes and/or values:

```py
countries_df.sort_index(ascending=False)
countries_df.sort_values(by='Population', ascending=False)
```

#### Grouping

Works like `GROUP BY` in _SQL_

```py
regions = countries_df.groupby('Region')
regions[['Population', 'Area (sq. mi.)']].sum()
regions.agg(['mean', 'count', 'max', 'min', 'median', 'std'])
regions[['Population', 'Area (sq. mi.)']].sum() \
    .sort_values('Population', ascending=False)
```

### Read files

_Pandas_ has methods for reading files and translate them to _DataFrames_.
Decimal separator can be defined.

```py
countries_df = pd.read_csv(countries.csv, decimal=",")
```

## Plotting

Import matplotlib

```py
%matplotlib inline
import matplotlib
```

```py
gdp = 'GDP ($ per capita)'
top_ten_countries_df = countries_df[[gdp]] \
    .sort_values(gdp, ascending=False) \
    .head(10)
top_ten_countries_df
top_ten_countries_df.plot(kind="bar")
```
