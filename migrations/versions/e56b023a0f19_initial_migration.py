"""initial migration

Revision ID: e56b023a0f19
Revises: 
Create Date: 2023-06-03 19:12:47.261655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56b023a0f19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False, comment='用户名'),
    sa.Column('password', sa.String(length=256), nullable=False, comment='密码'),
    sa.Column('role', sa.Integer(), nullable=True, comment='角色'),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('mobile', sa.String(length=16), nullable=True, comment='手机号'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('t_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False, comment='角色名'),
    sa.Column('uid', sa.Integer(), nullable=True, comment='用戶id'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['uid'], ['t_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_role')
    op.drop_table('t_user')
    # ### end Alembic commands ###