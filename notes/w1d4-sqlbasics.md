<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 03 - SQL Basics

## Database types

- **SQL**: **S**tructured **Q**uery **L**anguage. Relational database. Contains many different tables interconnected.
  - SQLite
  - PostgreSQL
  - MySQL / MariaDB
  - Microsoft SQL Server
  - Oracle
- **NoSQL**:
  - Document (MongoDB)
  - Key-value (Dynamo)
  - Graph (Neo4j)

SQL language allows fetching data from a database.

## Relational databases

Data is organized in 1 or more tables of columns and rows with a unique `primary key` identifying each row.
When the `primary key`is used in another table is called `foreign key`.
The DB design pattern can be 1:1 (one-to-one) or 1:n(one-to-many).

### SQLite

Single-file database written in `c`.

### ERD (Entity Relationship Diagram) Diagram

Database relationship diagram.

### Queries

Get all columns in table `country`

```sql
select * from country
```

From `python`.
`.fetchall()` method returns a `list` of `tuple`.

```py
import sqlite3

conn = sqlite3.connect('data/soccer.sqlite')
c = conn.cursor()

c.execute("SELECT * FROM Country")
rows = c.fetchall()
print(rows)
```

If `sqlite3.Row` is added to `.row_factory`. Each row acts like a `dict`

```py
conn = sqlite3.connect('data/soccer.sqlite')
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute("SELECT * FROM Country")
rows = c.fetchall()
for row in rows:
    print(f"{row['id']}: {row['name']}")
```

To fetch only one result, `.fetchone()` can be used.

```py
c.execute("SELECT * FROM Country")
result = c.fetchone()
```

To count all the occurences `COUNT(*)` can be used.

```sql
SELECT COUNT(*) FROM Country
```

#### Projection

Select the columns we want the query to return.
Replace `*` for the column names.

```sql
SELECT id, season, stage, date FROM Match
```

**BEST PRACTICE** add a table name alias and add the alias to each column.

```sql
SELECT m.id, m.season, m.stage, date FROM Match m
```

#### Selection

Select the rows we want the query to return
Use of the `WHERE` clause.

```sql
SELECT m.id, m.season, m.stage, date FROM Match m WHERE m.country_id = 1
```

`WHERE` clauses can be linked with `AND` `OR` clauses

```sql
SELECT m.id, m.season, m.stage, date
FROM Match m
WHERE m.country_id = 1
OR m.country_id = 1729
```

It is the same query as:

```sql
SELECT *
FROM Match m
WHERE m.country_id IN (1, 1729)
```

For string filtering, the `=` compares exactly the string.
In the case below we only get results where the `player_name` is exactly John.

```sql
SELECT * FROM Player p WHERE UPPER(p.player_name) = 'JOHN'
```

In the case below we only get results where the `player_name` starts with John.

```sql
SELECT * FROM Player p WHERE UPPER(p.player_name) LIKE 'JOHN%'
```

In the case below we only get results where the `player_name` contains the string `john` in any place.

```sql
SELECT * FROM Player p WHERE UPPER(p.player_name) LIKE '%JOHN%'
```

`COUNT` can also be used with _selection_.

```sql
SELECT COUNT(p.id) FROM Player p WHERE p.height >= 200
```

#### Sort and limit

Data returned can be sorted and limited using words `ORDER BY` and `LIMIT`.
More than one `ORDER BY` can be defined.

```sql
SELECT * FROM Player p ORDER BY p.weight DESC LIMIT 10
```

### Group

SQL allows aggregating rows with a function where values of C column are the same.

```sql
SELECT COUNT(m.id), m.country_id
FROM Match m
GROUP BY m.country_id
```

To sort by the function (`COUNT`, `MAX`, `MIN`, ...) an alias to the result has to exist.

```sql
SELECT COUNT(m.id) AS match_count, m.country_id FROM Match m
GROUP BY m.country_id ORDER BY match_count DESC
```

To filter after the function is created, the word `HAVING` has to be used.
In the case below the query filters the `match_count` value after calculating it.

```sql
SELECT COUNT(m.id) AS match_count, m.country_id
FROM Match m
GROUP BY m.country_id
HAVING match_count >= 3000
ORDER BY match_count DESC
```

### Case

```sql
SELECT COUNT(m.id) AS outcome_count,
  CASE
      WHEN m.home_team_goal > m.away_team_goal
          THEN 'home_win'
      WHEN m.home_team_goal = m.away_team_goal
          THEN 'draw'
      ELSE 'away_win'
  END AS outcome
FROM Match m
GROUP BY outcome
ORDER BY outcome_count DESC
```

### Join

Fetch information from more than one table, using the `foreign keys` to filter.
The information of both tables is combined whenever the `ON` condition is met.

```sql
SELECT l.name league, c.name country FROM League l
JOIN Country c ON l.country_id = c.id
```

### Complete example

```sql
SELECT l.id, l.name AS league_name,
    COUNT(m.id) AS match_count, c.name AS country_name
FROM Match m
JOIN League l ON m.league_id = l.id
JOIN Country c ON l.country_id = c.id
GROUP BY l.id
ORDER BY match_count DESC, country_name ASC
```

### Order of statements

The order matters and it is the following (order of execution):

| Order | Clause   | Function                                 |
| :---- | :------- | :--------------------------------------- |
| **1** | From     | Choose and join tables to get baase data |
| **2** | Where    | Filter base data                         |
| **3** | Group by | Aggregate base data                      |
| **4** | Having   | Filter aggregated data                   |
| **5** | Select   | Return final data                        |
| **6** | Order by | Sort final data                          |
| **7** | Limit    | Limit returned data to a row count       |
