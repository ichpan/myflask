"""initial migration

Revision ID: 53dc70cebdf8
Revises: 0ab43b31ee48
Create Date: 2023-04-20 12:26:58.546755

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '53dc70cebdf8'
down_revision = '0ab43b31ee48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.drop_column('is_super')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('t_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_super', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###