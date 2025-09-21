from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    title:str
    description:str 

    
class Todo(TodoBase):
    model_config = ConfigDict(from_attributes=True)
    id:int
    
class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    title:str | None = None
    description:str | None = None
    status:str | None = None
    
class TodoUpdateAll(TodoBase):
    pass