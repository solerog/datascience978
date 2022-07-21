<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 7 -Data visualization

## Matplotlib

Import module

```py
import matplotlib.pyplot as plt
```

Plot some data, save chart using `.savefig()`.

```py
years_x = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
total_y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]
plt.plot(years_x, total_y)
plt.savefig('carbon.png')
plt.show()
```

```py
years_x = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
total_y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]
total_z = [243, 543, 619, 831, 960, 310, 415, 270, 918]
plt.plot(years_x, total_y)
plt.plot(years_x, total_z)
# Displays one plot with two lines on it.
plt.show()
```

### Title

```py
plt.title('Title')
```

### Axis labels

```py
plt.xlabel('Year')
plt.ylabel('CO2 - M of tons')
```

### Axis ticks

```py
plt.xticks([1975, 1995, 2015], ['start', 1995, 'end'])
plt.yticks([0, 5000])
```

### Axis limits

By default they start with `0`.
It sets the beginning and end of the axis values.

```py
plt.xlim(right=, left=) # both arguments optional
plt.ylim(right=, left=) # both arguments optional
```

### Legends

Enable or disable series names.
There are many location options, `best` by default.

```py
plt.legend(loc='best')
```

### Grid

Can specifiy an `axis` (`x` or `y`). Both by default.
Also `linewidth`.

```py
plt.grid(linewidth='0.5') # Both axis
plt.grid(axis='x', linewidth='0.5') # Just x axis
```

### Style

```py
# Print options available
print(sorted(plt.style.available))

plt.style.use('seaborn') # Changes all charts' styles
```

It usually changes all charts' styles.
If we only want one chart to be affected.

```py
with plt.style.context('dark'): # Only this chart's style is changed
    plt.plot(years_x, years_y, label='Total')
    plt.plot(years_x, years_z, label='Other')
    plt.legend(loc='best')
    plt.show()
```

### Lines

`color`, `marker`, `linestyle`, `linewidth`.
We can see all the options in the documentation (`shift`+`tab`).

```py
plt.plot(years_x, years_y, color='#999', linestyle=':', marker='o', linewidth=2)
```

### Figsize

It accepts a tuple of measures (`width`, `height`)

```py
plt.figure(figsize=(16,4))
```

### Complete example

```py
plt.figure(figsize=(10,5))

# 3 lines plot
plt.plot(years_x, total_y, label='total', c="grey", ls=':', marker='s')
plt.plot(years_x, coal_y, label='coal')
plt.plot(years_x, gas_y, label='gas')
# Decoration
plt.legend()
plt.title('CO2 emissions from electricity production - US')
plt.ylim((0,3000))
plt.ylabel('MtCO2/yr')
plt.grid(lw=0.5)

plt.show()
```

### Axes vs axis

**Axis** are the axis of the plot (x, y, z, ...)
**Axes** is the area of the plot.

Useful for finetuning and customizing.

```py
plt.plot(years_x, total_y)
ax = plt.gca() # Saves the entire plot
```

#### AX Title

#### AX Spines

Customizing the axis line

```py

```

### Subplots

Plotting more than one chart in the same figure.
Rows and columns of the same figure can be defined. Each subplot will use one position.

Example:

```py
# Start a figure
plt.figure(figsize=(10,3))
# First subplot
plt.subplot(1,2,1) # 1 row, 2 columns, the plot will use the first position.
plt.plot(years_x, coal_y, label="coal")
plt.plot(years_x, gas_y, label = "gas")
plt.title('coal vs. gas')
plt.legend()
# Second subplot
plt.subplot(1,2,2) # 1 row, 2 columns, the plot will use the second position.
plt.plot(years_x, total_y, label="total", c='black')
plt.title("all energies")
# Global figure methods
plt.suptitle('US electricity CO2 emissions')
plt.show()
```

#### Best practices

