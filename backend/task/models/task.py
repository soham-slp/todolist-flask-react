from config import db
from sqlalchemy import String, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import datetime
from utils import to_jsondate

class Task(db.Model):
    __tablename__ = "Tasks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(60))
    due: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    complete: Mapped[bool] = mapped_column(Boolean, default=False)
    