#Get file input from user and try and open it and assign handle fhand
file = input("Enter File Name: ")
try:
  fhand = open(file)
except:
  print("Can't Open File")
  quit()

#Create empty dictionary to put values and keys in
count = dict()
#turn long string into list for each line in doc
for line in fhand: 
  words = line.split()
  print(words)
#Go through each list entry and add them to the dictionary while summing the number of times the key shows up in the value
  for word in words:
    count[word]=count.get(word,0) + 1

print(count)
print('Keys:',count.keys())
print('Values:',count.values())
print('Items:',count.items())


for aaa,bbb in count.items():
  print(aaa,bbb)
  
