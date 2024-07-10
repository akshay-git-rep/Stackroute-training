import uuid
from flask_smorest import Api
from flask import Flask, abort, request, jsonify
from db import stores, items

app = Flask(__name__)

#uuid is used to generate unique ids
#abort is better to handle responce error status
#it will be documented automatically


#store get
@app.get("/store")
def get_stores():
    return {"My stores": list(stores.values())}

#create endpoint for - get store by ID
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return{"message":"Store not found."}, 404

# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store

#store post
@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        print('store name not found in request data')
        abort(
            400,
            "Bad request. Ensure 'name' is included in the JSON payload.",
        )
    for store in stores.values():
        if store_data["name"] == store["name"]:
            print('store already exists')
            abort(400, "Store already exists.")
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store


# Delete the store by store id
@app.delete("/store/<string:store_id>")
def deleteStore(store_id):
    if store_id in stores:
        del stores[store_id]
        msg = deleteStoreItems(store_id)
        return f"{store_id} is deleted successfully \n" + msg, 200
    else:
        return {"message":"Store not found"}, 404
 
 
def deleteStoreItems(store_id):
    count = 0
    tempItems = items.copy()
    for item in tempItems.values():
        if item["store_id"] == store_id:
            del items[item["id"]]
            count+=1
    return f"{count} items of the store : {store_id} is also deleted sucessfully"


#get item
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,"Store not found.")

@app.post("/item")
def create_item():
    item_data = request.get_json()
    # Here not only we need to validate data exists,
    # But also what type of data. Price should be a float,
    # for example.
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            "Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.",
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, "Item already exists.")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item


#delete endpoint for item

@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted successfully."}
    except KeyError:
        abort(404,"Item not found.")
 
 # update the item data
@app.put("/item/<string:item_id>")
def updateItem(item_id):
    item_data = request.get_json()
    if ("price" not in item_data or "store_id" not in item_data or "name" not in item_data):
        abort(400, message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")
    for item in items.values():
        if (item["id"] == item_id):
            del items[item_id]
            items[item_id] = {**item_data}
            return item
    return "Item not found"

