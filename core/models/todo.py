from .base import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User



class Todo(Base):
    title:Mapped[str]= mapped_column(String(32))
    description:Mapped[str] = mapped_column(String(128))
    status:Mapped[str] 
    
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    user:Mapped["User"] = relationship("User", back_populates="todos")