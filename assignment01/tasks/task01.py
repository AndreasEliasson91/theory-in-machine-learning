a = [1, -2, 2, 3]
b = [-1, 1, 1, 4]
c = [2, 2, -3, -3]

# Remove x from (b) and (c)
a1 = a  # x - 2y + 2z = 3
b1 = [b[i] + a[i] for i in range(len(b))]  # -y + 3z = 7
c1 = [c[i] - 2*a[i] for i in range(len(c))]  # 6y - 7z = -9

# Remove y from (a) and (c)
a2 = [a1[i] - 2*b1[i] for i in range(len(a1))]  # x - 4z = -11
b2 = b1  # -y + 3z = 7
c2 = [c1[i] + 6*b1[i] for i in range(len(c1))]  # 11z = 33

# Calculate x, y, z
z = int(c2[3] / c2[2])  # 11z = 33 <=> 11z / 11 = 33 / 11 <=> z = 3
x = ((a2[2] * z) * (-1)) + a2[3]  # x - 4z = -11 <=> x - (4 * 3) = -11 <=> x - 12 = -11 <=> x = -11 + 12 = 1
y = abs((b2[3] + ((b2[0] * x) * (-1))) + ((b2[2] * z) * (-1)))  # -y + 3z = 7 <=> -y + (3 * 3) = 7 <=> -y + 9 = 7 <=> -y = 7 - 9 = -2 <=> y = 2

# print whether left side is equivalent to the right side of the equation system and the values of (x, y, z)
print(sum([a[0] * x, a[1] * y, a[2] * z]) == a[3],
      sum([b[0] * x, b[1] * y, b[2] * z]) == b[3],
      sum([c[0] * x, c[1] * y, c[2] * z]) == c[3])
print(f'x = {x}\ny = {y}\nz = {z}')
