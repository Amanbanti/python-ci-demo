from fastapi import FastAPI, HTTPException

from calc import add, divide, multiply, subtract

app = FastAPI()


@app.get("/add/{a}/{b}")
def do_add(a: int, b: int):
    return {"result": add(a, b)}


@app.get("/subtract/{a}/{b}")
def do_subtract(a: int, b: int):
    return {"result": subtract(a, b)}


@app.get("/multiply/{a}/{b}")
def do_multiply(a: int, b: int):
    return {"result": multiply(a, b)}


@app.get("/divide/{a}/{b}")
def do_divide(a: int, b: int):
    try:
        return {"result": divide(a, b)}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error