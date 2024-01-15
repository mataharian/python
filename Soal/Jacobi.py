f1 = lambda x, y, z : (1+y-z)/3
f2 = lambda x, y, z : (-3*x-2*z+0)/6
f3 = lambda x, y, z : (-3*x-3*y+4)/7


TOL = 0.0001
iteration = 0

# initial value
x0 = 0
y0 = 0
z0 = 0

condition = True
while condition:
    x1 = round(f1(x0, y0, z0), 4)
    y1 = round(f2(x0, y0, z0), 4)
    z1 = round(f3(x0, y0, z0), 4)

    e = round(max(abs(x1-x0), abs(y1-y0), abs(z1-z0))/max(abs(x1), abs(y1), abs(z1)), 4)
    iteration += 1

    x0 = x1
    y0 = y1
    z0 = z1

    condition = TOL < e

print(f"Nilai x = {x1}")
print(f"Nilai y = {y1}")
print(f"Nilai z = {z1}")
print(f"Nilai e = {e}")
print(f"Iterasi = {iteration}")