```py
# Destructuring initialization. Creates a new figure with 1 row, 2 columns.
fig, axs = plt.subplots(1, 2, figsize=(10,3)) # axs is a (1,2) nd-array

# First subplot
axs[0].plot(years_x, coal_y, label="coal")
axs[0].plot(years_x, gas_y, label = "gas")
axs[0].set_title('coal vs. gas')
axs[0].legend()
# Second subplot
axs[1].plot(years_x, total_y, c='black')
axs[1].set_title('all energies')
# Global figure methods
plt.suptitle('US electricity CO2 emissions')
plt.show()
```

```py
# Destructuring initialization. Creates a new figure with 3 row, 3 columns.
fig, axs = plt.subplots(3, 3, figsize=(10,3)) # axs is a (3,3) nd-array
# First row
axs[0]
axs[1]
axs[2]
# Second row
axs[3]
axs[4]
axs[5]
# Third row
axs[6]
axs[7]
axs[8]
```

### Pandas

We can do the same thing with pandas `DataFrames`.

```py
import pandas as pd
df = pd.DataFrame({ 'coal': coal_y, 'gas': gas_y }, index=years_x)
ax = df.plot();
ax.set_title('CO2 Emission from Electricity Production (US)')
ax
```

Example:

```py
df1 = pd.DataFrame({ 'coal': coal_y, 'gas': gas_y }, index=years_x)
df2 = pd.DataFrame({ 'total': total_y }, index=years_x)
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
df1.plot(ax=ax1)
df2.plot(ax=ax2)
```

:warning: There are two `plot` methods. One for `pandas`, one for `matplotlib.pyplot`. They return different things.

### Plot types

#### Scatter

Type of plot using Cartesian coordinates `(x,y)`.
One of the most important graphs to understand _correlation_.

```py
plt.scatter(data['views'], data['likes'])
```

#### Bar plot

Useful for comparison, and time-series analysis.

```py
# Python
plt.bar(years_x, years_y)
# Pandas
df.plot(kind='bar')
```

#### Histogram

Accurate representation of the data distribution.

```py
plt.hist(x, bins=100)
```

## Seaborn

```py
import seaborn as sns
```

Compare it to `matplotlib`.

```py
plt.figure(figsize=(14, 4))

plt.subplot(1, 2, 1)
plt.title('Matplotlib')
plt.hist(tips_df['total_bill'])

plt.subplot(1, 2, 2)
plt.title('Seaborn')
sns.histplot(tips_df['total_bill'], kde=True);
```

### Histogram

For one numeric value.

```py
sns.histplot(tips_df['total_bill'], kde=True)
```

### Countplot

For one categorical value (string).
Counts how many records there are for unique values of the data we send.

```py
# Count smoker 'yes' or 'no'
sns.countplot(x='smoker', data=tips_df);
```

```py
# Count smoker 'yes' or 'no' depending on 'dinner' or 'lunch'
sns.countplot(x='time', hue='smoker', data=tips_df);
```

### Catplot

One numeric value and one categorical (string)
Has 4 different options: `bar`, `box`, `violin` or `boxen`.

```py
sns.catplot(x='day', y='total_bill', kind='')
```

#### Boxplot

Best plot to check data distribution.
Shows median, second quartile, third quartile.

```py
sns.catplot(x='day', y='total_bill', kind='')
```

### Scatterplot

For two numeric variables.

```py
sns.scatterplot(x="total_bill", y="tip", data=tips_df);
```

### Regression

For two numeric variables.

```py
sns.regplot(x='total_bill', y='tip', data=tips_df)
```

### Full example with 3 numeric and 1 categorical variables in 1 graph

```py
plt.figure(figsize=(10, 7))
sns.scatterplot(x="total_bill", y="tip", hue='smoker', size="size",
                palette=sns.color_palette(["#2ecc71", "#e74c3c"]),
                sizes=(10, 300), data=tips_df)
```

### Facet grid

Plot graph by groups

```py
# Create a grid
g = sns.FacetGrid(tips_df, col="time", row="smoker", hue="smoker")
# Plot a graph in each grid element
g.map(sns.histplot, "total_bill");
```

### Pair plot

Distributions between columns.

```py
sns.pairplot(tips_df, height=2)
plt.show()
```

## Plotly

Interactive charts.
A bit heavy to run on webapps.

```py
import plotly.express as px
```
