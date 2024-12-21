

# rumus menghitung Indeks Massa Tubuh
def IMTCalc(weight:float, height:float):
    return weight/((height/100)**2)

# kategori berat badan berdasarkan umur
def categoryBBU(weight:float, minus_3_sd:float, minus_2_sd:float, plus_1_sd:float):
    if weight < minus_3_sd:
        return "Berat badan sangat kurang"
    elif minus_3_sd <= weight < minus_2_sd:
        return "Berat badan kurang"
    elif minus_2_sd <= weight < plus_1_sd:
        return "Berat badan normal"
    else:
        return "Resiko berat badan lebih"

# kategori tinggi badan berdasarkan umur
def categoryTBU(height:float, minus_3_sd:float, minus_2_sd:float, plus_3_sd:float):
    if height < minus_3_sd:
        return "Stunting parah"
    elif minus_3_sd <= height < minus_2_sd:
        return "Stunting"
    elif minus_2_sd <= height < plus_3_sd:
        return "Normal"
    else:
        return "Tinggi"

# kategori indeks massa tubuh berdasarkan umur
def categoryIMTU(imt:float, minus_3_sd:float, minus_2_sd:float, plus_1_sd:float, plus_2_sd:float, plus_3_sd:float):
    if imt < minus_3_sd:
        return "Gizi buruk"
    elif minus_3_sd <= imt < minus_2_sd:
        return "Gizi kurang"
    elif minus_2_sd <= imt < plus_1_sd:
        return "Normal"
    elif plus_1_sd <= imt < plus_2_sd:
        return "Beresiko gizi lebih"
    elif plus_2_sd <= imt < plus_3_sd:
        return "Gizi lebih"
    else:
        return "Obesitas"