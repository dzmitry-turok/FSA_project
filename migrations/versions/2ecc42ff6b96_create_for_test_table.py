"""create for test table

Revision ID: 2ecc42ff6b96
Revises: 
Create Date: 2021-06-15 23:21:01.047373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ecc42ff6b96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table('test_table')
