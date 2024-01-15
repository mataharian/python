# FOR LOOPS : A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Print semua buah yang ada di list atau daftar
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i) #apple, banana, cherry

print("")


# LOOPING THROUGHT A STRING
# Mengulangi huruf-huruf dalam kata yg tertera
for i in "banana":
  print(i) #b a n a n a

print("")


# THE BREAK STATEMENT : With the break statement we can stop the loop before it has looped through all the items
# Berhenti dari loop ketika i adalah "banana"
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i)
  if i == "banana":
    break #apple, banana

print("")

# Keluar dari loop ketika i adalah "banana", tapi jeda muncul sebelum print
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  if i == "banana":
    break
  print(i) #apple

print("")


# THE CONTINUE STATEMENT : With the continue statement we can stop the current iteration of the loop, and continue with the next
# Jangan print "banana"
fruits = ["apple", "banana", "cherry"]
for i in fruits:
  if i == "banana":
    continue
  print(i) #apple, cherry

print("")


# THE RANGE() STATEMENT : To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Loop menggunakan function range
for x in range(6):
  print(x) #0,1,2,3,4,5 --> 6 tidak termasuk karena dimulai dari 0

print("")

# Loop menggunakan function range dengan parameter mulai
for x in range(2, 6):
  print(x) #2,3,4,5,

print("")

# Loop menggunakan function range dengan parameter mulai dan meningkat 3
for x in range(2, 18, 3):
  print(x) #2,5,8,11,14,17

print("")


# ELSE IN FOR LOOP : The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# Print semua angka 0-5 dan print pesan saat loop berakhir
for x in range(6):
  print(x)
else:
  print("Finally finished!") #0,1,2,3,4,5 Finally Finished!

print("")

# Hentikan loop ketika x adalah 3 
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #jika loop dihentikan, maka blok else tidak dieksekusi

print("")


# NESTED LOOPS : A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop"
# Print semua adjektif untuk semua buah
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print("")

# THE PASS STATEMENT : for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass