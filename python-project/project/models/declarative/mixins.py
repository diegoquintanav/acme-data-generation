import sqlalchemy as sa
from sqlalchemy import inspect


class ReprMixin(object):
    """A mixin to implement a generic __repr__ method"""

    def __repr__(self):
        inspector = inspect(self.__class__)
        return "%s(%s)" % (
            self.__class__.__name__,
            ", ".join([f"{c}={getattr(self, c)}" for c in inspector.attrs.keys()]),
        )


class GhostIdMixin(object):
    """Implements a dummy id to make sqlalchemy work.
    
    This id is not meant to be used at the DB level"""

    ghost_id = sa.Column("id", sa.Integer, primary_key=True)