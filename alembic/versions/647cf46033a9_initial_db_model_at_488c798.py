"""initial DB model at 488c798

Revision ID: 647cf46033a9
Revises: 
Create Date: 2019-09-14 23:56:13.526547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '647cf46033a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hostname', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('processhandler', sa.String(length=1024), nullable=True),
    sa.Column('processname', sa.String(length=1024), nullable=True),
    sa.Column('event_type', sa.String(length=256), nullable=True),
    sa.Column('event_time', sa.DateTime(), nullable=True),
    sa.Column('process_start_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('process_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=256), nullable=True),
    sa.Column('hostname', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.Column('processhandler', sa.String(length=1024), nullable=True),
    sa.Column('processname', sa.String(length=1024), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rule_override',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('reference_date', sa.Date(), nullable=True),
    sa.Column('max_time_per_day', sa.Integer(), nullable=True),
    sa.Column('min_time_of_day', sa.Time(), nullable=True),
    sa.Column('max_time_of_day', sa.Time(), nullable=True),
    sa.Column('min_break', sa.Integer(), nullable=True),
    sa.Column('free_play', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rule_override')
    op.drop_table('process_info')
    op.drop_table('admin_event')
    # ### end Alembic commands ###