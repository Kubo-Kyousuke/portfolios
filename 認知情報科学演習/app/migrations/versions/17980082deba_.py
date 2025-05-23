"""empty message

Revision ID: 17980082deba
Revises: 2687104df806
Create Date: 2024-12-19 05:41:40.741856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17980082deba'
down_revision = '2687104df806'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('timing_hours')
        batch_op.drop_column('timing_minutes')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timing_hours', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('timing_minutes', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('timing_minutes')
        batch_op.drop_column('timing_hours')

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timing_minutes', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('timing_hours', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
