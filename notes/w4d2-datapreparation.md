<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 16 - Data preparation

- Raw data is dirty and noisy
- MAchine learning algorithms have certain constraints regarding input data
- Transformations can improve the model performance.

## Sklearn modeling flow

```py
from sklearn import SomeModel

mdl = Model()
mdl.fit(X_train,y_train)
mdl.score(X_test,y_test)
mdl.predict(X_new)
```

## Duplicates

### Data leakage

Happens when duplicate data appears both in training and test datasets.
It can cause unreliable results.
The whole point of having a test dataset is not to have it in the training data.

## Missing data

Missing data does not always mean lack of information.

Common reasons:

- Programming error
- Measurement failure
- Random events

Representation:

- NaN
- Large negatives
- ?
- Infinity

### Handle missing data

Do missing values represent an event?
Can I afford to lose data?

### Suggestions

- If $>30%$ of values are missing: potential drop.
- If $<30%$ of values missing: replace for a value that makes sense.

The approximation creates **noise**.

`SimpleImputer`: tool to replace missing values.

- `imputer.fit()` stores the strategy value as an attribute.
- `imputer.transform()` identifies and replaces missing values with the strategy calculated in the `fit()`step.

The tool is called **transformer**

## Outliers

Data points which deviate from the rest of data.

Common reasons:

- Data entry errors
- Measurement errors
- Manipulation or processing errors
- Novelties (not errors)

### Detect outliers

Using `boxplot`.
Using `min`.

### Handle outliers

We have to fully comprehend what an outlier is before removing it.

## Feature scaling

Transforming continuous features to a common, smaller range.
Not all numerical values have to be continuous.

- Features with large values outweigh features with small values.
- Scaling improves computational efficiency
- Increase interpretability of feature coefficients

### Standardizing

$z-score = z = \dfrac{(x - mean)}{std}$

We can use sklearn `StandardScaler`

- It is the _most effective_ when data is **normally distributed**.
- Sensitive to _outliers_.
- Can distort relative distances.
- Corrects skewness

### Normalizing (MinMax Scaling)

$X' = \dfrac{X - X_{min}}{X_{max} - X_{min}}$

Compress feature values between [0, 1]

We can use sklearn `MinMaxScaler`

- Ensures a _fixed range_
- Efficient regardless of distribution
- Does not reduce outlier affection
- Does not correct skewness

### Robust scaling

$RobustScaled = \dfrac{(x - median)}{IQR}$

Scales using central tendency metrics.

We can use sklearn `RobustScaler`

- Less sensitive to outliers

## Dataset balancing

The number of datapoints representing each class is often unequal or imbalanced.

It is good to balance beacuse ML algorithms learn by example.
Will predict under-represented classes poorly.

### Balancing strategies

- Oversampling minority
- Undersampling majority
- Computation of new minority classes.

Over-sampling can cause _data leakage_.

_Synthetic Minority Over-sampling TEchnique (SMOTE)_ creates new data in the same space.

:rotating_light: Only use balancing techniques on the training set.

## Encoding

Transofrming non-numerical data to a numerical form.

### Label Encoding

`LabelEncoder()`

### Feature Encoding

`OneHotEncoder()`

Label Encoding creates a false relation of order between features.

## Discretizing

Process of turning continuous data into discrete data using bins.

`pd.cut()`

```py
data['SalePriceBinary'] = pd.cut(x = data['SalePrice'], bins=[data['SalePrice'].min()-1, data['SalePrice'].mean(),
data['SalePrice'].max()+1], labels=['cheap', 'expensive'])
```

Above it splits Prices in two bins `cheap` and `expensive`

## Feature creation

- Create additional information

Feature engineering.

## Feature selection

Process of eliminating non-informative features.

_Garbage in, garbage out_: Poor quality input will induce noise and destabilize the model.
_Curse of dimensionality_: Not observing enough data
Reducing complexity:

- Feature correlation (univariate)
- Feature permutation (multivariate)

### Feature correlation

High correlation means redundant information.

## Modelling

## Feature permutation

Evaluates the importance of each feature in predicting the target.

sklearn `permutation_importance`

## Reducing complexity

Reducing the number of features.

## Prepare test set

Whatever strategies we take on our _training set_, we have to do exactly the same to the _test set_
