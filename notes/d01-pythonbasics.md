<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 01 - Python for Data Science

## Introduction to Python

- Multi-platform
- Dynamic typing
- Garbage collected (memory automatically freed up)
- OOP & procedural (top to bottom)
- Large standard library

**REPL**: Read, eval, print, loop. Pythom terminal.

## Built-in Types

Types can be checked with the method `type()`

```py
type(42)
type(3.141592)
type('hello world')
```

### Numeric

integers `int` or floats `float`

Operators:

- `+`
- `-`
- `/` Division
- `//` Floor division
- `%` Remainder or modulo

### Boolean

Either `True` or `False`.

Operators:

- `and`
- `or`
- `not`

```py
(True or False) and False # False
(True or False) and True # True
```

All the other types have Boolean _truthy_ or _falsy_ values.
`None` and `False` are false.
For _numeric_: all values except `0` are `True`.
For _strings_: all non-empty strings are `True`.
For _lists_ and _dicts_: non-empty sets are `True`.

```py
bool(0) # False
bool(5) # True
bool('hello') # True
```

Comparisons:

- `==` and `!=`
- `<` and `>`
- `<=` and `>=`

### String

For single line strings you can use `'` or `"`
If you want to create a multi-line strings you have to use `'''` or `"""`.

```py
a='string'
b=""" Multi
line
String """
```

For special characters inside a string you have to use backslash to escape them.

#### f-strings

Allow expressions inside strings. String interpolation.

```py
first_name = 'john'
last_name = 'lennon'
greeting = f'Hi! My name is {first_name.capitalize()} {last_name.capitalize()}'
```

#### Built-in methods

- _capitalize()_: First letter in the string in capital.
- _endswith(str)_: Checks if the string ends with the argument `str`

```py
'helloworld'.endswith('rld') # True
```

- _strip()_: Removes whitespaces and line breaks in boths ends, but not in the middle

```py
"""
hello     """.strip() # 'hello'
```

- Conversions:

  - _int(other_type)_
  - _float(other_type)_
  - _str(other_type)_
  - _bool(other_type)_

- _input(str)_: Prompts the user for input. It always returns a string. Can be converted while storing.

```py
name = input('Write your name: ')
age = int(input('Write your age: '))
```

- _print(str)_: Prints the value in the console.

### List

Defined inside square brackets.
Each element has an index starting with 0 and a value.

```py
first_list = ['a', 'b', 'c']
```

Length of lists can be checked using `len(list)` function.

```py
len(['a', 'b', 'c']) # 3
```

If one element exists inside a list can be checked by `element in list`.

```py
'a' in ['a', 'b', 'c'] # True
```

#### List operations

Read / acces an element

```py
beatles = ['john', 'paul', 'ringo']
beatles[0] # john
beatles[2] # ringo
beatles[-1] # ringo
```

Assign element. A non-existing index cannot be assigned.

```py
beatles[1] = 'shakira'
```

Slicing

```py
beatles[1:3] = ['shakira', 'ringo']
```

Deleting an element for its index

```py
del beatles[1]
```

Deleting an element for its value

```py
beatles.remove('shakira')
```

- `append(element)` adds one element to the end
- `insert(index, element)` adds one element in the index position, moves the other elements forward.

### Dict

Defined inside brackets. Key-value pairs.
`len(dict)` returns the number of key-value pairs.
`in` checks for keys, not values.

```py
first_dict = {'city': 'Paris', 'population': 2_141_000}
len(first_dict) # 2
'city' in first_dict # True
'Paris' in first_dict # False
```

#### Built-in methods

`keys()` returns the list of keys.
`values()` returns the list of values.
`items()` returns

You should convert to list the results

```py
keys = list({'city': 'Paris', 'population': 2_141_000}.keys())
```

#### Dict operations

```py
instruments = {'john':'guitar', 'paul':'bass'}
```

Read / acces an key-value pair. If the key does not exists, we'll get an error back

```py
instruments['john'] # guitar
```

Another way of accessing if the `get(key, default)` method. It returns the value for the key if it exists, otherwise default.

```py
instruments.get('paul', 'No value') # bass
instruments.get('shakira', 'No value') # No value
```

Add a new key-value pair or updating existing key-value pair

```py
# George does not exist, new key-value pair is created
instruments['george'] = 'drums'
# John exists, key-value pair is updated
instruments['john'] = 'sitar'
```

Deleting an k-v pair

```py
del instruments['john']
```

### Variables

Variable name should be descriptive.

```py
age = 24
name = 'Camila'
```

## Control flow

### If statements

Runs code inside the block after the condition is fulfilled

```py
age = 20
if age >= 21:
    print('You can become president')
elif age >= 18:
    print('You can vote')
else:
    print('Be patient')
```

### For statements

Executes code for each element inside an iteration.

```py
letters = ['a', 'b', 'c']
for l in letters:
  print(l.upper()) # A
                   # B
                   # C
```

```py
for index, value in enumerate(letters):
  print(f'{index}, {l.upper()}') # 0, A
                                 # 1, B
                                 # 2, C
```

```py
beatles = {'paul':'bass', 'ringo':'drums'}
for beatle, instrument in beatles.items():
  print(f'{beatle.capitalize()} plays {instrument}') # Paul plays bass
                                                     # Ringo plays drums
```

### While loops

Executed until the condition returns false

```py
i = 1
while i < 10:
    print(i)
    i += 1
```

## Functions

Defined with the `def` word.
Python uses explicit `return`.
Can take arguments.
Optional arguments must have a default value.

```py
def is_even(number):
  return number % 2 == 0

def is_odd(number = 0):
  return number % 2 != 0

def full_name(first, last, capitalize=True):
    if capitalize:
        return ' '.join([first.capitalize(), last.capitalize()])
    return ' '.join([first, last])
```

## Debugging

```py
def connect(username, password):
    breakpoint()
    query = # [...]
```

`l` to show where you are
Look at local variables + their types (e.g. username or type(username))
`s` for _step_ into (to use before a function call, to enter that function)
`n` for step over (go to _next_ line)
`c` for _continue_ to next breakpoint (or end of program)
