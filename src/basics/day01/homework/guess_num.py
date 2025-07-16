'''
猜数字游戏：

1. 电脑产生一个（1-100）的随机数，用户进行猜测(通过 input 输入)，直到猜中为止。
2. 如果猜对了，输出：恭喜你猜对了，数字是 xx。
3. 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
4. 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次
'''

'''
1. 先判断输入的数字在 1-100之间如果不是重新输入
2. 如果猜对了，break
3. 猜大或猜小都继续， continue
4. 用 while
'''

import random
print('猜数字游戏:')
print('='*40)
computer = random.randint(1,100)


while True:
    player = int(input('请输入一个 1-100的数字:'))
    if player<1 or player>100:
        print("输入的数字范围不对, 请重新输入")
        continue
    elif computer == player:
        print(f'恭喜你猜对了，数字是:{computer}')
        break
    elif player > computer:
        print('猜测的数字太大了，继续加油')
        continue
    elif player < computer:
        print('猜测的数字有点小，再来一次')
        continue

print('='*40)