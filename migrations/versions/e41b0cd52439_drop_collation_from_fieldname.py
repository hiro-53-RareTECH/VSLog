"""drop collation from fieldname

Revision ID: e41b0cd52439
Revises: 1714a54ab229
Create Date: 2026-03-31 16:37:17.900638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e41b0cd52439'
down_revision = '1714a54ab229'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE fields
        MODIFY COLUMN fieldname VARCHAR(20)
        NOT NULL
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE fields
        MODIFY COLUMN fieldname VARCHAR(20)
        COLLATE utf8mb4_general_ci
        NOT NULL
        """
    )
