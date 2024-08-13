from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    declared_attr,
)

from core.utils import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    """
    Возвращает:

        str: Название таблицы в формате snake_case.
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"

    id: Mapped[int] = mapped_column(primary_key=True)
