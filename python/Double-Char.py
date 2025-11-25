def double_char(s):
    nilai = ""
    for huruf in s:
        nilai += huruf + huruf
    return nilai


## Best Practices ##
# penjelasan:
# - menggunakan join dan list comprehension
# - lebih efisien dan lebih cepat

def double_char(s):
    return ''.join(c * 2 for c in s)
