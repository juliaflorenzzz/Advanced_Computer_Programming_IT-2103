fname = str (input ("Father's name: "))
fbirthplace = str (input ("Father's birthplace: "))
fmonth = str (input ("Father's birthmonth: "))
fday = int (input ("Father's birthdate: "))
fyear = int (input ("Father's birthyear: "))
currentyear = 2023
fage = (currentyear - fyear)

print ("   ")
print ("   ")
print ("Father's name: ",fname)
print ("Father's birthplace: ",fbirthplace)
print ("Father's birthday: ", fmonth, fday, fyear)
print ("Father's age: ",fage)