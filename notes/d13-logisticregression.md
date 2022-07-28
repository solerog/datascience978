<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 13 - Decision Science - Logistic regression

**Linear regression** is _not the best_ idea to predict a _discrete value_.

Logistic regression is used to predict a _binary outcome_.

## Predict a binary outcome

Win or loss, success or failure.
One_star or five_star.

We're trying to fit a `sigmoid function`.
$\dfrac{1}{1+e^{-(\beta_0+\beta_1X_1+...+\beta_nX_n)}}$

We set a `classification threshold`. ($0.5$ by default).
If prediction result is above $0.5$ then $1$, if below $0$.

$\hat{y} > 0.5 = 1$
$\hat{y} < 0.5 = 0$

## Find best fitting $\beta$

We can move the `sigmoid function` over the `x-axis`.
$y$ is the value we want to predict.
$\hat y$ is the prediction.

Ideally we want $\hat y_i$ close to 1 if $y_i = 1$ and $(1 - \hat y_i)$ close to 1 if $y_i = 0$.

The line that minimizes the error is not the Linear regression.

**Likelihood $L(\beta)$**: product of all predictions using $\hat y_i$ if 1, $(1 - \hat y_i)$ if 0.
The closer the **likelihood** to 1 the better.
**Likelihood** is even more sensitive to outliers than _SSR_

If the prediction is good we say that is _calibrated_.

The logarithm
Logit space. Between -$\infty$ and +$\infty$

The _odds_ of an event are $\dfrac{p}{1-p}$

```py
p = np.arange(0.01, 1, 0.005)
odds = p / (1-p)
plt.plot(p, odds);
```

Logit space is the log of the odds.

```py
plt.plot(p, np.log(odds));
plt.grid()
plt.scatter(0.9, np.log())
```

Probability space is the `sigmoid function`. From 0 to 1.
Logit space goes from -$\infty$ to +$\infty$.

### Reading coefficients

We want to know the probability of a given person to survive.

```py
model = smf.logit(formula='survived ~ 1', data=titanic)
```

`smf.logit` returns the log of the odds. Can be negative if most results are 0.

coeff = $log(\dfrac{p}{1 - p})$
odds = exp(log_odds)
probability = odds / (1 + odds) = 38%

```py
cross_tab = pd.DataFrame(
  'count': titanic['survived'].value_counts(),
  'pct': titanic['survived'].value_counts(normalize=True)
)
```

```py
model=smf.logit(formula='survived ~ fare', data=titanic).fit()
model.params
# Intercept -0.941
# fare       0.015
```

_Intercept_ is the probability with 0 features.
The coefficient is the log.

coeff = 0.015
odds = exp(0.015) = 1%

The log of the odds of surviving for a passenger who paid nothing is -0.94

coeff = -0.94
odds = exp(-0.94) = 0.39
prob = odds / (1 + odds) = 71%

### Using categorical

```py
model2 = smf.logit(formula='survived ~ C(pclass)', data=titanic).fit()
model2.params
# Intercept         0.530628
# C(pclass)[T.2]   -0.639431
# C(pclass)[T.3]   -1.670399
```

Now the _intercept_ is represented by a person of the first class. It is the _log of the odds_ for the first class.
The next coefficients are related to the first class, the are not the log of the odds for that class, only the relation with the first class.
_This only applies to categorical values_.
$-0.63$ is the decrease in the log-odds for the second class of survival related to the intercept.

$log(odds_2) - log(odds_1) = -0.63$
$log(\dfrac{odds_2}{odds_1}) = -0.63$
$\dfrac{odds_2}{odds_1} = exp(-0.63)$

```py
log_odds_2 = -0.639431 + 0.530628
odds_2 = np.exp(log_odds_2)
proba_2 = odds_2 / (1 + odds_2)
```

### With multiple features

```py
model2 = smf.logit(formula='survived ~ fare + C(sex) + age', data=titanic).fit()
model2.params
# Intercept         0.934841
# C(sex)[T.male]   -2.347599
# fare              0.012773
# age              -0.010570
```

The intercept is a `female` with 0 fare and 0 age.

Holding fare and age constant, being a male in Titanic reduces the log-odds of surviving by 2.35

### Evaluate performance

`Pseudo-r-squared`

If $P>|z| < 0.05$ in the summary we can reject the null hypothesis.
If $P>|z| > 0.05$ the feature is not statistically significant.

`p-value` represents the probability if a value to belong to a distribution.
The higher the $z$ the lower the $P>|z|$

## Inference

`p_values` work similarly to Linear Regression
`z-score` are used instead of `t-score`.

## Goodness-of-fit ($R^2$ or equivalent?)

We calculate the `log-likelihood (LL)`.

`Pseudo R-squared` $1 - \dfrac{LL(predict)}{LL(mean)}$

`Pseudo R-squared` between 0, 1.
Useful to compare models predicting the same problem for same data.
Not as descriptive as R-squared.

## Multicolinearity issues

Problem that occurs if one column is dependant from one or more columns.
This means you can't hold other values constant and we cannot trust the coefficients, as they are volatile.

We have to use the `rank` of the matrices.
The feature matrix needs to be `full rank`.

Example:

```py
mpg = sns.load_dataset('mpg').dropna().drop(columns=['origin', 'name', 'displacement'])
mpg.corr().style.background_gradient(cmap='coolwarm')
```

In the summary you get warnings for multicolinearity.
We may not know which are the columns affected by colinearity.
You cannot trust `coefficients` nor `p-values`.

Filter numerical values

```py
mpg.select_dtypes(exclude=['bool','object'])
```

If there is noise in the linear combination column, we cannot detect it.

### VIF: Variance inflation factor

$VIF(X_k) = \dfrac{1}{1-R^2_k}$

The higher $VIF$ the stronger the colinearity.

To calculate $VIF$ he have to scale all features, except the target.

A high value is considered over 10.

```py
dropped = mpg.drop(columns=['weight'])
mpg_scaled = (dropped - dropped.mean()) / dropped.std()
```

```py
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
df = pd.DataFrame()
df["features"] = mpg_scaled.columns
df["vif_index"] = [vif(mpg_scaled.values, i) for i in range(mpg_scaled.shape[1])]
round(df.sort_values(by="vif_index", ascending = False),2)
```
