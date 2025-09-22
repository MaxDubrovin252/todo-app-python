from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .todo import Todo
    
class User(Base):
    username:Mapped[str] = mapped_column(unique=True)
    password:Mapped[bytes]
    
    todos:Mapped[list["Todo"]] = relationship("Todo", back_populates="user")