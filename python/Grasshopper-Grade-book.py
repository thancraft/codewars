# Menghitung grade berdasarkan rata-rata 3 nilai
def get_grade(s1, s2, s3):
    total = s1 + s2 + s3
    rata_rata = total / 3
    hasil = ""
    
    # Tentukan grade berdasarkan rentang rata-rata
    if 90 <= rata_rata <= 100:
        hasil = "A"
    elif 80 <= rata_rata < 90:
        hasil = "B"
    elif 70 <= rata_rata < 80:
        hasil = "C"
    elif 60 <= rata_rata < 70:
        hasil = "D"
    elif 0 <= rata_rata < 60:
        hasil = "F"
    
    return hasil