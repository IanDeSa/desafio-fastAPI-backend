"""create product table

Revision ID: 0b6a827780ec
Revises: 
Create Date: 2023-01-27 13:08:38.121374

"""
from alembic import op
import sqlalchemy as sa
from migrations.data_table.product import product_data
from migrations.populate_table import populate_table


# revision identifiers, used by Alembic.
revision = "0b6a827780ec"
down_revision = None
branch_labels = None
depends_on = None


table_name = "product"


def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(50), nullable=False),
        sa.Column("price", sa.String(50), nullable=False),
        sa.Column("status", sa.Boolean, nullable=False),
    )

    populate_table(table_name, product_data)


def downgrade() -> None:
    op.drop_table(table_name)
