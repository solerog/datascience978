from fastapi import FastAPI

app = FastAPI()


# define a root `/` endpoint
@app.get("/")
def index():
    return {"ok": True}


# define a root `/` endpoint
@app.get("/marti")
def marti():
    return {"marti": 'Chan chan chaaaann'}


# define a root `/` endpoint
@app.get("/predict")
def predict(name='Roger', age=34):
    return dict(name=name, age=age)
