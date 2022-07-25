<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 10 - Decision Science - project setup

Working in a real-life project.

## Big picture

Work as data consultant. How to improve the process of the company.

First linear statistical models.
Find correlations between vairables.
Statistical inference.

## Motivations

1. Collecting the data.
2. Store data.
3. Explore and transform. (clean, anomaly detection)
4. Aggregate, label data.
5. Learn and optimize data.

## Olist

Helps small sellers to publish their catalog on Amazon, Walmart, etc.

Customers could review the products before they arrived.

### Data

Info about ~100k orders.

### Revenues

10% of all of the products sold + 80 BRL a month.

### Costs

Square-root of number of orders processed.

Reputation costs
| review_score | cost(BRL) |
|:--|:--|
| 1 | 100 |

## Goal

> How to increase customer satisfaction (so as to increase profit margin) while maintaining a healthy order volume?

## Classes

A `class` is a template designed to build `instances` that share `attributes`.

### Class definition

```py
class Student:

    # Constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
```

### Create instance

```py
student1 = Student('Roger', 34)
```

### Methods

Class can have method inside. All methods must have the `self` parameter.

```py
    def say(self) -> None:
        print(f'Hello my name is {self.name}')
```

### Class attributes

Class variables can be defined inside it.

```py
class Student:

    school = 'LeWagon'

    # Constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
```

### Decorator

It is one function that is called from the class, not the instance.

In the case below it creates a new instance of the class using the birth_year instead of age, calling the constructor with the date substraction.

```py
# Class method
@classmethod
def from_birth_year(cls, name, birth_year):
  return cls(name, date.today().year - birth_year)
```

### Subclasses

They inherit methods and attributes from parent class.

```py
class DataStudent(Student):
  course = 'Data Science'

  def __init__(self, name, age, batch):
    super().__init__(name, age)
    self.batch = batch
```

## Naming conventions

- Packages and modules **all-lowercase** (`pandas`, `lewagon`).
- Class names **UpperCamelCase** (`DataStudent`).
- Variables and functions **lower_snake_case** (`say_hi`, `batch_number`)

## Save global module

Modifiy `.zshrc` file to include `PATH`.

## Jupyter Notebook best practices

Install `nbextensions`.

## iPython Debugger

`s`
`n` next
`c` continue to next `breakpoint()`

In Notebook `%debug`

## Dealing with new datasets

1. Check attributes `shape`, `columns`, `dtypes`.
2. `head`, `describe`, `info`, `nunique`, `isna().sum()`.
3. Plot distributions

Instead of using all these methods, we can use the `pandas_profiling`.
(It takes some time tobe displayed)

```py
import seaborn as sns
import pandas_profiling

df = sns.load_dataset('mpg')
df.profile_report()
```
