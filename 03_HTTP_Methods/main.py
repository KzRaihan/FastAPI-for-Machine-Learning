from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_method():
    return {"method": "GET"}


@app.post("/")
def post_method():
    return {"method": "POST"}


@app.put("/")
def put_method():
    return {"method": "PUT"}


@app.delete("/")
def delete_method():
    return {"method": "DELETE"}
