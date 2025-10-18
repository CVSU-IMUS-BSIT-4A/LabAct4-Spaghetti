from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(
    title="Inventory and Sales API",
    description="A simple FastAPI application for managing inventory and sales.",
    version="activity v2"
)

# ----- Data Model -----
class InventoryItem(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

# ----- Sample Inventory -----
inventory = {
    1: {
        "Name": "Intel i5 11th Gen",
        "Price": "10000",
        "Description": "Intel i5 11th Gen is a processor that is used in laptops and desktops.",
    },
    2: {
        "Name": "AMD Ryzen 5 5600G",
        "Price": "10000",
        "Description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops.",
    },
    3: {
        "Name": "AMD Ryzen 7 5800H",
        "Price": "10000",
        "Description": "AMD Ryzen 7 5800H is a processor that is used in laptops and desktops.",
    },
}

# ----- Endpoints -----

@app.get("/home/")
def home():
    return {
        "Team Spaghetti": [
            "Member 1 - Paul",
            "Member 2 - Joseph Edrick",
            "Member 3 - Chris",
            "Member 4 - Renz",
            "Member 5 - Michael",
            "Member 5 - Nathaniel",
        ],
        "message": "Welcome to the Inventory and Sales of Team Spaghetti API"
    }

@app.get("/get_inventory/")
def get_inventory():
    if not inventory:
        raise HTTPException(status_code=404, detail="No items found in inventory.")
    return {"inventory": list(inventory.values())}

@app.get("/get_inventory/{item_id}")
def get_inventory_by_id(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item": inventory[item_id]}

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, response: Response):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del inventory[item_id]
    return Response(status_code=204)
