"""Авторизация пользователя

Revision ID: 04655e936182
Revises: 1aafdd2f43e4
Create Date: 2024-03-08 20:01:06.738670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04655e936182'
down_revision = '1aafdd2f43e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_pc_id', sa.Integer(), nullable=True))
    op.drop_constraint('user_pc_id_fkey', 'user', type_='foreignkey')
    op.create_foreign_key(None, 'user', 'user_pc', ['user_pc_id'], ['id'])
    op.drop_column('user', 'user_pc_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_pc_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_foreign_key('user_pc_id_fkey', 'user', 'user_pc', ['user_pc_id'], ['id'])
    op.drop_column('user', 'user_pc_id')
    # ### end Alembic commands ###