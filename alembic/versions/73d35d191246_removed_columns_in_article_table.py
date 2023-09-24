"""removed columns in article table

Revision ID: 73d35d191246
Revises: cbf4c7a8573b
Create Date: 2023-09-03 20:08:51.672712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73d35d191246'
down_revision: Union[str, None] = 'cbf4c7a8573b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
