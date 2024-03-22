from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(
    AsyncAttrs, DeclarativeBase
):
    pass


class Auth(Base):
    __tablename__ = "auth"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
