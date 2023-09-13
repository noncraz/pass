import random
print("@ittz_danyar------@tools_vip")
print('<—————————————————————————————->')
print(''' LIST PASS ''')
Gie=input("ناوێک بنوسە:")
mas=int(input("چەند پیت بێ؟:"))
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
