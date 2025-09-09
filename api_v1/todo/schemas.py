from pydantic import BaseModel

class TodoBase(BaseModel):
    title:str
    description:str 
    status:str
    
class Todo(TodoBase):
    id:int
    
class TodoCreate(TodoBase):
    pass