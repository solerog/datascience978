<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 28 - Recurrent neural networks

## Introduction

Specially designed to deal with sequences as input data.

- Prediction of future stock market values and trends
- Video prediction
- Predict next word

It is massively used for _text_.

## RNN inputs = sequence of observations

Each input is a sequence of repeated observations.

`X.shape` = (n_sequences, n_observations, n_features)

**Notation** $X^t_{i,j}$

$i$ is the **sample** or sequence
$j$ is the **feature**
$t$ is the **time**

In _RNNs_ the input tensor $X$ has one additional dimension at `X.shape[1]`

Standard ML/DL algorithms are not able to handle this extra temporal dimension.

## Prediction

We can predict:

- the next occurence
- the next few occurences
- the next, but not consecutive
- the next, but not right after
- from multivariate input
- to multivariate inputs
- to classification

Inputs are sequences of repeated observations
Output is whatever you want to predict
Each sequence can be of varying length

## Architecture

## Under the hood

$h$ internal state

1. Initialize internal state $h_1$
2. Compute new internal state $h_2$ using $h_1$ and $x^1$
3. Compute $y^1$

The same for the next step.
The _RNN_ is an _NN_ that keep **memories** ($h_n$) about past observations.

### Trainable parameters

The number of weights is:
$$n_h*n_x+n_h*n_h+n_h$$

### Layer output

The output of a layer is the internal state of the last step $y_n = h_n$.
$y^{(t)}$ is not the target directly, but the input of the next layer to compute the target at $t + 1$.
It is a vectur of size `RNN_units`.

The **units** can be seen as the number of **memories** about features maintained in parallel.

## Predict an entire sequence

`return_sequences=True` outputs $y^{(t)}$ at each time step.

```python
model_2 = Sequential()
model_2.add(layers.SimpleRNN(units=2, return_sequences=True, activation='tanh'))
model_2.add(layers.Dense(1, activation='relu'))
```

To predict a **sequence** you need `y_train` to be a sequence too.

## Stacking RNNs

$h$ is the number of interesting temporal features to be captured.

You have to set the `return_sequences=True` in the first layer for stacking RNNs. Not necessary in the last one.

## RNN Zoology

RNNs suffer from vanishing gradient through time.

Three types of RNNs:

- **RNN** (**`SimpleRNN`**)
- **LSTM** (Long Short Term Memory): prevents vanishing gradient.
- **GRU** (Gated Recurrent Units): reduces the number of parameters in comparison to _LSTM_. Faster training with less training data.

`activation='tanh'` as default.

## Variations

Typical neural network: one to one.

## Inputs of different lengths

You cannot fit different lengths in an input sequence.

### Padding

You have to pad input data with some values that will not be considered by the NN.

We have to use values that not occur naturally.

### Masking layer

Tells the model to ignore the padded values

## Single time series
