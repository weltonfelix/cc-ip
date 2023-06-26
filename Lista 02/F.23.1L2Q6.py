n = int(input())

print(
    "A sequência de número das camisas do seu time será: 1",
    end=(", " if n > 1 else "\n"),
)

l1 = 1
l2 = 0

for i in range(1, n):
    current_value = l1 + l2
    l2 = l1
    l1 = current_value

    print(current_value, end=(", " if i + 1 < n else "\n"))
