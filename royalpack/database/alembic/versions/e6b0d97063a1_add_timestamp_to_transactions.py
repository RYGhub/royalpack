"""Add timestamp to transactions

Revision ID: e6b0d97063a1
Revises: c6aacbd5d796
Create Date: 2021-04-25 02:18:44.248837

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e6b0d97063a1'
down_revision = 'c6aacbd5d796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fiorygi_transactions',
                  sa.Column('timestamp', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True))
    op.add_column('fiorygi_treasures',
                  sa.Column('creation_time', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False))
    op.add_column('fiorygi_treasures', sa.Column('find_time', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fiorygi_treasures', 'find_time')
    op.drop_column('fiorygi_treasures', 'creation_time')
    op.drop_column('fiorygi_transactions', 'timestamp')
    # ### end Alembic commands ###
