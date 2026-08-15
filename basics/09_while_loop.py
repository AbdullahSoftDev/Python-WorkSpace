count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
i = 0
while True:
    if i == 5:
        break
    print(i)
    i += 1

# Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)