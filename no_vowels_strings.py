txt = "Dieu est Puissant, juste et grande"
count = 0
for char in txt:
  char = char.lower()
  if char == 'a' or char == "e" or char == "i" or char == "o" or char == "u":
    count += 1
print("Number of vowels: ", count)
