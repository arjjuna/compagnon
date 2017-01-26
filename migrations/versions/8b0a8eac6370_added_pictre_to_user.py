"""added pictre to user

Revision ID: 8b0a8eac6370
Revises: a3e205aed75f
Create Date: 2017-01-17 20:08:34.774000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b0a8eac6370'
down_revision = 'a3e205aed75f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('picture', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'picture')
    # ### end Alembic commands ###
