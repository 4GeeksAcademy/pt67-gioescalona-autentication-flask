"""empty message

Revision ID: 2ad3ef10fcb8
Revises: e19583cd5957
Create Date: 2024-08-23 02:07:17.740681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad3ef10fcb8'
down_revision = 'e19583cd5957'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Birth_year', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Eye_color', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Films', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Gender', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Hair_color', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Heigh', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Homeworld', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Mass', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Skin_color', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Created', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Edited', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Species', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Starships', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Url', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('Vehicles', sa.String(length=120), nullable=False))
        batch_op.drop_constraint('characters_author_key', type_='unique')
        batch_op.drop_constraint('characters_category_key', type_='unique')
        batch_op.drop_constraint('characters_description_key', type_='unique')
        batch_op.drop_constraint('characters_title_key', type_='unique')
        batch_op.drop_constraint('characters_url_video_key', type_='unique')
        batch_op.create_unique_constraint(None, ['Gender'])
        batch_op.create_unique_constraint(None, ['Edited'])
        batch_op.create_unique_constraint(None, ['Films'])
        batch_op.create_unique_constraint(None, ['Created'])
        batch_op.create_unique_constraint(None, ['Skin_color'])
        batch_op.create_unique_constraint(None, ['Name'])
        batch_op.create_unique_constraint(None, ['Eye_color'])
        batch_op.create_unique_constraint(None, ['Mass'])
        batch_op.create_unique_constraint(None, ['Vehicles'])
        batch_op.create_unique_constraint(None, ['Homeworld'])
        batch_op.create_unique_constraint(None, ['Birth_year'])
        batch_op.create_unique_constraint(None, ['Url'])
        batch_op.create_unique_constraint(None, ['Heigh'])
        batch_op.create_unique_constraint(None, ['Starships'])
        batch_op.create_unique_constraint(None, ['Hair_color'])
        batch_op.create_unique_constraint(None, ['Species'])
        batch_op.drop_column('category')
        batch_op.drop_column('author')
        batch_op.drop_column('description')
        batch_op.drop_column('title')
        batch_op.drop_column('url_video')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url_video', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('description', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('characters_url_video_key', ['url_video'])
        batch_op.create_unique_constraint('characters_title_key', ['title'])
        batch_op.create_unique_constraint('characters_description_key', ['description'])
        batch_op.create_unique_constraint('characters_category_key', ['category'])
        batch_op.create_unique_constraint('characters_author_key', ['author'])
        batch_op.drop_column('Vehicles')
        batch_op.drop_column('Url')
        batch_op.drop_column('Starships')
        batch_op.drop_column('Species')
        batch_op.drop_column('Edited')
        batch_op.drop_column('Created')
        batch_op.drop_column('Skin_color')
        batch_op.drop_column('Name')
        batch_op.drop_column('Mass')
        batch_op.drop_column('Homeworld')
        batch_op.drop_column('Heigh')
        batch_op.drop_column('Hair_color')
        batch_op.drop_column('Gender')
        batch_op.drop_column('Films')
        batch_op.drop_column('Eye_color')
        batch_op.drop_column('Birth_year')

    # ### end Alembic commands ###
