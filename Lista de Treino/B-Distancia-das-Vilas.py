xh = 34
zh = 220

xk = 0
zk = 0

xs = 140
zs = 456

x0 = int(input())
z0 = int(input())

d0h = ((x0 - xh) ** 2 + (z0 - zh) ** 2) ** 0.5
d0k = ((x0 - xk) ** 2 + (z0 - zk) ** 2) ** 0.5
d0s = ((x0 - xs) ** 2 + (z0 - zs) ** 2) ** 0.5

print(f"Distancia para Hogsmeade: {d0h:.2f}")
print(f"Distancia para Kakariko: {d0k:.2f}")
print(f"Distancia para Solitude: {d0s:.2f}")
