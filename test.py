numbers = [1,4,5]
max = 0
min = 0
for n in numbers:
    if n > max:
        max=n

for n in numbers: 
    if n <= min:
        min=n
    else:
        min+=1
       
print(max)
print(min)
