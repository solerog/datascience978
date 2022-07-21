<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 4 - Advanced SQL

## SQL injection

Possible attack sending SQL data through forms
Has to be prevented

Unsafe way of inserting data:

```sql
insert into Students (last_name, first_name)
values('{last_name}', '{first_name}')
```

It allows the possibility of injecting SQL code. If `last_name` = `Robert'); drop table Students; --`

```sql
insert into students (last_name, first_name)
values('Smith', 'Robert'); drop table Students; --');
```

### Parameter substitution

Prevents attacks of _SQL injection_.
It replaces all `?` for the tuple values in order.
The tuple has to have as many values as `?` signs in the query.
If `?` is 1, tuple has to have a trailing comma `(first,)`

```py
query = """
    select * from users
    where users.username = ?
    and users.password = ?
    """
c.execute(query, (username, password))
```

## CRUD

Methods for creating, reading, updating and deleting data.

### Create

```sql
insert into table (column1, column2, ...)
values (value1, value2 , ...)
```

Example:

```sql
insert into Country (id, name)
values (999, 'NewCountry')
```

### Update

```sql
update table
set column_1 = new_value_1,
    column_2 = new_value_2
where
    search_condition
```

Example:

```sql
update Country
set name = 'NotNewCountry'
where id = 999
```

### Delete

Delete one or many rows from a table.
It is **best practices** to first select the data to be deleted to be sure

```sql
select * from table where search_condition

delete from table
where search_condition
```

Example:

```sql
delete from Country
where id = 999
```

## Cleaning data

### String functions

```sql
SUBSTR
INSTR
TRIM (LTRIM, RTRIM)
LENGTH
UPPER / LOWER
REPLACE
```

Other functions:

```sql
LEFT(string, n)
RIGHT(string, n)
POSITION(pattern in string)
```

[SQLite String Functions](https://www.sqlitetutorial.net/sqlite-string-functions)

### Join

#### Inner join

Default join. Data must exist in both tables, otherwise it does not appear.

```sql
select * from League l
join Country c on c.id = l.country_id
```

#### Left join

Data is returned as long as it exists in the first (left) table.

```sql
select * from League l
left join Country c on c.id = l.country_id
```

#### Right join

Data is returned as long as it exists in the second (right) table.
:x: Not supported in SQLite.

#### Full outer join

Data is returned from both tables.
:x: Not supported in SQLite.

#### Self join

Fetching data from the same table. `Alias` has to be used.

```sql
select employees.id, employees.name,
    employees.title, managers.name as manager
from employees
left join employees as managers on managers.id = employees.manager_id
```

### Coalesce

Replaces `NULL` values

```sql
select
    League.id,
    League.name,
    COALESCE(Country.name, 'Unknown') AS country_name
from League
left join Country on Country.id = league.country_id
```

### Window functions

Perform a calculation across a set of table rows that are somehow related to the current row.
Simmilar to aggregate functions as `COUNT()` `AVG()` but without grouping or compressing the rows. Row retain separate identities.

The _window_ is defined by the `PARTITION`

#### Rank

Useful to answer the question: Was it the customer's first order? second one? etc.

Example:

```sql
SELECT
    orders.id,
    orders.ordered_at,
    orders.customer_id,
    RANK() OVER (
        PARTITION BY orders.customer_id
        ORDER BY orders.ordered_at
    ) AS order_rank
FROM orders
```

In this example the rank is the sort number of the orders of the same customer (`PARTITION`) and sorted by the order time (`ORDER BY`)

#### Sum

Cumulative amount of orders in time.

```sql
SELECT
    orders.id,
    orders.ordered_at,
    orders.amount,
    orders.customer_id,
    SUM(orders.amount) OVER (
        PARTITION BY orders.customer_id
        ORDER BY orders.ordered_at
    ) AS cumulative_amount
FROM orders
```

Left join can be used too:

```sql
SELECT
    orders.id,
    customers.first_name,
    customers.last_name,
    orders.ordered_at,
    SUM(orders.amount) OVER (
        PARTITION BY orders.customer_id
        ORDER BY orders.ordered_at
    ) AS cumulative_amount
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
```

### With

:arrow_right:[Documentation](https://www.sqlite.org/draft/lang_with.html)

We want to select the cumulative number of matches played every month.
First we create a table with the matches per month.

```sql
SELECT
  STRFTIME('%Y-%m', DATE(m.date)) AS period,
  COUNT(*) AS cnt
FROM Match m
GROUP BY period
ORDER BY period
```

The we calculate the aggregated sum using the table above as an independent table inside the `WITH` clause.
`PARTITION` is not needed as the table only contains the data to be used.

```sql
WITH matches_per_month AS (
    SELECT
        STRFTIME('%Y-%m', DATE(m.date)) AS period,
        COUNT(*) AS cnt
    FROM Match m
    GROUP BY period
    ORDER BY period
)
SELECT
    matches_per_month.period,
    SUM(matches_per_month.cnt) OVER (
        ORDER BY matches_per_month.period
    ) AS cumulative_count
FROM matches_per_month
```
