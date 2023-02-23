import random
menPref = {}
womenPref = {}

n = int(input("Enter number of people in each group:"))

for i in range(n):
    x = [f"woman{j+1}" for j in range(n)]
    random.shuffle(x)
    menPref[f"man{i+1}"] = x

print(menPref)
print()

for i in range(n):
    x = [f"man{i+1}" for i in range(n)]
    random.shuffle(x)
    womenPref[f"woman{i+1}"] = x

print(womenPref)
