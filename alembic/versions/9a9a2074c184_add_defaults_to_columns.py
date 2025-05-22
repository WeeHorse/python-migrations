"""Add defaults to columns

Revision ID: 9a9a2074c184
Revises: 39fc872afe3c
Create Date: 2025-05-23 00:54:52.718868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a9a2074c184'
down_revision: Union[str, None] = '39fc872afe3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'customers', 'approved',
        existing_type=sa.Boolean(),
        server_default=sa.text("False")
    )
    op.alter_column(
        'accounts', 'balance',
        existing_type=sa.Integer(),
        server_default=sa.text("0")
    )
    op.alter_column(
        'transactions', 'amount',
        existing_type=sa.Boolean(),
        server_default=sa.text("0")
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'customers', 'approved',
        existing_type=sa.Boolean(),
        server_default=None
    )
    op.alter_column(
        'accounts', 'balance',
        existing_type=sa.Integer(),
        server_default=None
    )
    op.alter_column(
        'transactions', 'amount',
        existing_type=sa.Boolean(),
        server_default=None
    )

