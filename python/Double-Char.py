def double_char(s):
    nilai = ""
    for huruf in s:
        nilai += huruf + huruf
    return nilai


## Best Practices ##
# 1.
def double_char(s):
    return ''.join(c * 2 for c in s)
