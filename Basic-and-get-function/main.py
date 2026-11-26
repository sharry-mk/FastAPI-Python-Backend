# this file consists of the basic opertions on fastapi and the usage of get() function


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return "Hello fastapi !"

@app.get("/student")
def student():
    students = ["Peter", "Steve", "Tony", "Bruce"]
    
    marks = (88, 89, 97), (78, 67, 78), (98, 96, 100), (100, 100, 99)
    stu_marks = {}
    for stu, mark in zip(students, marks):
        stu_marks.setdefault(stu, mark)

    return stu_marks


@app.get("/student/marks")
def marks_of_student():
    stu_marks = student()
    marks = []
    for val in stu_marks.values():
        marks.append(val)

    return marks


# this will ask for a value to be given by the user
@app.get("/users/{user_id}")
def get_user(user_id:str):
    return {"user ID":user_id}

@app.get("/PrimeCheck/{num}")
def get_number(num:int):
    if(num <= 1):
        return f"{num} is neither prime nor composite"
    for i in range(2, int(num ** 0.5) + 1):
        if(num % i == 0):
            return f"{num} is composite"

    return f"{num} is prime"



