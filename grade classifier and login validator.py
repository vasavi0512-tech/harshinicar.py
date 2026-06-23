score=int(input("enter marks"))
if score>=80:
    print("grade A")
elif score>=70:
    print("grade B")
elif score>=60:
    print("grade C")
elif score>=50:
    print("grade D")
elif score<=40:
     print("fail")
username=input("enter username")
pin=(input("enter pin"))
if username=="admin" and pin=="6330":
        print("login successful")
else:
        print("login failed")