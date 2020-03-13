def dec2bin( n: int ) -> str :
    reste = ''
    a = n
    while a != 0:
        reste = str(a%2) + reste
        a = a // 2
    return reste