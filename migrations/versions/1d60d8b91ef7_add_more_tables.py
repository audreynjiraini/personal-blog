"""Add more tables

Revision ID: 1d60d8b91ef7
Revises: 
Create Date: 2019-09-23 12:39:41.383496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d60d8b91ef7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('post_id', sa.Integer(), nullable=True))
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    op.add_column('comments', sa.Column('blog_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_blog_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'])
    op.drop_column('comments', 'blog')
    op.add_column('users', sa.Column('password_hash', sa.String(length=60), nullable=False))
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.drop_column('users', 'image_file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('image_file', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    op.drop_column('users', 'password_hash')
    op.add_column('comments', sa.Column('blog', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_fkey', 'comments', 'blogs', ['blog'], ['id'])
    op.drop_column('comments', 'blog_id')
    op.add_column('blogs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    op.drop_column('blogs', 'post_id')
    # ### end Alembic commands ###
