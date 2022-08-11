<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 23 - Time Series

## Introduction

Series of repeated observation within a time interval.
Observations are taken at evenly spaced intervals.

DataFrames usually have the `time` on the index.

Auto-regressive approach.

`y = df.values`
`X` is past `y` values.

Each row is `X[t] = y[t-1], y[t-2], y[t-3], ...`

Traditional _holdout_ method cannot be used.

We have to use _contiguous `train_test_split`_

```py
# Let's keep the last 40% of the values out for testing purposes
train_size = 0.6
index = round(train_size*df.shape[0])

df_train = df.iloc[:index]
df_test = df.iloc[index:]
```

### Predict next datapoint

```py
y_pred = df_test.shift(1)
y_pred
```

We can also move backwards

```py
df_test.shift(-1)
```

```py
from sklearn.metrics import r2_score

y_pred = df_test.shift(1).dropna()
y_true = df_test[1:]

print(f"R2: {r2_score(y_true, y_pred)}")
# R2: 0.5069517261286796
```

This means 50% of the variance is explained by the features.

### Linear model with 12 autoregressive features

```py
df2 = df.copy(); df2_train = df_train.copy(); df2_test = df_test.copy()

for i in range(1, 13):
    df2_train[f't - {i}'] = df_train['value'].shift(i)
    df2_test[f't - {i}'] = df_test['value'].shift(i)

df2_train.dropna(inplace=True)
df2_test.dropna(inplace=True)

df2_train.head()
```

```py
X2_train = df2_train.drop(columns = ['value'])
y2_train = df2_train['value']
X2_test = df2_test.drop(columns = ['value'])
y2_test = df2_test['value']

print(X2_train.shape,y2_train.shape, X2_test.shape,y2_test.shape)
```

```py
# Predict and measure R2
model = LinearRegression()
model = model.fit(X2_train, y2_train)

print('R2: ', r2_score(y2_test, model.predict(X2_test)))
pd.Series(model.coef_).plot(kind='bar')
plt.title('partial regression coefficients');
```

For a Time Series, the further it is the value to predict, the lower the $R^2$

## Decomposition

- **Trend**
- **Seasonal** / **Periodic**
- **Irregularities**

```py
from statsmodels.tsa.seasonal import seasonal_decompose
```

### Additive

```py
# Additive Decomposition (y = Trend + Seasonal + Residuals)
result_add = seasonal_decompose(df['value'], model='additive', extrapolate_trend='freq')
result_add.plot();
result_add.trend
```

### Multiplicative

```py
# Multiplicative Decomposition (y = Trend * Seasonal * Residuals)
result_mul = seasonal_decompose(df['value'], model='multiplicative')
result_mul.plot();
```

```py
# Plot the residuals with "result_add.resid" to decide
f, (ax1, ax2) = plt.subplots(1,2, figsize=(13,3))
ax1.plot(result_add.resid); ax1.set_title("Additive Model Residuals")
ax2.plot(result_mul.resid); ax2.set_title("Multiplicative Model Residuals");
```

✅ Multiplicative residuals have **less notion of time**, which is better (in this example).
They are centered in 1.
**`stationarity`**: TS that do not exhibit meaningful statistical over time.

Most methods are designed to work on **stationary TS**

## Stationarity

If time does not influence `mean`, `variance` or `autocorrelation` / `covariance`. All values should be constant.
For a **stationary TS** distribution is not affected by the location of the window.

### Test for stationarity

- Calculate `mean`, `variance` and `autocorrelation`.

**Augmented Dickey Fuller (ADF)** tests the null hypothesis $H_0$

```py
from statsmodels.tsa.stattools import adfuller

adfuller(df.value)[1]  # p-value 1.0
print('additive resid: ', adfuller(result_add.resid.dropna())[1])
# 0.000285
print('multiplicative resid: ', adfuller(result_mul.resid.dropna())[1])
# 1.74726e-07
```

### Achieve stationarity

Decomposition $Y = Y_{trend} + Y_{season} + Y_{resid}$ and predict $Y_{resid}$
Differencing $Y_{diff} = Y_{t} + Y_{t-1}$ and predict $Y_{diff}$

## Autocorrelation

Measures the correlation between $Y(t)$ and a lagged version $Y(t-i)$

### ACF Autocorrelation Graph

```py
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(df.value, lags=50)
plt.show()
```

Autocorrelation measures the **direct** and **indirect** effect of a lagged point in time.

Time Series can be treated as a linear model.

$$Y_t = \alpha + \beta_1Y_{t-1} + \beta_2Y_{t-2} + ... + + \beta_pY_{t-p} + \epsilon_t$$

**Autoregression (AR)** is the linear model of a Time Series.

**Partial correlation function (PACF)** is the analysis of the lag terms. It only measures the direct effect.

```py
from statsmodels.graphics.tsaplots import plot_pacf

plot_pacf(df.value, lags=50, c='r');
```

```py
fig, axes = plt.subplots(1,2, figsize=(16,3))

plot_acf(df.value, lags=50, ax=axes[0]);
plot_pacf(df.value, lags=50, ax=axes[1], color='r');
```

