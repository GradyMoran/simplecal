"""event calendar id foreign key

Revision ID: b530343e63d6
Revises: 65f07cd4a3b9
Create Date: 2020-06-28 14:06:16.236130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b530343e63d6'
down_revision = '65f07cd4a3b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        #batch_op.create_foreign_key(None, 'cal_data', ['calendar_id'], ['id'])
        batch_op.create_foreign_key('id', 'cal_data', ['calendar_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
