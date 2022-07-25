# Unsafe way

import sqlite3

conn = sqlite3.connect('data/exploitable_db.sqlite')
c = conn.cursor()


def connect_unsafe(username, password):
    query = f"""
    SELECT *
    FROM users
    WHERE users.username = '{username}'
    AND users.password = '{password}'
  """
    c.execute(query)
    user = c.fetchone()
    if user is None:
        return "Unauthorized"
    else:
        return "Authorized"


print(connect_unsafe('john', 'passw0rd'))
# Hack
print(connect_unsafe("john", "'OR 1=1 --"))

# Safe way


def connect_safe(username, password):
    query = """
    SELECT *
    FROM users
    WHERE users.username = ?
    AND users.password = ?
  """
    c.execute(query, (username, password))
    user = c.fetchone()
    if user is None:
        return "Unauthorized"
    else:
        return "Authorized"


print(connect_safe('john', 'passw0rd'))
# Hack
print(connect_safe("john", "'OR 1=1 --"))
