'''
打印如下所示的三角形圖案:
需輸入行數(row)
Q1:
*
**
***
****
*****
Q2:
    *
   **
  ***
 ****
*****
Q3:
    *
   ***
   5
  *****
 *******
*********
'''
row = int(input('請輸入行數: '))

# Q1:
for num in range(1, row+1):
    print('*' * num)

### Q1 ANS
#for i in range(row):
#    for _ in range(i + 1):
#        print('*', end='')
#    print()


# Q2:
count = 1
for num in range(row, 0, -1):
    if (num-1) > 0:
        print(' ' * (num-1) + '*' * count)
    else:
        print('*' * count)
    count += 1

#### Q2 ANS
#for i in range(row):
#    for j in range(row):
#        if j < row - i - 1:
#            print(' ', end='')
#        else:
#            print('*', end='')
#    print()

# Q3:
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
