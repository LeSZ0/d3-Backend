import sqlalchemy as sa
from config import metadata, Base


class Group(Base):
    __tablename__ = 'groups'
    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(150))
    is_active = sa.Column(sa.Boolean(), default=True)

    def __str__(self) -> str:
        return self.name

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "is_active": self.is_active
        }
