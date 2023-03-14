"""empty message

Revision ID: 814181657bd5
Revises: 1646cdb5353d
Create Date: 2023-03-14 23:08:34.090378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814181657bd5'
down_revision = '1646cdb5353d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
