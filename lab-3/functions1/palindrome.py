def is_pal():
    o = str(input("string: "))
    if o == o[::-1]:
        return True
    return False

print(is_pal())