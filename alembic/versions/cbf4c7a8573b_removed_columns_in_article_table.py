"""removed columns in article table

Revision ID: cbf4c7a8573b
Revises: 017d244117b1
Create Date: 2023-09-03 20:06:09.117472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbf4c7a8573b'
down_revision: Union[str, None] = '017d244117b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
