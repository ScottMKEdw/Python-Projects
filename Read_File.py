file = input("Enter File Name: ")
try:
  fhand = open(file)
except:
  print("Can't Open File")
  quit()
for i in fhand:
    print(i)

