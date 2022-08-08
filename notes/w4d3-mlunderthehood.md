<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 18 - Under the hood

_Loss functions_ and _solver optimizer_.

## Behind `.fit()`

A model can be expressed as $y = h(X, \beta) + error$

### Loss Function $L$

`.fit()` minimizes $L(error)$

$$\beta = arg \min_\beta L(\beta, X, y, h)$$

There exist numerours `solvers` to minimize $L(\beta)$.

The most basic iterative method is **Gradient Descent**

## Gradient Descent

It uses the **slope** of the **Loss function** as an indicator.
As the **slope** approaches $0$, the **Loss function** approaches its `minimum`.

### 1D Descent

1. Initialize a random parameter. $\beta_0 = n$
2. Calculate the derivative of the **Loss Function** at that point.
3. Move a step in the _opposite direction_ of the derivative. The step size is **proportional** to derivative value and a chosen **Learning rate** $\eta$
   $$\beta_0^{(k+1)} = \beta_0^{(k)} - \eta\dfrac{\partial L}{\partial \beta_0}(\beta_0^{(k)})$$
   This is called **epoch**.
4. Go back to step `2.`

As the **Loss** approaches the `minimum` the derivative gets smaller and so do the steps.
It stops with different **stopping criterions**.

- `Minimum step size`: When the step size is smaller, stop and get the value as the optimal value.
- `Maximum number of steps`: Number of **epochs**

### 2D Descent

We can reiterate the same procedure for both parameters at the same time.

The _energy landscape_ is in 3D.

There can be many dimensions in a problem.

### Vectorial formulation

1. Start with random values $\beta_0$, $\beta_1$, ..., $\beta_n$
2. At each **epoch** $k$ update both in the appropiate direction.

### Effect of learning rate $\eta$

Small learning rate:

- ✅ Shorter path to minimum
- ❌ Requires more epochs
- ❌ Sensible to local minima

Large learning rate:

- ✅ Requires less epochs
- ❌ May never converge

## Other solvers

**Gradient descent** is computationally expensive.

### Minibatch gradient descent

1. Choose minibatch size (16 or 32 are common).
2. Compute gradient of the minibatch
3.

### Stochastic Gradient Descent (SGD)

Loop one by one over all observations.

SGD is less stable as it works on a single point instead of the average.

- ✅ Faster for very large datasets
- ✅ Jumps out of local minima
- ✅ Reduces RAM load
- ❌ Needs more epochs
- ❌ Never exactly converges
- ❌ Slower for small datasets with many features

When to use:

- Dataset population $n$ over 1 M.
- By default

In `sklearn` exist `SGDRegressor` which is a `Linear Regression` that uses **SGD** and `SGDClassifier` is a `Logistic Regression` that uses **SGD**.

## Loss functions

_Squared Loss_ is not the only function we can use.

```py
SGDClassifier(loss='log')
SGDClassifier(loss='hinge')
```

### Loss $\not ={}$Performance Metrics

Performance metrics are computed **after** the model is fitted.

Performance metrics:

- MSE
- RMSE
- RMSLE
- MAE
- $R^2$

Classification metrics:

- Accuracy
- Precision
- Recall
- F1

Loss is usde to fit the model.

### Regression Loss Functions

Huber Loss is a mix of L1 (MAE) and L2 (MSE)

### Classification Losses

Log Loss (Cross Entropy Loss)
