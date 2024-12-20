"""membuat model database

Revision ID: 97df4454a021
Revises: 
Create Date: 2024-12-20 21:51:47.392795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97df4454a021'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('berat_badan_umur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jenis_kelamin', sa.Enum('laki-laki', 'perempuan'), nullable=False),
    sa.Column('umur_bulan', sa.Integer(), nullable=False),
    sa.Column('minus_3_sd', sa.Float(), nullable=False),
    sa.Column('minus_2_sd', sa.Float(), nullable=False),
    sa.Column('minus_1_sd', sa.Float(), nullable=False),
    sa.Column('median', sa.Float(), nullable=False),
    sa.Column('plus_1_sd', sa.Float(), nullable=False),
    sa.Column('plus_2_sd', sa.Float(), nullable=False),
    sa.Column('plus_3_sd', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('indeks_massa_tubuh',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jenis_kelamin', sa.Enum('laki-laki', 'perempuan'), nullable=False),
    sa.Column('umur_bulan', sa.Integer(), nullable=False),
    sa.Column('minus_3_sd', sa.Float(), nullable=False),
    sa.Column('minus_2_sd', sa.Float(), nullable=False),
    sa.Column('minus_1_sd', sa.Float(), nullable=False),
    sa.Column('median', sa.Float(), nullable=False),
    sa.Column('plus_1_sd', sa.Float(), nullable=False),
    sa.Column('plus_2_sd', sa.Float(), nullable=False),
    sa.Column('plus_3_sd', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tinggi_badan_umur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jenis_kelamin', sa.Enum('laki-laki', 'perempuan'), nullable=False),
    sa.Column('umur_bulan', sa.Integer(), nullable=False),
    sa.Column('minus_3_sd', sa.Float(), nullable=False),
    sa.Column('minus_2_sd', sa.Float(), nullable=False),
    sa.Column('minus_1_sd', sa.Float(), nullable=False),
    sa.Column('median', sa.Float(), nullable=False),
    sa.Column('plus_1_sd', sa.Float(), nullable=False),
    sa.Column('plus_2_sd', sa.Float(), nullable=False),
    sa.Column('plus_3_sd', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama_lengkap', sa.String(length=255), nullable=False),
    sa.Column('umur_bulan', sa.Integer(), nullable=False),
    sa.Column('jenis_kelamin', sa.Enum('laki-laki', 'perempuan'), nullable=False),
    sa.Column('tinggi_badan', sa.Float(), nullable=False),
    sa.Column('berat_badan', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('diagnosis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hasil_bb_u', sa.String(length=100), nullable=False),
    sa.Column('hasil_tb_u', sa.String(length=100), nullable=False),
    sa.Column('hasil_imt_u', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diagnosis')
    op.drop_table('users')
    op.drop_table('tinggi_badan_umur')
    op.drop_table('indeks_massa_tubuh')
    op.drop_table('berat_badan_umur')
    # ### end Alembic commands ###
