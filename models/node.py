import sqlalchemy as sa
from config import metadata, Base


class Node(Base):
    __tablename__ = 'nodes'
    id = sa.Column(sa.String(50), primary_key=True)
    group = sa.Column(sa.ForeignKey("groups.id"))

    def __str__(self) -> str:
        return self.id
    
    def serialize(self) -> dict:
        return {
            "id": self.id,
            "group": self.group
        }
