"""empty message

Revision ID: daae8baa9733
Revises: e740e5731229
Create Date: 2019-04-13 13:17:11.793322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daae8baa9733'
down_revision = 'e740e5731229'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('summary', sa.Text(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_articles_title'), 'articles', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_articles_title'), table_name='articles')
    op.drop_table('articles')
    # ### end Alembic commands ###
