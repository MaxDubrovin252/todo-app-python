from fastapi import FastAPI
import uvicorn 
from api_v1.todo import todo_router
app = FastAPI()


app.include_router(router=todo_router)



if __name__=="__main__":
    uvicorn.run("main:app", reload=True)
