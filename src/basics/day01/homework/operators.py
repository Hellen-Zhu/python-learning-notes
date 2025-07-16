'''
1. 书写代码求 `1-100之间所有数字的累加和`
'''
num=0
for i in range(101):
    num+=i
    i+=1

print(f'1-100之间所有数字的累加和为: {num}')

'''
2. 书写代码求 `1-100 之间偶数的累加和`
'''
num1=0
for i in range(101):
    if i%2==0:
        num1+=i
        i+=1
print(f'1-100 之间偶数的累加和: {num1}')
