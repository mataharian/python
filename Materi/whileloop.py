# WHILE LOOP : With the while loop we can execute a set of statements as long as a condition is true.

# THE WHILE LOOP
fruits = ["Apple", "Banana", "Cherry"]
i = 0
while i < len(fruits):
  print(fruits[i])
  i += 1 #Apple, Banana, Cherry

print("")

# Print i selama i kurang dari 6  
i = 1
while i < 6:
  print(i)
  i += 1 #1,2,3,4,5

print("")


# THE BREAK STATEMENT : With the break statement we can stop the loop even if the while condition is true.
# Keluar dari loop ketika i adalah 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 #1,2,3

print("")


# THE CONTINUE STATMENET : With the continue statement we can stop the current iteration, and continue with the next.
# Lanjutkan ke pengulangan berikutnya jika i adalah 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("")


# THE ELSE STATEMENT : With the else statement we can run a block of code once when the condition no longer is true.
# Print pesan ketika kondisinya salah
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")