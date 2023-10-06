"""Wagwan Fam?

Revision ID: 7f4d8c85eec3
Revises: 94ecd9711e46
Create Date: 2023-10-06 02:36:39.545272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f4d8c85eec3'
down_revision = '94ecd9711e46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_investments')
    with op.batch_alter_table('investments', schema=None) as batch_op:
        batch_op.alter_column('investor_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('profitandloss', schema=None) as batch_op:
        batch_op.alter_column('investment_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('investor_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profitandloss', schema=None) as batch_op:
        batch_op.alter_column('investor_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('investment_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('investments', schema=None) as batch_op:
        batch_op.alter_column('investor_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    op.create_table('_alembic_tmp_investments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('investor_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('amount', sa.FLOAT(), nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['investor_id'], ['investors.id'], name='fk_investments_investor_id_investors'),
    sa.PrimaryKeyConstraint('id', name='pk_investments')
    )
    # ### end Alembic commands ###
