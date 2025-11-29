# Menambahkan nomor urut di depan setiap baris (dimulai dari 1)
def number(lines):
    # enumerate(lines, start=1) memberikan index dan line, index dimulai dari 1
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
