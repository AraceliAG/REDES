for i in range (1, 11):
    a = i #2
    d = a*4 #8
    c = d - a #6
    b = c / a #3
    
    if (a * 4 == d and a + c == d and c / a == b and d - a == c and c!=b):
        print('este es el bueno ')
        print(f"a = {a}")
        print(f"b = {b}")
        print(f"c = {c}")
        print(f"d = {d}")
        break
    else:
        print('no es ', i)
    