**ACF** is the correlation of the series with itself

- Slow exponential decrease
- $X(t)$ is correlated with $X(t-1)$, which is correlated to $X(t-2)$

**PCF** is more informative

- Removes intermediate correlations

## Moving averages

Predicting next values based on the average value of a specific windows size.

Similar to the **PACF**

| Date | Value | MovWindow(3) | abserror |
| ---- | ----- | ------------ | -------- |

## Auto Regressive Moving Average (ARMA)

Combines two models Auto Regressive (AR) and Moving Average (MA)
$ARMA(p, q)$

- Linear combination of $p$ lags of $Y$
  _plus_
- Linea combination of $q$ lagged forecast errors

$AR: Y_t = \alpha + \beta_1Y_{t-1} + ... + \beta_pY_{t-p} + \epsilon_t$
$MA: Y = \alpha + \phi_1\epsilon_{t-1} + ... + \phi_q\epsilon_{t-q} + \epsilon_t$

Hyperparameters $p$ and $q$
$p$: How many lags we want to incorporate to $AR$
$q$: How many lags we want to incorporate to $MA$

First lag is ignored.
We have to choose the lags before the values drop below the confidence interval.

## Auto Regressive Integrated Moving Average (ARIMA)

$ARIMA(p, d, q)$

Data **must be stationary** to use this model.
We can apply **differencing** to turn our data into **stationary**
More than one **differencing** can be applied.

$I$ uses differencing to achieve stationarity

In the $AR$ process a _shock_ will propagate far. Not necessarily stationary.
In the $MA$ process a _shock_ will have limited effect. Always stationary.
Differencing tends to turn $AR$ processes into $MA$ ones.

```py
zero_diff = df.value
first_order_diff = df.value.diff(1)
second_order_diff = df.value.diff(1).diff(1)


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,4))
ax1.plot(zero_diff); ax1.set_title('Original Series')
ax2.plot(first_order_diff); ax2.set_title('1st Order Differencing')
ax3.plot(second_order_diff); ax3.set_title('2nd Order Differencing');
```

It is possible to _deseasonalize_ a TS.

```py
# Let's remove seasons
df['deseasonalized'] = df.value.values/result_mul.seasonal

plt.figure(figsize=(15,4)); plt.subplot(1,2,1); plt.plot(df.deseasonalized);
plt.title('Drug Sales Deseasonalized', fontsize=16);

# Also remove exponential trend
df['linearized'] = np.log(df['deseasonalized'])

plt.subplot(1,2,2); plt.plot(df['linearized'])
plt.title('Drug Sales Linearized', fontsize=16);
```

```py
# Let's difference this and look at the ACFs
fig, axes = plt.subplots(1, 3,figsize=(15,4))

axes[0].plot(df['linearized']); axes[0].set_title('Linearized Series')
# 1st Differencing
y_diff = df['linearized'].diff().dropna()
axes[1].plot(y_diff); axes[1].set_title('1st Order Differencing')

# 2nd Differencing
y_diff_diff = df['linearized'].diff().diff().dropna()
axes[2].plot(y_diff_diff); axes[2].set_title('2nd Order Differencing');
```

```py
# check with ADF Test for stationarity
print('p-value zero-diff: ', adfuller(df['linearized'])[1])
# 0.71346
print('p-value first-diff: ', adfuller(df['linearized'].diff().dropna())[1])
# 1.00928e-09
print('p-value second-diff: ', adfuller(df['linearized'].diff().diff().dropna())[1])
# 1.31818e-12
```

We shouldn't _over-difference_ not to lose the data properties and select the first diff.
Usually 1-diff is enough
$d$ is anothe hyperparameter

```py
# automatically estimate differencing term
from pmdarima.arima.utils import ndiffs
ndiffs(df['linearized'])
```

```py
# ACF / PACF analysis of y_diff linearized
fig, axes = plt.subplots(1,3, figsize=(16,2.5))
axes[0].plot(y_diff); axes[0].set_title('1st Order Differencing')
plot_acf(y_diff, ax=axes[1]);
plot_pacf(y_diff, ax=axes[2], c='r');
```

```py
# from statsmodels.tsa.arima_model import ARIMA #statsmodels 0.11
from statsmodels.tsa.arima.model import ARIMA  #statsmodels 0.12+

arima = ARIMA(df['linearized'], order=(2, 1, 1), trend='t')
arima = arima.fit()
arima.summary()
```

### Performance Metrics

#### Akaike Information Criterion (AIC)

Metric to compare different models. The lower the better.

We can use **`auto_arima`** to `GridSearch` the hyperparameters $p, d, q$

