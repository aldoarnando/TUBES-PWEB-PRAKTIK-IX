from project.app import db


class Users(db.Model):
    # nama tabel
    __tablename__ = 'users'
    
    # mendefinisikan nama-nama kolom
    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(255), nullable=False)
    jenis_kelamin = db.Column(db.Enum('laki-laki', 'perempuan'), nullable=False)
    
    # membuat relasi setiap user memiliki diagnosis
    relation_diagnosis = db.relationship('Diagnosis', back_populates='relation_user', cascade='all, delete-orphan')
    
    def __init__(self, nama_lengkap:str, jenis_kelamin:str):
        self.nama_lengkap = nama_lengkap
        self.jenis_kelamin = jenis_kelamin
        
    @staticmethod
    def insertUser(nama_lengkap:str, jenis_kelamin:str):
        user = Users(nama_lengkap=nama_lengkap, jenis_kelamin=jenis_kelamin)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def checkUser(nama_lengkap:str):
        return Users.query.filter_by(nama_lengkap=nama_lengkap).first()
    
    def __repr__(self) -> str:
        return f'<User {self.nama_lengkap}>'


class Diagnosis(db.Model):
    # nama tabel
    __tablename__ = 'diagnosis'
    
    # mendefinisikan nama-nama kolom
    id = db.Column(db.Integer, primary_key=True)
    umur_bulan = db.Column(db.Integer, nullable=False)
    tinggi_badan = db.Column(db.Float, nullable=False)
    berat_badan = db.Column(db.Float, nullable=False)
    hasil_bb_u = db.Column(db.String(100), nullable=False)
    hasil_tb_u = db.Column(db.String(100), nullable=False)
    hasil_imt_u = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # membuat relasi setiap diagnosis memiliki user
    relation_user = db.relationship('Users', back_populates='relation_diagnosis')
    
    def __init__(self, umur_bulan:int, tinggi_badan:float, berat_badan:float, hasil_bb_u:str, hasil_tb_u:str, hasil_imt_u:str, user_id:int):
        self.umur_bulan = umur_bulan
        self.tinggi_badan = tinggi_badan
        self.berat_badan = berat_badan
        self.hasil_bb_u = hasil_bb_u
        self.hasil_tb_u = hasil_tb_u
        self.hasil_imt_u = hasil_imt_u
        self.user_id = user_id
        
    @staticmethod
    def insertDiagnosis(umur_bulan:int, tinggi_badan:float, berat_badan:float, hasil_bb_u:str, hasil_tb_u:str, hasil_imt_u:str, user_id:int):
        diagnosis = Diagnosis(umur_bulan=umur_bulan, tinggi_badan=tinggi_badan, berat_badan=berat_badan, hasil_bb_u=hasil_bb_u, hasil_tb_u=hasil_tb_u, hasil_imt_u=hasil_imt_u, user_id=user_id)
        db.session.add(diagnosis)
        db.session.commit()
        return diagnosis
        
    def __repr__(self) -> str:
        return f'<User {self.nama_lengkap}>'


class BeratBadanUmur(db.Model):
    # nama tabel
    __tablename__ = 'berat_badan_umur'
    
    # mendefinisikan nama-nama kolom
    id = db.Column(db.Integer, primary_key=True)
    jenis_kelamin = db.Column(db.Enum('laki-laki', 'perempuan'), nullable=False)
    umur_bulan = db.Column(db.Integer, nullable=False)
    minus_3_sd = db.Column(db.Float, nullable=False)
    minus_2_sd = db.Column(db.Float, nullable=False)
    minus_1_sd = db.Column(db.Float, nullable=False)
    median = db.Column(db.Float, nullable=False)
    plus_1_sd = db.Column(db.Float, nullable=False)
    plus_2_sd = db.Column(db.Float, nullable=False)
    plus_3_sd = db.Column(db.Float, nullable=False)
    
    def __init__(self, jenis_kelamin:str, umur_bulan:int, minus_3_sd:float, minus_2_sd:float, minus_1_sd:float, median:float, plus_1_sd:float, plus_2_sd:float, plus_3_sd:float):
        self.jenis_kelamin = jenis_kelamin
        self.umur_bulan = umur_bulan
        self.minus_3_sd = minus_3_sd
        self.minus_2_sd = minus_2_sd
        self.minus_1_sd = minus_1_sd
        self.median = median
        self.plus_1_sd = plus_1_sd
        self.plus_2_sd = plus_2_sd
        self.plus_3_sd = plus_3_sd
        
    @staticmethod
    def getBySexAge(jenis_kelamin:str, umur_bulan:int):
        return BeratBadanUmur.query.filter_by(jenis_kelamin=jenis_kelamin, umur_bulan=umur_bulan).first()
    
    def __repr__(self) -> str:
        return f'<Berat Badan menurut Umur {self.umur_bulan} {self.jenis_kelamin}>'


