from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class Todo(Base):
    title:Mapped[str]= mapped_column(String(32))
    description:Mapped[str] = mapped_column(String(128))
    status:Mapped[str] 