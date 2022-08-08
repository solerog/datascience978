<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 14 - Decision Science - Communication

Bad data leads to a bad model.

- Make the complex easy to understand.
  - Not explaining technical things
  - Explain the findings, not the process.

## Pyramid principle

Three problems, causes, actions for each solution.

- Deductive

  - Why(Problems) - Why(Causes) - How(Actions) - Solution

- Inductive

  - Solution - How(Actions) - Why(Causes) - Why(Problems)

## Trade-offs

1. Create model, `lift` table.
2. Create `mandays` table.
3. Create `sensitivity` matrix.

```py
lift = np.arange(0.01, 0.05, 0.01)
benefits = pd.DataFrame({'lift': lift, 'benefit': 100000*20*lift})
mandays = np.arange(20, 60, 10)
costs = pd.DataFrame({'mandays':mandays, 'cost': mandays*500*3})
```

```py
costs['connect'] = 1
benefits['connect'] = 1
possible_scenarios = benefits.merge(costs)
possible_scenarios['profit'] = possible_scenarios['benefit'] - possible_scenarios['cost']
```

```py
possible_scenarios.pivot(index='lift', columns='mandays', values='profit')
```

```py
# _ displays the last thing displayed and allows changes.
_.style.applymap(lambda x : 'color: red' if x < 0 else 'color: black')
```

## Powerful forms of communication

1. Docs and code itself
   - Write the docs to see the `best practices`.
2. Interactive tools

## Advanced parameters

`args` extra arguments the function can receive. `args` is a tuple.

```py
def function(name, *args):
  print(name)

function('roger', 72)
```

`kwargs` keyword arguments. Preceded by the key. It returns a dictionary with key, value.

```py
def function(name, *args, **kwargs):
  print(name)
  print(args)
  print(kwargs)

function('roger', 72, 'Castelldefels', course='data science')
```

```py
class Student:
  def __init__(self, name, age, **kwargs):
    self.name = name
    self.age = age
    self.__dict__.update(kwargs)
```

```py
class DataStudent(Student):
  course = 'data'

  def __init__(self, name, age, batch, **kwargs):
    super().__init__(name, age, **kwargs)
    self.batch = batch
```

## Type

```py
def say_hi(name: str) -> str:
  print f'Hi {name}!'
```

## Decorators

```py
def decorator(func):
  def wrapper():
    print('Before')
    print(func())
    print('After')

  return wrapper
```

```py
@decorator
def say():
  return 'Hello world'
```

```py
say()
# Before
# Hello World
# After
```

## Presentation

View -> Cell Toolbar -> Slideshow

Each cell can be defined as a `slide`, `subslide` or `fragment`, `notes` or `skip`.
`notes` and `skip` are not displayed in the presentation.

In a Python cell run

```py
jupyter nbconvert --to slides --post serve <your_notebook.ipynb>
```

It is saved as an `.html` file.
