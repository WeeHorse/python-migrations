"""customer approved before transaction function and constraint

Revision ID: 39fc872afe3c
Revises: 996c30c137ed
Create Date: 2025-05-22 13:52:18.940686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39fc872afe3c'
down_revision: Union[str, None] = '996c30c137ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        CREATE OR REPLACE FUNCTION check_customer_approved()
        RETURNS TRIGGER AS $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM customers WHERE id = NEW.customer_id AND approved = TRUE
            ) THEN
                RAISE EXCEPTION 'Kund är inte godkänd';
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
        
        CREATE TRIGGER validate_transaction
        BEFORE INSERT ON transactions
        FOR EACH ROW
        EXECUTE FUNCTION check_customer_approved();
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TRIGGER IF EXISTS validate_transaction ON transactions")
