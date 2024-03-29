"""add image path to database

Revision ID: 230e787ebbc3
Revises: fe5ad212d0b1
Create Date: 2019-09-24 09:12:23.674225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230e787ebbc3'
down_revision = 'fe5ad212d0b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'image_file')
    # ### end Alembic commands ###
