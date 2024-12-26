# penghubung models dan view
from flask import render_template, request, redirect, url_for
from project.utils.calc import IMTCalc, categoryBBU, categoryTBU, categoryIMTU
from project.models import Users, Diagnosis, BeratBadanUmur, TinggiBadanUmur, IndeksMassaTubuh
from project.utils.groq_ai import getAnswerAI


def indexPage():
    return render_template('index.html')

def insertData():
    # inisialisasi hasil diagnosis
    category_bb_u = None
    category_tb_u = None
    category_imt_u = None
    ai_answer = None
    
    # jika form sudah disubmit
    if request.method == 'POST':
        # mengambil input dari user
        complete_name = request.form['nama_lengkap']
        sex = request.form['jenis_kelamin']
        month_age = int(request.form['umur_bulan'])
        height = float(request.form['tinggi_badan'])
        weight = float(request.form['berat_badan'])
        
        # mengambil data yang sesuai dengan database acuan
        bb_u = BeratBadanUmur.getBySexAge(jenis_kelamin=sex, umur_bulan=month_age)
        tb_u = TinggiBadanUmur.getBySexAge(jenis_kelamin=sex, umur_bulan=month_age)
        imt_u = IndeksMassaTubuh.getBySexAge(jenis_kelamin=sex, umur_bulan=month_age)
        
        # hasil diagnosis
        category_bb_u = categoryBBU(weight, bb_u.minus_3_sd, bb_u.minus_2_sd, bb_u.plus_1_sd)
        category_tb_u = categoryTBU(height, tb_u.minus_3_sd, tb_u.minus_2_sd, tb_u.plus_3_sd)
        category_imt_u = categoryIMTU(IMTCalc(weight=weight, height=height), imt_u.minus_3_sd, imt_u.minus_2_sd, imt_u.plus_1_sd, imt_u.plus_2_sd, imt_u.plus_3_sd)
        
        # Cek apakah user sudah ada
        check_user = Users.checkUser(nama_lengkap=complete_name)
        
        # jika ada gunakan user itu, jika tidak ada maka buat user baru 
        # masukkan ke database
        if check_user:
            new_user = check_user
        else:
            new_user = Users.insertUser(complete_name, sex)
        new_diagnoses = Diagnosis.insertDiagnosis(month_age, height, weight, category_bb_u, category_tb_u, category_imt_u, new_user.id)
        ai_answer = getAnswerAI(month_age, category_bb_u, category_tb_u, category_imt_u)
    return render_template('cek_stunt.html', category_bb_u=category_bb_u, category_tb_u=category_tb_u, category_imt_u=category_imt_u, ai_answer=ai_answer)