class TinggiBadanUmur(db.Model):
    # nama tabel
    __tablename__ = 'tinggi_badan_umur'
    
    # mendefinisikan nama-nama kolom
    id = db.Column(db.Integer, primary_key=True)
    jenis_kelamin = db.Column(db.Enum('laki-laki', 'perempuan'), nullable=False)
    umur_bulan = db.Column(db.Integer, nullable=False)
    minus_3_sd = db.Column(db.Float, nullable=False)
    minus_2_sd = db.Column(db.Float, nullable=False)
    minus_1_sd = db.Column(db.Float, nullable=False)
    median = db.Column(db.Float, nullable=False)
    plus_1_sd = db.Column(db.Float, nullable=False)
    plus_2_sd = db.Column(db.Float, nullable=False)
    plus_3_sd = db.Column(db.Float, nullable=False)
    
    def __init__(self, jenis_kelamin:str, umur_bulan:int, minus_3_sd:float, minus_2_sd:float, minus_1_sd:float, median:float, plus_1_sd:float, plus_2_sd:float, plus_3_sd:float):
        self.jenis_kelamin = jenis_kelamin
        self.umur_bulan = umur_bulan
        self.minus_3_sd = minus_3_sd
        self.minus_2_sd = minus_2_sd
        self.minus_1_sd = minus_1_sd
        self.median = median
        self.plus_1_sd = plus_1_sd
        self.plus_2_sd = plus_2_sd
        self.plus_3_sd = plus_3_sd
        
    @staticmethod
    def getBySexAge(jenis_kelamin:str, umur_bulan:int):
        return TinggiBadanUmur.query.filter_by(jenis_kelamin=jenis_kelamin, umur_bulan=umur_bulan).first()
        
    def __repr__(self) -> str:
        return f'<Tinggi Badan menurut Umur {self.umur_bulan} {self.jenis_kelamin}>'


class IndeksMassaTubuh(db.Model):
    # nama tabel
    __tablename__ = 'indeks_massa_tubuh'
    
    # mendefinisikan nama-nama kolom
    id = db.Column(db.Integer, primary_key=True)
    jenis_kelamin = db.Column(db.Enum('laki-laki', 'perempuan'), nullable=False)
    umur_bulan = db.Column(db.Integer, nullable=False)
    minus_3_sd = db.Column(db.Float, nullable=False)
    minus_2_sd = db.Column(db.Float, nullable=False)
    minus_1_sd = db.Column(db.Float, nullable=False)
    median = db.Column(db.Float, nullable=False)
    plus_1_sd = db.Column(db.Float, nullable=False)
    plus_2_sd = db.Column(db.Float, nullable=False)
    plus_3_sd = db.Column(db.Float, nullable=False)
    
    def __init__(self, jenis_kelamin:str, umur_bulan:int, minus_3_sd:float, minus_2_sd:float, minus_1_sd:float, median:float, plus_1_sd:float, plus_2_sd:float, plus_3_sd:float):
        self.jenis_kelamin = jenis_kelamin
        self.umur_bulan = umur_bulan
        self.minus_3_sd = minus_3_sd
        self.minus_2_sd = minus_2_sd
        self.minus_1_sd = minus_1_sd
        self.median = median
        self.plus_1_sd = plus_1_sd
        self.plus_2_sd = plus_2_sd
        self.plus_3_sd = plus_3_sd
        
    @staticmethod
    def getBySexAge(jenis_kelamin:str, umur_bulan:int):
        return IndeksMassaTubuh.query.filter_by(jenis_kelamin=jenis_kelamin, umur_bulan=umur_bulan).first()
        
    def __repr__(self) -> str:
        return f'<Tinggi Badan menurut Umur {self.umur_bulan} {self.jenis_kelamin}>'
    
    
"""
Isi dari tabel:
1. berat_badan_umur = impor dari dataset WFA
1. tinggi_badan_umur = impor dari dataset HFA
1. indeks_massa_tubuh = impor dari dataset BMI
"""