from pydantic import BaseModel

class TodoBase(BaseModel):
    title:str
    description:str 
    status:str
    
class Todo(TodoBase):
    id:int
    
class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title:str | None = None
    description:str | None = None
    status:str | None = None