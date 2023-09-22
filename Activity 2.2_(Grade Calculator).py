print ("-------- GRADE CALCULATOR --------")
print ("Enter your grades in the following subjects: ")

eng = int (input("English: "))
fil = int (input("Filipino: "))
sci = int (input("Science: "))
math = int (input("Mathematics: "))
ap = int (input("Araling Panlipunan: "))
pe = int (input("Physical Education: "))

ave = ((eng+fil+sci+math+ap+pe) /6)

print ("Your general average: ",ave)