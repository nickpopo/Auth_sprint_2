"""Google user unique constraints

Revision ID: ec1b9d5dd8d2
Revises: 0d9047d7b945
Create Date: 2021-08-05 09:26:48.481854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1b9d5dd8d2'
down_revision = '0d9047d7b945'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'google_user', ['email'])
    op.create_unique_constraint(None, 'google_user', ['user_id'])
    op.create_unique_constraint(None, 'google_user', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'google_user', type_='unique')
    op.drop_constraint(None, 'google_user', type_='unique')
    op.drop_constraint(None, 'google_user', type_='unique')
    # ### end Alembic commands ###
