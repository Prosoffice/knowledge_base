"""Change in article model

Revision ID: 795c9d57f3e7
Revises: 73d35d191246
Create Date: 2023-09-03 20:11:35.474843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '795c9d57f3e7'
down_revision: Union[str, None] = '73d35d191246'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gdprarticle', 'context')
    op.drop_column('gdprarticle', 'content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gdprarticle', sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('gdprarticle', sa.Column('context', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
