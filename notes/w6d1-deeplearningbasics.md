<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 25 - Deep learning basics

## Fundamentals

Use cases

## Basic architecture

**Neuron** is an operation {regression, activation}.
A concatenation of a linear combination and a non-linear combination.

### Activation functions

Used for introducing **non-linearities**

- Sigmoid
- tanh
- ReLU
- Leaky ReLU
- Maxout
- ELU

_ReLU_ = rectified linear unit

An input passes through many different neurons.
An output of a neuron can be passed through a new layer of neurons.

## Neural network

Combination of neuron layers with different activation functions.

## Keras

1. Define architecture

   ```py
   model = Sequential()
   model.add(...)
   ```

2. Define methods

   ```py
   model.compile(...)
   ```

3. Fit on data

   ```py
   model.fit(X, y, ...)
   ```

4. Predict

   ```py
   y_new = model.predict(X_new)
   ```

### Decision rules

Most decision rely on practice.

1. First layer needs the size of the input.

   ```py
   # Imagine each observation has 4 features (x1, x2, x3, x4)
   model = Sequential()
   model.add(layers.Dense(10, input_dim=4, activation='relu'))
   ```

   The model has to know the size of the input
   It impacts the **number of weights** of the first layer.

2. Last layer is dictated by the task.

   - **Regression** tasks require **linear** activation functions.

     ```py
     ### size 1 (predict one value):
     model.add(layers.Dense(1, activation='linear'))

     # OR

     ### size 13 (y_pred.shape=(13,))
     model.add(layers.Dense(13, activation='linear'))
     ```

   - **Classification** tasks require **softmax** or **sigmoid**
     Softmax turns numbers into probabilities that sum 1.

     ```py
     ### 2 classes (binary)
     model.add(layers.Dense(1, activation='sigmoid'))

     # OR

     ### 8 classes (y_pred.shape=(8,))
     model.add(layers.Dense(8, activation='softmax'))
     ```

In practice you have to choose:

- Number of neurons
- Number of layers
- Activation functions

## Training loss and optimization procedure

### Compiling

```py
model.compile(loss='mse', optimizer='adam')
```

### Fitting

```py
model.fit(X, y, batch_size=32, epochs=10)
```

The learning phase is iterative and stochastic.

- `batch_size` is the subset size given to the neural network.

## Conclusion & intuition

**Deep learning** is multiple linear regressions stacked together and non-linear functions called _activation functions_.

_Dense networks_ are **universal approximations** to any function with arbitrary precision. They are **not** the most appropriate architecture for some topics (imgs, text, ...)

💡 First layer needs the size of the input
💡 Last layer's neuron numbers equals the output dimension
💡 Last layer activation is `Linear` or `Softmax`/`sigmoid`
💡 Almost always start with `relu` activaiton function

## Bonus 1

[How Many Hidden Layers/Neurons to Use](https://towardsdatascience.com/beginners-ask-how-many-hidden-layers-neurons-to-use-in-artificial-neural-networks-51466afa0d3e)

There are 3 classes of layers

- Input (x1)
- Hidden (as many as necessary)
- Output (x1)

The number of **neurons** in the input layer equals the number of input variables in the data to process.
The number of **neurons** in the ouput layer equals the number of outputs associated to each input.

To determine the number of Hidden layers and neurons of each layer:

1. Draw an expected decision boundary to separate the classes.
2. Express the decision boundary as a set of lines.
3. The number of lines represent the number of **neurons** in the **first hidden layer**
4. To connect the lines of the previous layer, a new hidden layer is added.
5. The number of hidden neurons in each hidden layer is equal to the number of connections.

In artificial neural networks, **hidden layers** are required if and only if data must be separated non-linearly. (with a single line)

## Bonus 2

[What is a neural network - 3Blue1Brown](https://www.youtube.com/watch?v=aircAruvnKk&ab_channel=3Blue1Brown)
