<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 12 - Decision Science - Linear regression

## Statistical Inference

Hypothesis testing

- `p-value`
- $\alpha = 0.05$ significance level

Central Limit Theorem

- z-test for normal distributions
- t-test for student distribution

Bayesian approach

- $posterior ~ prior * likelihood$

## Visual approach (seaborn)

`mpg` seaborn dataset

```py
mpg.describe().apply(lambda x: round(x))
sns.scatterplot(x='horsepower', y='weight', data=mpg)
sns.regplot(x='horsepower', y='weight', data=mpg)
```

Interpretation
:ok: Powerful cars seem heavier

```py
round(mpg.corr(),2)
```

### R-Squared $R^2$

Is the explanation of the variance.
A low $R^2$ means high variance, but a bad $R^2$ dies not mean unuseful data.
$R^2$ is the percentage of how much the model is better than calculating the `mean`.
$R^2 = 1$ best case scenario
$R^2 = 0$ simple `mean`
$R^2 < 0$ worst than simple `mean`

```py
(mpg.corr()['weight']['horsepower']) ** 2
```

```py
sns.heatmap(round(mpg.corr(),2), cmap='coolwarm')
```

### Ordinary Least Square (OLS)

Linear Regression is very sensitive to outliers.

### Confidence interval

When measuring a sample, how much confident we can be that the sample results can describe the whole population results.

## Calculation (`statsmodels`)

Two ways to use `statsmodels`

```py
import statsmodels.api as sm

Y = mpg['weight']
X = mpg['horsepower']
model = sm.OLS(Y, X).fit() # Finds best beta
model.predict(X) # Y prediction (regression line)
```

```py
import statsmodels.api.formula as smf
model = smf.ols('weight ~ horsepower', data=mpg)
print(model.params)
```

horsepower 19 means for each 1 horsepower increased, the weight increases 19 kg.

```py
model.rsquared() # 0.747
```

The weight change can be explained in a 75% by the horsepower.

```py
model.summary()
```

$R^2$
F-statistic means if this model is statistical significant. Represents the combined `p_value` of all the coefficients.
$Skew$

### std err

$\dfrac{1}{\sqrt{n}}\dfrac{\sigma residuals}{\sigma horsepower}$

**Null hypothesis**: `horsepower`is not correlated with `weight`.

As `p-value` is much lower than the significance value $0.05$.

## Asusmptions for inferential analysis

- Random sampling
- Independant sampling (sample with replacement, n < 10% population)

Residuals is the difference between the predicted value and the actual value.

_Heteroscedasticity_: the variance increases with the number of ?.

## OLS using 2 dimensions

The result is a hyperplane.

```py
model2 = smf.ols(formula='weight ~ horsepower + cylinders', data=mpg).fit()
model2.params
```

## Partial regression plots

```py

```

## Categorical values

```py
# Use C(variable)
model3 = smf.ols(formula='weight ~ C(origin)', data=mpg).fit()
model3.params
```

```py
# Use C(variable). We can remove the intercept
model4 = smf.ols(formula='weight ~ C(origin) - 1', data=mpg).fit()
model4.params
```

## Cheat sheet

$R^2$ -> Check the goodness of the fit.
`p-values` and `F-statistic` -> Check statistical significance
