# Day 33 - Predict in production

## FastAPI

Uses Python decorators to link the routes to the code.

```python
from fastapi import FastAPI

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}
```

## Docker

`Dockerfile` is a **blueprint** describing the steps required to create a Docker `image`

```dockerfile
FROM python:3.8.12
```

From `Dockerfile` we build an `image`.

```sh
docker build
```

This `image` is a **mold** that allows to create Docker `containers`

```sh
docker run
```
