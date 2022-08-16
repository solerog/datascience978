<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 26 - Optimizer, Loss & fitting

## Compiling

It's how neural networks optimize parameter $\theta$

```py
model.compile(
  loss='',
  optimizer='',
  metrics=''
)
```

Examples:

```py
# REGRESSION
model.compile(loss='mse',
              optimizer='adam',
              metrics=['mae'])

# CLASSIFICATION WITH 2 CLASSES
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# CLASSIFICATION WITH N (let's say 14) CLASSES
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy', 'precision'])
```

### Metrics

Human measures of how good predictions are.
Computed by **forward propagation**.

Common metrics:

- Calssification
  - Precision, recall, accuracy, f1
- Regression
  - MSE, MAE, RMSE, RMSLE

All metrics and losses are based on _distance_ or _similarity_.

```py
# use strings for quick access
model.compile(metrics=['accuracy', 'precision'])

# use Keras metric objects for fine-tuning
metric = keras.metrics.AUC(
    num_thresholds = 200,
    curve='ROC', # or curve='PR'
)
model.compile(metric=metric)

# Custom metrics
def custom_mse(y_true, y_pred):
    squared_diff = tf.square(y_true - y_pred)
    return tf.reduce_mean(squared_diff)

model.compile(metrics=[custom_mse])
```

### `loss function` $L_x(\theta)$

The function to optimize the algorithm.
It has to be smooth and continuous so that a gradient can be computed.

Measures the distance between $\hat y$ and $y$

Binary cross-entropy = Log loss

```python
# use strings for quick access
model.compile(loss = "binary_crossentropy")


# use Keras metric objects for fine-tuning
loss = keras.losses.BinaryCrossentropy(...)
model.compile(loss = loss)

# Custom losses
def custom_mse(y_true, y_pred):
    squared_diff = tf.square(y_true - y_pred)
    return tf.reduce_mean(squared_diff)

model.compile(loss=custom_mse)
```

### Optimizer

The optimizer is fed with data **batch by batch**.

In the forward pass we calculate the functions.
In the backward pass the derivatives are calculated. All previously calculated terms can be reused.

`backpropagation`

**Speed** benefits:

- 1 iteration uses:
  - 1 forward pass
    - Computes outputs for each observation in minibatch
    - Loss for the minibatch
  - 1 backward pass

**Vanishing gradient** phenomenon: The weights of the first layers are harder to move than from the last layer.

Which optimizer to choose?

- `Adam` the best to start with. Works well in most scenarios.

#### Hyperparameters

```python
opt = tensorflow.keras.optimizers.Adam(
    learning_rate=0.01,
    beta_1=0.9,
    beta_2=0.99
)
model.compile(loss=..., optimizer=opt)
```

##### `learning_rate`

Amount of change on the weights for each update
Smaller rates require more epochs.

##### `batch_size`

The smaller the batch, the faster it may converge but is more stochastic.
The larger the batch, the better it generalizes, but requires more computational power.

Always a **power of $2$** for computational reasons.
$16$ or $32$ in most cases.

##### `epochs`

The larger the `batch_size` the more `epochs` you need.

Use `train_test_split`. It is better to split data in 3 sets _train_, _validation_ and _test_.

**K-fold cross-validation** can be better but is much more expensive computationally.

```python
# Give validation set explicitly
history = model.fit(X_train, y_train,
          validation_data=(X_val, y_val),
          batch_size=16,
          epochs=100)
```

or using `validation_split`:

```python
history = model.fit(X_train, y_train,
          validation_split=0.3, # /!\ LAST 30% of train indexes are used as validation
          batch_size=16,
          epochs=100,)
          # shuffle=True) # Training data is shuffled at each epoch by default
```

##### `Early stopping`

It stops the algorithm if the `validation loss` is worse in the next `epoch`

```python
from tensorflow.keras.callbacks import EarlyStopping

es = EarlyStopping(patience=20, restore_best_weights=True)

model.fit(X_train, y_train,
          batch_size=16,
          epochs=100,
          validation_split=0.3,
          callbacks=[es])

# "callback" means that the early stopping criterion
# will be called at the end of each epoch
```

We need to add a `patience` hyperparameter so it does not stop in the first epoch that does not improve the loss.
We also add `restore_best_weights` so the best results are fetched and not the last

##### Regularization

All previous steps are **mandatory**.

It is important to try an _initial architecture_ and then _know what to change_ to improve results.

Prevents models to overfit.
Applied _layer by layer_ and active during the training.
Can be applied to _weights_ (`kernel_regularizer`), _biases_ (`bias_regularizer`) and/or _outputs_ (`activity_regularizer`).
It **does not add** parameters to the model.

1. $L1$
2. $L2$

```python
from tensorflow.keras import regularizers, Sequential, layers

reg_l1 = regularizers.L1(0.01)
reg_l2 = regularizers.L2(0.01)
reg_l1_l2 = regularizers.l1_l2(l1=0.005, l2=0.0005)

model = Sequential()

model.add(layers.Dense(100, activation='relu', input_dim=13))
model.add(layers.Dense(50, activation='relu', kernel_regularizer=reg_l1))
model.add(layers.Dense(20, activation='relu', bias_regularizer=reg_l2))
model.add(layers.Dense(10, activation='relu', activity_regularizer=reg_l1_l2))
model.add(layers.Dense(1, activation='sigmoid'))
```

##### Dropout layer

Randomly kills the activity of some _neurons_ so their weights are not updated.
Prevents neurons from over-specializing and not being able to generalize.

It **does not add** parameters to the model.

```python
model = Sequential()

model.add(layers.Dense(20, activation='relu', input_dim=56))
model.add(layers.Dropout(rate=0.2))  # The rate is the percentage of neurons that are "killed"

model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dropout(rate=0.2))

model.add(layers.Dense(3, activation='softmax'))
```

## Pro tips

1. Start from the **last layer**.
2. Implement the **easiest architecture** first
3. Stick with the same batch size ($16$ or $32$) and only change it when you are sure about the effects it has.
4. Don't think about **`epochs`**, use `EarlyStopping`.

## More tips

1. Make your model **overfit** before regularizing.
2. If you can't **overfit** change your `learning_rate`.
3. **Regularization** is good if the loss is decreasing rapidly.
4. Only **regularize** if topics 1, 2 and 3 are fulfilled.
5. Try to **regularize** last layers before the first ones.

## Preprocessing pipelines

```python
from tensorflow.keras.layers.experimental import preprocessing
```
