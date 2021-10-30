import sqlalchemy as sa
from config import metadata, Base


class Link(Base):
    __tablename__ = 'links'

    id = sa.Column(sa.Integer, primary_key=True)
    source = sa.Column(sa.ForeignKey("nodes.id"))
    target = sa.Column(sa.ForeignKey("nodes.id"))
    value = sa.Column(sa.Integer)

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f'<Link(source={self.source}, target={self.target}>'

    def serialize(self) -> dict:
        return {
            "source": self.source,
            "target": self.target,
            "value": self.value
        }
