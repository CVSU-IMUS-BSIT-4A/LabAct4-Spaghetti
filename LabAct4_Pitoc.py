from fastapi import FastAPI, HTTPException, Query, Response
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
    1: {"Name": "Intel i5 11th Gen",
        "Price": "10000",
        "Description": "Intel i5 11th Gen is a processor that is used in laptops and desktops.",
        },
    2: {"Name": "AMD Ryzen 5 5600G",
        "Price": "10000",
        "Description": "AMD Ryzen 5 5600G is a processor that is used in laptops and desktops.",
        },
    3: {"Name": "AMD Ryzen 7 5800H",
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

# Get all items
@app.get("/get_inventory/")
def get_inventory():
    if not inventory:
        raise HTTPException(status_code=404, detail="No items found in inventory.")
    return {"inventory": list(inventory.values())}

# Get single item by ID
@app.get("/get_inventory/{item_id}")
def get_inventory_by_id(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    return {"item": inventory[item_id]}

# Create new item
@app.post("/create_inventory/", status_code=201)
def create_inventory(item: InventoryItem):
    if item.id in inventory:
        raise HTTPException(status_code=400, detail="Item already exists.")
    inventory[item.id] = item.dict()
    return {"message": "Item created successfully.", "item": item}

# Update existing item
@app.put("/update_inventory/")
def update_inventory(item: InventoryItem):
    if item.id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    inventory[item.id] = item.dict()
    return {"message": "Item updated successfully.", "item": item}

# ----- DELETE item -----
@app.delete("/delete_inventory/{item_id}")
def delete_inventory(item_id: int, response: Response):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    # Remove item
    del inventory[item_id]

    # Return 204 No Content with empty body
    response.status_code = 204
    return Response(status_code=204)

# ----- Run Server -----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Lab3:app", host="127.0.0.1", port=8000, reload=True)
  
