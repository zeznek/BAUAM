s = ""
a = "1112031584"

for i in range(1, len(a)):
    if (int((a[i])) % 2 == (int(a[i-1]) % 2)):
        s += str(max(a[i], a[i-1]))

secretcode = s
print(f"multisoft.se/{secretcode}")
