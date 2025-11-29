# Menentukan kuartal tahun berdasarkan bulan (1-12)
def quarter_of(month):
    if month == 1 or month == 2 or month == 3:  # Q1: Jan-Mar
        return 1
    if month == 4 or month == 5 or month == 6:  # Q2: Apr-Jun
        return 2
    if month == 7 or month == 8 or month == 9:  # Q3: Jul-Sep
        return 3
    if month == 10 or month == 11 or month == 12:  # Q4: Oct-Dec
        return 4

