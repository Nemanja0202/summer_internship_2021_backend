"""create measurement table

Revision ID: 0962e56a1229
Revises: 
Create Date: 2021-06-21 16:06:55.083797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0962e56a1229'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pollution', sa.Float(), nullable=False),
    sa.Column('humidity', sa.Float(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('time_stamp', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurements')
    # ### end Alembic commands ###
