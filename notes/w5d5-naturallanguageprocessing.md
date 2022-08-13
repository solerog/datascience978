<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 24 - Natural Language Processing

## Introduction

The goal is to incorporate **textual data** in ML algorithms.

(e-mail filtering, chatbots, voice recognition)

## NLP

Subfield of linguistics concerning the interactions between computer and human language.

### Text preprocessing

As in any ML algorithm, data preprocessing is crucial.

- Lowercase
- Deal with numbers
- Split
- Tokenize
- Remove 'stopwords'
- Lemmatizing

`.strip` removes whitespaces at the beginning and end of a _str_.
`.strip(str)` removes any letter in 'str' and whitespaces in the beginning and end of a _str_.

`.replace(old, new)` replaces all occurences of _old_ with _new_

`.split(delim)` splits text into list using _delim_.

`.lower()` converts all text to lowercase.

Remove numbers

```py
''.join(char for char in text if not char.isdigit())
```

Remove punctuation and symbols. Not always needed.

```py
import string
string.punctuation
text = [text.replace(punct, '') for punct in string.punctuation]
```

### NLTK

_Tokenize_: Create a list from a string.

_Stopwords_: Remove words that are frequently used and don't carry much information.

Useful for topic modelling
Dangerous for sentiment analysis or authorship attribution.

_Lemmatizing_: Find the root of the words to group them by their meaning.

## Vectorizing

Process of converting a raw text into numerical representation

### Bag-of-words

Most simple and effective ways to represent a text.
Counts the number of words in each sentence.

`CountVectorizer()`

Limitations:
❌ Does not take into account the **order**
❌ Does not take into account **document length**
❌ Does not capture the **document context**

### `Tf-idf` representation

Term frequency (tf) & count vectorizer.

Frequency or a word $x$ in a document $d$ is called **`term frequency`**

$t_{young,3} = 5$

Document frequency (df)

The number of documents $d$ containing the word $x$ is called **`document frquency`** $df_x$

Relative document frequency $\dfrac{df_x}{N}$

Intuition: Give a weight to any term that appears frequently in a single document but not in too many documents.

### TfidfVectorizer

We have to control the vocabulary size not to have all possible words as features.

#### Key parameters of `TfidVectorizer` (and `CountVectorizer`)

`max_df` (and `mid_df`) are percentages or int.
They ignore terms that appear in more (or less) than the percentage of the documents or the number of documents specified.

`max_features` gets the most frequent words

✅ More robust to document length
❌ No word order
❌ Does not capture the within-document context

## `N-grams`

Groups of tokens.
Unigram (1-gram), bigrams, trigrams, 4-gram.

### Key parameter

`ngram-range` = (1, 3) will capture from unigrams to trigrams
`ngram-range` = (2, 2) will only capture bigrams

There are two methods for _vectorizing_:

- `CountVectorizer` (counting)
- `TfidVectorizer` (weighing)

Main parameters

- `min_df` (infrequent words)
- `max_df` (frequent words)
- `max_features` (dimensionality)
- `ngram_range` (context)

## Multinomial Naive Bayes Algorithm

Classification algorithm based on **Bayes'**.

$\mathbb{P}$

✅ Easy to implement
✅ Not iterative
✅ Works well on data
✅ Not a parametric model

❌ Assumes that words don't depend on previous words.

## Latent Dirichlet Allocation

Unsupervised algorithm for finding topics in documents.

Latent = hidden topics
Dirichlet = Type of probability distribution
