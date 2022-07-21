<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

# Day 6 -Data sourcing

## Pandas I/O

Data sources:

- csv
- API
- SQL Queries
- Google Big Query
- Web scraping

We'll use `Jupyter lab`, it is similar to `Jupuyter Notebook`.

```py
tracks_df = pd.read_csv('data/spotify_2017.csv')
# Fetch only two columns
tracks_df[['artists', 'name']].head()
```

## Module creation

A regular `Python` file is created.
We can import the file by stating.

```py
from <file> import <function>
```

Every time that a change is made in the `Python` file.
It is important to set the `autoreload` option in the top of the _Jupyter notebook_.
Once the code below is set, kernel has to be restarted, but just once.

```py
%load_ext autoreload
%autoreload 2
```

Possible parameters for `autoreload`.
_0_: Default value. No autoreload.
_1_: Checks only the function that we are running.
_2_: Checks all the functions from the notebook.

The necessary imports have to be defined inside the module.

## LOC and ILOC functions

LOC Work like pointer:

```py
df.loc['1', 'name']
```

ILOC needs the exact position. Only receives `int`.

```py
df.iloc[1,2]
```

Create a new column lyrics at index 0:

```py
index = 0
tracks_df.loc[index, 'lyrics'] = fetch_lyrics_music()
```

### Iterrows

```py
for index, row, in tracks_df.iterrrows():
  print(index)
  print(row)
  print(row['artists'])
  print(row['name'])
  tracks_df.loc[index, 'lyrics'] = fetch_lyrics_music(row['artists'], row['name'])
  break
```

### Value_counts

Series method. Returns the number of unique values and its count for the series.

## SQL

```py
import pandas as pd
import sqlite3
conn = sqlite3.connect("data/soccer.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
```

Read from \*pandas

```py
league_df = pd.read_sql(
    '''
    SELECT l.id, l.name, c.name as country_name
    FROM League l
    JOIN Country c ON c.id = l.country_id
    ''', conn)
league_df.head(3)
```

## Google BigQuery

Inside Google Cloud.
[console.cloud.com](console.cloud.com)

```py
!pip install --quiet pandas-gbq
```

```py
import pandas_gbq
project_id = '<gcp project name>'
sql = '''
SELECT * FROM 'bigquery-public-data.austin_crime.crime' LIMIT 1000;
'''
airports_df = pandas_gbq.read_gbq(sql, project_id=project_id)
```

## Scraping
