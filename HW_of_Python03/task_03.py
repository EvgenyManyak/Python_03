my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 0
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(round(max-min, 2))