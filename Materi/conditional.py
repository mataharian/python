# CONDITIONS AND IF STATEMENTS

a = 33
b = 200
if b > a:
  print("b is greater than a") #b is greater than a

print("")


# ELIF : The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #a and b greather than a

print("")


#ELSE : The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #a is greater than b

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #b is not greater than a

print("")


# SHORT HAND IF : If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b") #a is greater than b"

print("")


# SHORT HAND IF ... ELSE : If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
a = 2
b = 330
print("A") if a > b else print("B") #B

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #=

print("")


# AND : The and keyword is a logical operator, and is used to combine conditional statements.
# Test if a is greater than b, AND if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") #Both conditions are True

print("")

# OR : The or keyword is a logical operator, and is used to combine conditional statements.
# Test if a is greater than b, OR if a is greater than c
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") #At least one of the conditions is True

print("")


# NESTED IF : You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print("")


# THE PASS STATEMENT : if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass