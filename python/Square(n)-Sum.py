# Menghitung jumlah kuadrat dari semua angka dalam array
def square_sum(numbers):
    if len(numbers) != 0:
        return sum([x ** 2 for x in numbers])  # Kuadratkan setiap angka lalu jumlahkan
    if len(numbers) == 0:  # Jika array kosong
        return 0
