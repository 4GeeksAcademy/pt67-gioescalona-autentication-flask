"""empty message

Revision ID: e9187aa579df
Revises: e962df8dca2e
Create Date: 2024-08-23 02:36:29.692047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9187aa579df'
down_revision = 'e962df8dca2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('climate', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('created', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('diameter', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('edited', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('films', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('gravity', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('orbital_period', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('population', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('residents', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('surface_water', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('terrain', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('url', sa.String(length=120), nullable=False))
        batch_op.drop_constraint('planets_Birth_year_key', type_='unique')
        batch_op.drop_constraint('planets_Created_key', type_='unique')
        batch_op.drop_constraint('planets_Edited_key', type_='unique')
        batch_op.drop_constraint('planets_Eye_color_key', type_='unique')
        batch_op.drop_constraint('planets_Films_key', type_='unique')
        batch_op.drop_constraint('planets_Gender_key', type_='unique')
        batch_op.drop_constraint('planets_Hair_color_key', type_='unique')
        batch_op.drop_constraint('planets_Heigh_key', type_='unique')
        batch_op.drop_constraint('planets_Homeworld_key', type_='unique')
        batch_op.drop_constraint('planets_Mass_key', type_='unique')
        batch_op.drop_constraint('planets_Name_key', type_='unique')
        batch_op.drop_constraint('planets_Skin_color_key', type_='unique')
        batch_op.drop_constraint('planets_Species_key', type_='unique')
        batch_op.drop_constraint('planets_Starships_key', type_='unique')
        batch_op.drop_constraint('planets_Url_key', type_='unique')
        batch_op.drop_constraint('planets_Vehicles_key', type_='unique')
        batch_op.create_unique_constraint(None, ['gravity'])
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_unique_constraint(None, ['orbital_period'])
        batch_op.create_unique_constraint(None, ['climate'])
        batch_op.create_unique_constraint(None, ['population'])
        batch_op.create_unique_constraint(None, ['residents'])
        batch_op.create_unique_constraint(None, ['created'])
        batch_op.create_unique_constraint(None, ['surface_water'])
        batch_op.create_unique_constraint(None, ['terrain'])
        batch_op.create_unique_constraint(None, ['url'])
        batch_op.create_unique_constraint(None, ['diameter'])
        batch_op.create_unique_constraint(None, ['edited'])
        batch_op.create_unique_constraint(None, ['films'])
        batch_op.drop_column('Birth_year')
        batch_op.drop_column('Films')
        batch_op.drop_column('Skin_color')
        batch_op.drop_column('Hair_color')
        batch_op.drop_column('Vehicles')
        batch_op.drop_column('Created')
        batch_op.drop_column('Gender')
        batch_op.drop_column('Species')
        batch_op.drop_column('Url')
        batch_op.drop_column('Eye_color')
        batch_op.drop_column('Homeworld')
        batch_op.drop_column('Name')
        batch_op.drop_column('Edited')
        batch_op.drop_column('Starships')
        batch_op.drop_column('Heigh')
        batch_op.drop_column('Mass')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Mass', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Heigh', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Starships', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Edited', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Name', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Homeworld', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Eye_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Url', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Species', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Gender', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Created', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Vehicles', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Hair_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Skin_color', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Films', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('Birth_year', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
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
        batch_op.create_unique_constraint('planets_Vehicles_key', ['Vehicles'])
        batch_op.create_unique_constraint('planets_Url_key', ['Url'])
        batch_op.create_unique_constraint('planets_Starships_key', ['Starships'])
        batch_op.create_unique_constraint('planets_Species_key', ['Species'])
        batch_op.create_unique_constraint('planets_Skin_color_key', ['Skin_color'])
        batch_op.create_unique_constraint('planets_Name_key', ['Name'])
        batch_op.create_unique_constraint('planets_Mass_key', ['Mass'])
        batch_op.create_unique_constraint('planets_Homeworld_key', ['Homeworld'])
        batch_op.create_unique_constraint('planets_Heigh_key', ['Heigh'])
        batch_op.create_unique_constraint('planets_Hair_color_key', ['Hair_color'])
        batch_op.create_unique_constraint('planets_Gender_key', ['Gender'])
        batch_op.create_unique_constraint('planets_Films_key', ['Films'])
        batch_op.create_unique_constraint('planets_Eye_color_key', ['Eye_color'])
        batch_op.create_unique_constraint('planets_Edited_key', ['Edited'])
        batch_op.create_unique_constraint('planets_Created_key', ['Created'])
        batch_op.create_unique_constraint('planets_Birth_year_key', ['Birth_year'])
        batch_op.drop_column('url')
        batch_op.drop_column('terrain')
        batch_op.drop_column('surface_water')
        batch_op.drop_column('residents')
        batch_op.drop_column('population')
        batch_op.drop_column('orbital_period')
        batch_op.drop_column('name')
        batch_op.drop_column('gravity')
        batch_op.drop_column('films')
        batch_op.drop_column('edited')
        batch_op.drop_column('diameter')
        batch_op.drop_column('created')
        batch_op.drop_column('climate')

    # ### end Alembic commands ###
