from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int, search: str | None = None):

    return {
        "item_id": item_id,
        "search": search
    }
