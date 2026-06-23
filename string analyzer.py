text=input("enter string")
print("length =",len(text))
print("upper =",text.upper())
print("lower =",text.lower())
print("reverse =",text[::-1]) #-1 means move backward one step at a time , [::-1] means prints the string in reverse order.
vowel=0
for i in text:
    if i in "aeiouAEIOU":
        vowel+=1
print("vowel count:", vowel)