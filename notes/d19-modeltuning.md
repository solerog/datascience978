<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 19 - Model tuning

$X$ = features
$y$ = target = $h(X, \beta) + error$
$h$ = hypothesis function (Linear Regression, Logistic Regression, ...)

$\beta$ = model parameters

- computed automatically when `.fit()` by minimizing $L(\beta)$

**Hyperparameters** of the model

- $L(\beta)$ = loss function (MSE, MAE, RMSE, Log-loss)
- loss parameters (learning rate $\eta$, eta0, ...)
- solver = method to minimize $L$ (newton, sdg, ...)
- model-specificities ($n$-neighbours, kernel, ...)

## Model complexity

High **bias**: Model does not capture all the information in the data. Caused by low degree solutions.
High **variance**: Model does not generalize well with new datapoints. Includes noise inside functions.

### Bias-Variance tradeoff

One of the most important concepts in datascience.
$TotalError = Bias^2 + Variance + IrreducibleError$

The _optimal model complexity_ is the one that minimizes **TestError** no an unseen dataset.
We can use _learning curves_ to see that.

Diagnose using a **Validation set** and use **cross-validation** instead of single holdout.

### Solutions for _overfitting_

- Get more observations
- Feature selection
- **Regularization** of _Loss function_
- Dimensionality reduction
- Early stopping

## Regularization

Adding a **penalty term** that increases with $\beta$
$RegularizedLoss = Loss(X, y, \beta) + Penalty(\beta)$

- Penalize large values for $\beta_i$
- Forces model to shrink coefficients or select less features.
- Prevents overfitting.

### Ridge $L2$

**Penalty** is sum of $\beta$ squares.

$$Ridge = Loss + \alpha \sum^n_{i=1} \beta^2_i$$

### Lasso $L1$

**Penalty** is the sum of $\beta$ absolute values.

$$Lasso = Loss + \alpha \sum^n_{i=1} |\beta_i|$$

New **hyper-parameter** $\alpha$
Defines how much the model is **regularized**
Large $\alpha$ forces **model complexity** to **decrease**. A very high $\alpha$ leads to a **high bias**.

Sum starts when $i=1$, intercept is not penalized.

- Increasing $\alpha$ in $Ridge$ will only shrink parameters **towards $0$**.
- Increasing $\alpha$ in $Lasso$ can shrink parameters **to $0$**

### ElasticNet (Lasso & Ridge weighted average)

2 hyper-parameters to fine tune $(\alpha, \lambda)$

**Regularization** penalizes features that are **not statistically signifficant**. This means, features with **high p-values**.

### When to regularize

- **Regularize** if you think you are **overfitting** (Learning curves not converging)
- **Ridge** if all coefficients might have an impact.
- **Lasso** as a feature selection tool (better for interpretability)

✅ **Regularization** is almost always appropiate.

## Model tuning

How to choose the best hyper-parameters.

### Grid search method

1. Holdout a validation set
2. Select which grid of values for hyper-parameters to try out
3. Measure performance for each combination of values.
4. Select the hyper-params with the best performance.

❌ Computationally costly
❌ The optimal hyperparameter can be missed
❌ Can overfit hyperparameters to the training set if too many combinations are tried out.

### Random search

Randomly explore hyperparatemer values

Use `random search` if:

- Want to try many values. Less typing.
- Control the number of combinations

Always start with a **coarse grain** approach, then **fine-tune**.

🔥
**Fit** = find best **params** to minimize **loss**.
**Finetune** = find best **hyperparams** to maximize **performance metrics**

## Support Vector Machines (SVMs)

Decision boundaries for classification.

⚠️ All SVMs require **scaling**

The **hyperplane** that generalizes best to unseen data is the one that maximizes the **margin** (is furthest from all the points)
The points on the margin are called **support vectors**.

**Maximum margin classifier**:

- Super sensitive to outliers
- Overfits training data.

### Soft Margin classifier

Allows a few points to be misclassified with a penalty ($\xi$)

**Hinge Loss** is the penalty applied to each point on the wrong side. The deeper inside, the higher the loss.

### Regularization hyperparameter `C`

Strength of the penalty applied.
The higher `C` the stricter the **margin**.

### SVM Regressorss

The trick is to reverse the objective.
Instead of having a hyperplane with ideally no data inside to split classes. We want a hyperplane with all points inside, to predict new values.

## SVM Kernels

Adding new features (**feature mapping**) so data becomes separable.
Can become computationally expensive.

### Kernel trick

Each time the Loss function is calculated, its also calculated a **Kernel**, a **similarity** $K(a, b)$ between all pairs of datapoints.

### SVM Kernel lists

Specify the type of **feature mapping** to be used to make data **linearly separable** again.

- `linear`
- `poly`
- `rbf`
- `sigmoid`
