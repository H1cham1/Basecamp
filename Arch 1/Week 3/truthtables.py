A = True
B = False

print("AND\n")

print(A , "+" , A , "=" , A)
print(A , "+" , B , "=" , B)
print(B , "+" , A , "=" , B)
print(B , "+" , B , "=" , B)

print("Or\n")

print(A , "+" , A , "=" , B)
print(A , "+" , B , "=" , A)
print(B , "+" , A , "=" , A)
print(B , "+" , B , "=" , A)

