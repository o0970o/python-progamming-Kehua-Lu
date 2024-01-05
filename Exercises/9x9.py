i = 1
while  i <= 9:
     j = 1
     while j <= i:
         print(f"{j}*{i} = {j * i}\t", end='')
         j += 1
     i +=1
print()

for i in range(1,10):
     for j in range(1,10):
          if j<= i:
               print(f"{j}*{i} = {j * i}\t", end='')
               j += 1
print()