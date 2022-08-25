'''
Q:輸入兩個正整數計算它們的最大公約數和最小公倍數

最小公倍數:least common multiple (lcm)
lcm(a,b) = |a,b|/gcd(a,b)

最大公因數:
最大公因數（英語：highest common factor，hcf）
也稱最大公約數（英語：greatest common divisor，gcd）是數學詞彙
'''


gcd = 0
lcm = 0

#輸入兩個數值
key1 = int(input('key1 is:'))
key2 = int(input('key2 is:'))

if key1 > key2:
    key1 , key2 = key2, key1
# 讓key2 > key1

for factor in range(key2, 0, -1):
    if (key2 % factor == 0 ) and (key1 % factor == 0 ):
        gcd = factor
        lcm = key1 * key2 // gcd
        break
print('最大公因數(gcd):'+str(gcd))
print('最小公倍數(lcm):'+str(lcm))
