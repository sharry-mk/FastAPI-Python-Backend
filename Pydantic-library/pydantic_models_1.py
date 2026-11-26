from fastapi import FastAPI
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    id: int
    salary: float

app = FastAPI()

@app.post("/Employee-Creation")
def create_employee(emp: Employee):
    return{
        "message" : "Employee created successfully",
        "data" : emp
    }


class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name : str
    age : int
    address : Address

@app.post("/Create User")
def create_user(user: User):
    return{
        "Message": "User created",
        "Data" : user
    }