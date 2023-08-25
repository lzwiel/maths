def is_prime(num):
    # 质数大于1
    if num > 1:
        # 查找因子
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                # 如果能被整除，则不是质数
                return False
        else:
            # 没有找到因子，是质数
            return True
    else:
        # 小于等于1的数字不是质数
        return False

# 获取用户输入
number = int(input("请输入一个数字: "))

# 判断并输出结果
if is_prime(number):
    print(f"{number} 是质数")
else:
    print(f"{number} 是合数")
