<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 8 - Algebra & Calculus

## Volcabulary

- Exponent (power)
- Coefficient
- Term
- Operator
- Constant

## Functions

A relation that maps one set to another set.
$f:\R\rightarrow\R,f(x)=x^2+1$

```py
def square_plus_one(x):
    return x * x + 1
```

### Multivariate functions

A function defined by two or more variables.

```py
def multi_variate(x0, x1):
    y = 2 * x0 + 3 * x1 + 7
    return y
```

### Representation

We can plot functions on planes
$y = mx+b$
_m_ is the slope.
_b_ the intercept to y-axis.

### Non-linear functions

$y=cos(x)$

### Identity function

$y=x$

### Inverse function

Not all functions have an inverse. Only if both $f$ and $f^{-1}$ are **bijective**

$f(x) = y\longleftrightarrow g(y) = x$

## System of linear equations

COllection of one or more equations involving the same set of variables.

They might have 0, 1 or infinite solutions.

### Trivial (one unknown)

$2x+4$

### Non-Trivial (two unknowns)

- A father is 22 years older than his son.
- In 10 years, the father will be twice as old as his son.

$x = father's age$
$y = sons's age$

$x = y + 22$
$x + 10 = 2 (y + 10)$

$x = y + 22$
$x = 2y + 10$

$0 = y - 12$
$y = 12$
$x = 34$

In _python_:

```py
x = np.array([6, 18])
plt.plot(x, x + 22)
plt.plot(x, 2 * x + 10)
plt.xlabel('son')
plt.ylabel('father')
plt.show()
```

## Vectors

Defined by two indexes. x and y.
$(x,y)$

$\vec\imath$ and $\vec\jmath$ are

It can also be defined in the _polar notation_.

$(v, \theta)$

In _python_:

```py
v = np.array([[2, 1]])
v
```

To have data in vertical (as a usual vector), we have to _transpose_ it:

```py
transpose_v = v.T
```

### Dot product

Measure if $a$ and $b$ _reinforce_ or _cancel_ each other

If $a$ and $b$ are perpendicular, dot product is $0$. They don't have any similarity.

$a_xb_x + a_yb_y = |a|cos(\theta)|b|$

### Euclidian distance

Also called $L^2$ distance
$||\vec{AB}|| = L^2(\vec{AB})$

$d = \sqrt{(x_A-x_B)^2+(y_A-y_B)^2}$

### $L^1$ distance

Also known as 'taxi cab distance'.
Distance between two vectors following the grid.

## Matrices

```py
A = np.array([[1, 2], [3, 4], [5, 6]])
```

General notation $a_{mn}$ where $m$ is the row, $n$ is the column.

### Transpose

Rotating the matrix along its diagonal.
The transpose of the transpose is the original matrix.

```py
A.T
```

### Addition

Add numbers with the same position together

```py
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1, 4], [2, 5], [2, 3]])
C = A + B
```

### Scalar multiplication

Multiply each value in the matrix by the scalar

```py
D = 3 * A
```

### Matrix multiplication

Only defined if the number of **columns of the left** matrix is **the same as** the number of **rows of the right** matrix.

#### Matrix x Vector product

Also called _linear transformation_.
Visually, it returns the new vector coordinates after the transformation.

$\begin{bmatrix}a&b\\ c&d\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix}=x\begin{bmatrix} a\\ c\end{bmatrix}+y\begin{bmatrix}b\\ d\end{bmatrix}=\begin{bmatrix}ax+by\\ cx+dy\end{bmatrix}$

```py
A = np.array([[1, 1], [0, 1]])
B = np.array([[1], [2]])
np.matmul(A, B) # or np.dot(A,B) or A.dot(B)
```

#### Matrix x Matrix

Matrix multiplication is **associative** and **distributive**.
Not **commutative** $AB\not ={BA}$

Left matrix (m-n) and right matrix (n-p) multiplications gives as a result a new (m-p) matrix.

$\begin{bmatrix}a&b\\ c&d\end{bmatrix}\begin{bmatrix}e&f\\ g&h\end{bmatrix}=\begin{bmatrix}ae+bg&af+bh\\ ce+dg&cf+dh\end{bmatrix}$

### Identity matrix

Ones in the diagonal.

$I=\begin{bmatrix}1&0&0\\ 0&1&0\\ 0&0&1\end{bmatrix}$

### Inverse of a matrix

Returns the $I$ matrix if multiplied by the original matrix.

$A^{-1}A=I$

It helps solving _linear equations_.

$\Bigl\{{x - y = 22 \\
x - 2y = 10}$

$\begin{bmatrix}1&-1\\ 1&-2\end{bmatrix}\begin{bmatrix}x_1\\ x_2\end{bmatrix}=\begin{bmatrix}22\\ 10\end{bmatrix}$

In _python_:

```py
A = np.array([[1, -1], [1, -2]])
A_inv = np.linalg.inv(A)
B = np.array([[22], [10]])
np.matmul(A_inv, B)
```

#### Linear dependence

Three options:

- No solution
- One solution
- Infinite solutions

### Determinant

The _determinant_ is the area of the parallelepiped resulting from the matrix.
A square matrix is **not invertible** iif its _determinant_ is $0$.

```py
np.linalg.det(A)
```

## Computational complexity

- $O(1)$
- $O(log(n))$
- $O(n)$
- $O(nlog(n))$
- $O(n^2)$
- $O(2^n)$

## Derivative

The derivative of a function is related to its _rate of change_.
