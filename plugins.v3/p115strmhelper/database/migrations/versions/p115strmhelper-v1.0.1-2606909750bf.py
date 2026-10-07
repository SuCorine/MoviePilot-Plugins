"""1.0.1

Revision ID: 2606909750bf
Revises: 294b0079357e
Create Date: 2025-08-29 15:05:49.254548

"""

from alembic import op


# revision identifiers, used by Alembic
version = "1.0.1"
revision = "2606909750bf"
down_revision = "294b0079357e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 兼容 SQLite / PostgreSQL：SQLite 用 rowid，PostgreSQL 用 ctid（MP 底座为 PostgreSQL）
    _rid = "ctid" if op.get_bind().dialect.name == "postgresql" else "rowid"
    op.execute(f"""
        DELETE FROM files
        WHERE {_rid} NOT IN (
            SELECT MIN({_rid})
            FROM files
            GROUP BY path
        );
    """)

    op.execute(f"""
        DELETE FROM folders
        WHERE {_rid} NOT IN (
            SELECT MIN({_rid})
            FROM folders
            GROUP BY path
        );
    """)

    with op.batch_alter_table("files", schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f("uq_files_path"), ["path"])

    with op.batch_alter_table("folders", schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f("uq_folders_path"), ["path"])


def downgrade() -> None:
    with op.batch_alter_table("files", schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f("uq_files_path"), type_="unique")

    with op.batch_alter_table("folders", schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f("uq_folders_path"), type_="unique")
