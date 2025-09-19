from fastapi import FastAPI
import uvicorn 
from api_v1.todo import todo_router
from api_v1.auth.user import router as auth_router
app = FastAPI()


app.include_router(router=todo_router)
app.include_router(router=auth_router)




if __name__=="__main__":
    uvicorn.run("main:app", reload=True)
