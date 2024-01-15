omega = 1.25
f1 = lambda x, y, z : (1-omega)*x + (omega/3)*(1+y-z)
f2 = lambda x, y, z : (1-omega)*y + (omega/6)*(-3*x-2*z+0)
f3 = lambda x, y, z : (1-omega)*z + (omega/7)*(-3*x-3*y+4)


TOL = 0.0001
iteration = 0

# initial value
x0 = 0
y0 = 0
z0 = 0

condition = True
while condition:
    x1 = round(f1(x0, y0, z0), 4)
    y1 = round(f2(x1, y0, z0), 4)
    z1 = round(f3(x1, y1, z0), 4)
    iteration += 1

    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);

    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > TOL and e2 > TOL and e3 > TOL

print(f"Nilai x = {x1}")
print(f"Nilai y = {y1}")
print(f"Nilai z = {z1}")
print(f"Iterasi = {iteration} \n")
