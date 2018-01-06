str = input("Enter a string: ")
str = str.replace("Carlton", "Chutia")
substrs = str.split(' ')
for str in substrs:
  print(str)
str2 = ' '.join(substrs)
print(str2)
