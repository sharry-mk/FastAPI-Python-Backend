from fastapi import FastAPI

app = FastAPI()

#this file contains some applications of query parameters

# optional parameter
@app.get("/users")
def display_user(user_id:int = None):
    return {'User id':user_id}

# default parameter
@app.get("/products")
def display_limit(limit: int = 10):
    return {"Limit" : limit}

# multiple parameter
@app.get('/items')
def get_users(name:str = None, price:int = 0):
    return{
        "name" : name,
        "Price" : price
    }   