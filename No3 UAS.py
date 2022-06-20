data = [ ]
x = 0
while True:
    user = input("Masukan angka: ")
    if user == 'n':
        break
    x += 1
    data.append(user)

total = 0
for nilai in data:
    total += int(nilai)

total = total / x

print(total)
