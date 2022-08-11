<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 21 - Ensemble Methods

## Decision Trees

Hierarchical supervised learning algorithms.

- Classification and regression
- Non-linear modeling
- Data breakdown with binary decisions

### `DecisionTreeClassifier`

The depth of a tree is the number of levels except the leaves.

#### Gini index

Measures the ability of each feature to _separate data_.
It is the **impurity** of the node. The lower `Gini` the better.
$$Gini(node) = 1 - \sum{p^2_i}$$
$p_i$ is the ratio between observation in class $i$ and the total number of observations remaining.

#### Tree formation

1. Root Node contains the entire dataset.
2. Try various combinations of _features & threshold_. Each combination splits dataset in two _child_ nodes.
3. For each combination compute **Gini index** of both child nodes.
4. Select the combo _features & threshold_ with the lowest **Gini index** (purest).
5. Split dataset in two using this rules.
6. Repeat step 2 for each subset.
7. Stop if no feature improves node impurity.

#### Predicting

A new point is passed through the tree from top to bottom until it reaches a leaf.

Trees are not _calibrated_ classifiers.

Decision trees are **orthogonal** classifiers.

### `DecisionTreeRegressor`

Goal is to predict continuous values.
The method to grow a tree is different than for `DecisionTreeClassifier`

#### Tree formation

1. Select a `threshold`.
2.

Control overfitting:

- Decision trees must be _tuned_.

#### `min_samples_split`

Minimum number of samples in a node

#### `min_samples_leaf`

Minimum number of samples in a leaf

#### `max_depth`

Max level of nodes

### Variance illustrated

### Pros & cons

👍 No scaling necessary
👍 Resistant to outliers
👍 Intuitive and interpretable
👍 Allows feature selection
👍 Non-linear modeling

👎 High variance
👎 Long training time
👎 Splits data orthogonally

## Bagging (Bootstrap aggregating)

Parallel ensemble method.
Reduces variance.
Each version of the model is called **weak learner**.

### Pros & Cons

👍 Reduces variance
👍 Applied to any model

👎 Complex structure
👎 Long training time

## Boosting

Sequential ensenmble method.

### AdaBoost (Adaptative Boosting)

Assign every observation $x_i$ an initial weight.
Train a weak model (most often a decision tree).

## Gradient boosting

Only implemented for trees

1. Recursively fit each weak learner to predict the residuals of the previous one.
2. Add all the predictions

### XGBoost

Optimized library.
Needs a train set and validation set.

```py
from xgboost import XGBRegressor
xgb_reg = XGBRegressor(max_depth=10, n_estimators=100, learning_rate=0.1)
xgb_reg.fit(X_train, y_train,
    # evaluate loss at each iteration
    eval_set=[(X_train, y_train), (X_val, y_val)],
    # stop iterating when eval loss increases 5 times in a row
    early_stopping_rounds=5
)
y_pred = xgb_reg.predict(X_val)
```

### Pros & Cons

👍 Reduces bias
👍 Strong sub-models have more influence in final decision

👎 Computationally expensive
👎 Easily overfits
👎 Sensitive to outliers

## Stacking

Train different estiamtors and aggregate predictions.

### Simple aggregation
