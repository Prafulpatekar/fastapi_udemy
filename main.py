from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def index():
    return {"message":"Hello World!"}

@app.post('/hello')
def index2():
    return "Hi!"

# command to run 
# if myApp = FastAPI()
# then => uvicorn main:myApp --reload
# => uvicorn main:app --reload