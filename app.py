from flask import Flask, request
from operations import add, sub, mult, div

app =Flask(__name__)


@app.get("/add")
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    print("type", type(result))
    return str(result)


# @app.get("/sub")
# def sub():

# @app.get("/mult")
# def mult():

# @app.get("/div")
# def div():