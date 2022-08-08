<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 09 - Statistics & probabilities

## Packages

```py
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import math
import scipy
import scipy.stats as stats
```

## Introduction

_Statistics_ gives the possibility to quantify uncertainty.

## Statistical work

- Data analysis
- Probability
- Inference

## Descriptive statistics

- Discover underlying patterns
- Represent data
- Summarize data

```py
male_df = pd.DataFrame([140, 145, 160, 190, 155, 165, 150, 190, 195, 138, 160, 155, 153, 145, 170, 175, 175, 170, 180, 135, 170, 157, 130, 185, 190, 155, 170, 155, 215, 150, 145, 155, 155, 150, 155, 150, 180, 160, 135, 160, 130, 155, 150, 148, 155, 150, 140, 180, 190, 145, 150, 164, 140, 142, 136, 123, 155],
    columns=['weight'])
male_df['sex'] = 'male'
female_df = pd.DataFrame([140, 120, 130, 138, 121, 116, 125, 145, 150, 112, 125, 130, 120, 130, 131, 120, 118, 125, 135, 125, 118, 122, 115, 102, 115, 150, 110, 116, 108, 95, 125, 133, 110, 150, 108],
    columns=['weight'])
female_df['sex'] = 'female'

weights_df = pd.concat([male_df, female_df], ignore_index=True)
weights_df.sample(5)
```

### Histogram

Represents the distribution of numerical data.
It is an estimate of the probability distribution.

**Histrogram** is useful for _continuous values_.

## Summary statistics

Useful statistic data

- Location / central tendency (**mean**)
- Statistical dispersion / spread (**variance**)
- Shape of the distribution (**skewness**). Assymetry. Can be _right-skewed_ or _left-skewed_
- Linear **correlation**

:warning: It is not the same working with the entire population than with a sample of the population.

### Mean

Average value

### Median

Middle value. The value that separates the set into two equal smaller subsets.
More robust against outliers.

### Mode

Value that appears most often.
The peak of the distribution.

### Skewness

- Positive / Right (mode < median < mean)
- Symmetrical (mode = median = mean)
- Negative / Left (mode > median > mean)

## Statistical dispersion

### Variance $\sigma^2$

Sum of the difference between the value and the mean, squared.

### Standard deviation $\sigma$

Square root of variance
The formula changes for a sample. It is divided by $n-1$ instead of $N$ (Bessel's correction)

### Interquartile range $IQR$

Difference between upper and lower quartiles.
$IQR = Q_3 - Q_1$

Used to identify outliers.
Outliers are $<Q_1 - 1.5IQR$ or $>Q_3 + 1.5IQR$

In python we can get data summary using

```py
weights_df.describe()
```

### Correlation $\rho$

Linear correlation.

$\rho = -1$ means all values belong to a negative slope regression.
$-1<\rho<0 $ means values are correlated in a negative slope regression.
$\rho = 0$ means no correlation at all.
$0<\rho<1 $ means values are correlated in a positive slope regression.
$\rho = 1$ means all values are correlated in a positive slope regression.

The closer it gets to -1 or 1 the better correlation.

If two variables are _independent_, you will get a $\rho=0$.
But if you get $\rho=0$ does not mean that values are _independent_.

## Probability

$P(A)$ is a value between $0$ and $1$
$P(A^C) = 1 - P(A)$
$P(\bar A) = 1 - P(A)$

Operations:

- Union
- Intersection
- Complement
- Substraction
- Partition

### Union (or)

All the elements in two sets $A\cup B$

### Intersection (and)

All the elements that belong to both sets. $A\cap B$

### Complement

All the elements not belonging to the set. $A^C$

### Sample space $S$

Set of all possible outcomes.

If you toss a coin 3 times, the $S$ is the set of possible outcomes.
$S={(H,H,H), (H,H,T), (H,T,H), ..., (T,T,T)}$

_Permutations_ outcomes if you care about order.
_Combinations_ outcomes if you _do not_ care about order.

### Conditional probability

$P(B|A)$ is the _conditional probability_ of $B$ given $A$. Also noted as $P_A(B)$

Probability of drawing a king $P(A) = \dfrac{4}{52}$
$P(B|A) = \dfrac{3}{51}$

They are dependant

#### Bayes' Theorem

$P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}$

:bulb: [False positive paradox](https://en.wikipedia.org/wiki/Base_rate_fallacy#False_positive_paradox)

## Random variable

**Random variables** are specific numerical values of a random experiment.
For example, number of shots, shots on goal, yellow cards and red cards in a soccer match.

A random variable $X$ is a function from $S$ to $\R$.
$X$ as the number of _heads_ tossing a coin 2 times. $Range(X) = {0,1,2}$

### PMF Probability Mass Function

$X$ = Number of heads
$S={(H,H),(H,T),(T,H),(T,T)}$

### Expected value

For a random variable, the average value if you run the experiment a large number of times.

In this case $1$.

### Bernoulli process

Repeated sequence of binary random variables.

```py
np.random.binomial(n=1, p=0.3, size=10)
```

## Normal distribution

### Probability Density Function (PDF)

```py
def plot_normal_distribution(mu, variance):
    sigma = math.sqrt(variance)
    x = np.linspace(-10, 10, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), label=f"μ={mu}, σ²={variance}")

plot_normal_distribution(0, 1)
plot_normal_distribution(1, 2)
plot_normal_distribution(-3, 5)
plt.legend()
plt.show()
```

99.7% of data is inside $|3\sigma|$
95% of data is inside $|2\sigma|$
68% of data is inside $|\sigma|$

The entire area of PDF $=1$

### Cumulative Distribution Function (CDF)

```py
def plot_cumulative_normal_distribution(mu, variance):
    sigma = math.sqrt(variance)
    x = np.linspace(-10, 10, 100)
    plt.plot(x, stats.norm.cdf(x, mu, sigma), label=f"μ={mu}, σ²={variance}")

plot_cumulative_normal_distribution(0, 1)
plot_cumulative_normal_distribution(1, 2)
plot_cumulative_normal_distribution(-3, 5)
plt.legend()
```

## Central Limit theorem

### Z-score

How far a point is in terms of a standard deviation.
How many standard deviations is the value far from the mean.
$Z=0$ is equal to the mean
$Z=1$ value is $\sigma$ away (above or below) from the mean
