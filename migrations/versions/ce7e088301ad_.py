"""empty message

Revision ID: ce7e088301ad
Revises: 62ea444d5931
Create Date: 2023-08-08 11:31:11.396825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce7e088301ad'
down_revision = '62ea444d5931'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Source', schema=None) as batch_op:
        batch_op.alter_column('created',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('status_change',
               existing_type=sa.DATE(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Source', schema=None) as batch_op:
        batch_op.alter_column('status_change',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=False)
        batch_op.alter_column('created',
               existing_type=sa.String(),
               type_=sa.DATE(),
               existing_nullable=False)

    # ### end Alembic commands ###
