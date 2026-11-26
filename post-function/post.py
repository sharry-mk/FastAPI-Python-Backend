from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user(name: str, age: int):
    return{
        "Name" : name,
        "Age" : age
    }

@app.post("/initialize-student")
def initialize_student(stu: dict):
    return{
        "message" : "student initialized",
        "data" : stu
    }