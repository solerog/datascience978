<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 29 - Natural Language Processing

## Reminder

- What is $X$?
  $X$ is either one observation, a sequence of observation of multiple sequences of observations.
  The observation is repeated through time.

  `X.shape = (N_SEQUENCES, N_OBSERVATIONS, N_FEATURES)`

- What is $y$?
  Can be a feature that exists in $X$ or a complete new feature.
  Can have multiple values or one.

To **stack RNNs** or **predicting a sequence of inputs** we have to set the `return_sequences=True`

```py
model.add(layers.LSTM(units=10, activation='tanh', return_sequences=True))
model.add(layers.LSTM(units=10, activation='tanh'))
model.add(layers.Dense(1))
```

If the input sequences $X$ don't have the same length, we have to use `pad_sequences`.

```py
from tensorflow.keras.preprocessing.sequence import pad_sequences
X_pad = pad_sequences(X, dtype='float32', padding='post', value=-1000)
model.add(layers.Masking(mask_value=-1000))
```

## NLP Examples

### Language model

Attempts to predict the **next word** given a list of words.

### Text classification, sentiment analysis

Classification depending on text.

### Sequence to sequence

Language translation. Given a sequence, return a sequence.

## How to feed RNN with words

🚨 **Clean data** before anything

- Remove capital letters, numbers, punctuation, ...

To convert words into numbers, we can represent each word by a given number. (**tokenization**). NOT the solution as it does not convey the context.

### High dimensional embedding

Each word is represented by a vector of chosen length.
The vector determines if the word is positive or negative.

#### 2D embedding

We add a dimension to _negative-positive_ which is _abstract-concrete_.

#### 3D, 4, 5, ..., n embedding

Same as before, adding other dimensions to represent more word 'rankings'.

A **good embedding** should have semantically similar words close in the space.

## Custom embedding `layers.Embedding`

Find an embedding that is specially designed for your task.

`X.shape = (n_sentences, max_sentence_length, embedding_dim)`

### `Tokenizer`

```python
tk = Tokenizer()
tk.fit_on_texts(X)
X_token = tk.texts_to_sequences(X)
```

### `layers.Embedding`

Number of params = (`input_dim` + 1) \* `output_dim`

```py
Embedding(input_dim=VOCAB_SIZE,
          input_length=MAX_SENTENCE_LENGTH,
          output_dim=EMBED_DIM,
          mask_zero=True)
```

Running an RNN with custom embedding can be **slow**.

- You can reduce the **embedding space** by reducing the dimensions.
- You can **remove long sentences** (in words) to avoid having lots of useless information (padding)
- You can use a **high batch size** (64, 128, 256)

## Independent Embedding `Word2Vec`

An embedding that is good whatever the task.
The weights are not optimized for the specific task.

Input is a list of sequences
Output is a representation (embedding) for each word it is trained on.

1. `OneHotEncode` all the words
2. Train autoencoder to predict the word in the middle based on its neighbours
3. Use tha latent space (middle layer) as embedding

Parameters:

- `window size`: Number of neighbours
- `embedding dimension`: Latent space

## CNNs for NLP

We have to use 1D Convolutions to get all information, as each column is a word vector representation.

`layers.Conv1D`

A CNN can replace a RNN in a **`Word2Vec`** stack as the _embedding_ is independent of the second layer.

## NLP Zoology

### Attention Mechanism

### Transformer

### BERT
