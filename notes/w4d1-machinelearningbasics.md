<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 15 - :robot: Machine Learning fundamentals

## What is Machine Learning

Area of computational science that focuses on analyzing and interpreting patterns.

- Constantly and rapidly evolving.

Can be divided in `supervised` and `unsupervised` learning.

### Supervised

Develop predictive models based on both _input_ and _output_ data.

#### Classification vs Regression

`Regression`: Calculate a number
'Classification`: Calculate a categorical output.

### Unsupervised

Develop predictive models based on both _input_ and _output_ data.

### Jargon

_Features_ can also be _input_, _X's_

## Sklearn modeling flow

1. Import model `from sklearn import model`
2. Instantiate the model `model = model()`
3. Train the model `model.fit(X, y)`
4. Evaluate the model `model.score(new_X, new_y)`
5. Make predictions `model.predict(new_X)`

## Holdout method

Always evaluate the performance with data that has not been used in the training.

- Train set ($\approx70\%$)
- Test set ($\approx30\%$)

### Drawbacks

- The data in Test is not used to train the model
- If th dataset is small, the loss can be significant

### K-Fold Cross Validation

Dataset is split into K folds
For each split a _sub model_ is trained and scored
The `average score` of all _sub models_ is the **cross-validated** score of the model.
It does not output a _trained model_

#### Choosing K

- Tradeoff between performance evaluation and cmoputational expense.

As a rule of thumb $K = 5$ or $10$

### Bias / variance tradeoff

- _Bias_ (underfitting): The algorithm is basic and does not learn the patterns of the dataset.
- _Variance_ (overfitting): The algorith, generates overly complex relationships modelling patterns.

It is better to make _assumptions_ to avoid Bias and Variance.

### Learning curves

Plot of scores of training and validation sets while increasing the size of the training set.

As training set size increases:

- Training score will decrease
- Test score will increase
- Curves will converge (not always!)

In _underfitting_ we get low scores on both training and test sets, but the learning curves might converge.
In _overfitting_ both curves do not converge.

Ideally we should have a _high score_ on both curves and a convergence.
