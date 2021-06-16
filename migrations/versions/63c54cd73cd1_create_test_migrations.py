"""create test migrations

Revision ID: 63c54cd73cd1
Revises: 2ecc42ff6b96
Create Date: 2021-06-15 23:21:48.473376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63c54cd73cd1'
down_revision = '2ecc42ff6b96'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('users')