```py
import pmdarima as pm
smodel = pm.auto_arima(
    df['linearized'],
    start_p=1, max_p=2,
    start_q=1, max_q=2,
    trend='t',
    seasonal=False,
    trace=True
    )
# Performing stepwise search to minimize aic
#  ARIMA(1,1,1)(0,0,0)[0] intercept   : AIC=-555.440, Time=0.19 sec
#  ARIMA(0,1,0)(0,0,0)[0] intercept   : AIC=-453.201, Time=0.04 sec
#  ARIMA(1,1,0)(0,0,0)[0] intercept   : AIC=-527.228, Time=0.10 sec
#  ARIMA(0,1,1)(0,0,0)[0] intercept   : AIC=-533.804, Time=0.12 sec
#  ARIMA(0,1,0)(0,0,0)[0]             : AIC=-453.201, Time=0.04 sec
#  ARIMA(2,1,1)(0,0,0)[0] intercept   : AIC=-560.953, Time=0.08 sec
#  ARIMA(2,1,0)(0,0,0)[0] intercept   : AIC=-562.744, Time=0.04 sec
#  ARIMA(2,1,0)(0,0,0)[0]             : AIC=-562.744, Time=0.05 sec
#
# Best model:  ARIMA(2,1,0)(0,0,0)[0] intercept
# Total fit time: 0.671 seconds
```

#### Evaluate performance

```py
from statsmodels.graphics.tsaplots import plot_predict

fig, axs = plt.subplots(1, 1, figsize=(12, 5))
axs.plot(df['linearized'], label='linearized')
plot_predict(arima, start=1, end=250, ax=axs);
```

We need to recover the seasonality and

```py
# Re-compose back to initial TS
forecast_recons = np.exp(forecast) * result_mul.seasonal[150:]
train_recons = np.exp(train) * result_mul.seasonal[0:150]
test_recons = np.exp(test) * result_mul.seasonal[150:]
lower_recons = np.exp(confidence_int)[:, 0] * result_mul.seasonal[150:]
upper_recons = np.exp(confidence_int)[:, 1] * result_mul.seasonal[150:]

# Plot
plot_forecast(forecast_recons, train_recons, test_recons, lower_recons.values, upper_recons.values)
```

```py
# Check residuals for inference validity
residuals = pd.DataFrame(arima.resid)

fig, ax = plt.subplots(1,2, figsize=(16,3))
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1]);
```

✅ Residuals of equal variance over time (not homoscedastic)
✅ Approximately normally distributed

## Seasonal ARIMA (SARIMA)

No need to deseasonalize.
Seasonal patterns are very common.

Difference over seasonal period. eg. 12th lag.

```py
fig, axs = plt.subplots(2, 2, figsize=(18,8))
# keeping just log transform to stay ~ linear
df['log'] = np.log(df.value)

# linearized series
axs[0,0].plot(df.log); axs[0,0].set_title('linearized Series')

# Normal differencing
axs[0,1].plot(df.log.diff(1)); axs[0,1].set_title('1st Order Differencing')

# Seasonal differencing
axs[1,0].plot(df.log.diff(12))
axs[1,0].set_title('Seasonal differencing of period 12')

# Sesonal + Normal differencing
axs[1,1].plot(df.log.diff(12).diff(1))
axs[1,1].set_title('First order diff of seasonal differencing 12');
```

SARIMA has $7$ **hyperparameters**

`SARIMA(p, d, q)(P, D, Q)[S]`

$p, q, d$ are for _individual_ lag levels
$P, D, Q$ are for _seasonal_ lag levels
$S$ is the seasonality. 12 for annual.

**`GridSearch`** advised.

We can use **`auto_arima`** too

```py
smodel = pm.auto_arima(
    train,
    seasonal=True, m=12,
    start_p=0, max_p=1, max_d=1, start_q=0, max_q=1,
    start_P=0, max_P=2, max_D=1, start_Q=0, max_Q=2,
    trace=True, error_action='ignore', suppress_warnings=True
    )
# SARIMAX(train, order=(0, 1, 1), seasonal_order=(2, 0, 2, 12))
```

```py
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Build Model
sarima = SARIMAX(train, order=(0, 1, 1), seasonal_order=(2, 0, 2, 12))
sarima = sarima.fit(maxiter=75)

# Forecast
results = sarima.get_forecast(len(test), alpha=0.05)
forecast = results.predicted_mean
confidence_int = results.conf_int()
```

## SARIMAX for eXogenous features

Take advantage of two correlated TS by using one to predict another.

```py
SARIMAX(
    endog=df['electricity_price'],
    exog=df['weather'],
    order=(3, 0, 0),
    seasonal_order=(0,1,2,12)
    )
```

```py
# Auto-fit the best SARIMAX with help from this exogenous time series
import pmdarima as pm
sarimax = pm.auto_arima(
    df[['value']],
    exogenous=df_augmented[['seasonal']],
    start_p=0, start_q=0,
    test='adf',
    max_p=2, max_q=2, m=12,
    start_P=0, seasonal=True,
    d=None, D=1, trace=True,
    suppress_warnings=True,
    stepwise=True
    )
sarimax.summary()
```

## Facebook Prophet

Robuts forecast model.

The column names have to be `ds` and `y`. No index.

```py
# Specific format required by Prophet
df = df.reset_index().rename(columns={'date': 'ds', 'value':'y'})
df.head()
```
