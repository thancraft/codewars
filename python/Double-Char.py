# Menggandakan setiap karakter dalam string (contoh: "abc" -> "aabbcc")
def double_char(s):
    nilai = ""
    for huruf in s:
        nilai += huruf + huruf  # Tambahkan huruf dua kali
    return nilai
