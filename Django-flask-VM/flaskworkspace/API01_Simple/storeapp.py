from flask import Flask, request
app = Flask(__name__)


stores = [
    {
        "name": "Store 1",        
        "items":[
            {
                "name":"Table",
                "price":5678
            },
            {
                "name":"Chair",
                "price":2678
            },
        ]
    },
    {
        "name": "Store 2",        
        "items":[
            {
                "name":"Laptop",
                "price":58678
            },
            {
                "name":"Tablet",
                "price":32678
            },
        ]
    }
]

@app.route("/store")
def getStores():
    return {"stores": stores}

# @app.post("/store")         #make it post
# def createStores():
#     request_data=request.get_json()
#     new_store={"name": request_data["name"],"items":[]}
#     stores.append(new_store)
#     return {"new_store=":new_store}, 201

@app.post("/store/<store_name>/item")
def createItemInExistingStore(store_name):
    request_data = request.get_json()
    store = [ store for store in stores if store["name"] == store_name]
 
    if store:
        name = request_data["name"]
        price = request_data["price"]
        item=[item for item in store[0]["items"] if item["name"] == name]
        if(item):
            return {"message":"item already exists"},500
        else:
            new_item= {"name":name,"price":price}
            store[0]["items"].append(new_item)
            return {"new_item=":new_item},201
    return {"message":" Store name does not exists"},500