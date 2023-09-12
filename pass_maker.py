import random
print("@TweakPy------@Filza2")
print('<—————————————————————————————->')
print(''' LIST PASS ''')
Gie=input("خلطه الحروف حقتك؟:")
mas=int(input("طول الباس ؟:"))
print('<——————————————————————————————>')
def GetPassword(data):
  Max = (mas) 
  Password = ""
  while len(Password) != Max:
    value = random.choice(data)
    Password += value
  return Password
data = Gie
for i in range(18888):
   print(GetPassword(data))
   Password=GetPassword(data)
   with open('passwords.txt', 'a') as x:
   	x.write(Password+ '\n')
