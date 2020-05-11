try:
    num = 1/10
    int(num)
except Exception as E:
    raise ValueError from E

