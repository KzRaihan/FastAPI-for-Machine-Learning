from fastapi import FastAPI


app = FastAPI()


@app.put("/items/{item_id}")
def update_item(item_id: int):

    return {
        "message": "Item updated",
        "item_id": item_id
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    return {
        "message": "Item deleted",
        "item_id": item_id
    }
