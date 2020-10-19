import random
import string


# 生成随机手机号
def create_phone():
    # 第二位数字
    # second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    # third = {
    #     3: random.randint(0, 9),
    #     4: [5, 7, 9][random.randint(0, 2)],
    #     5: [i for i in range(10) if i != 4][random.randint(0, 8)],
    #     7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
    #     8: random.randint(0, 9),
    # }[second]

    # 最后八位数字
    suffix = random.randint(9999999,100000000)
# 拼接手机号
    return "131{}".format( suffix)
    # return "1{}{}{}".format(second, third, suffix)

    # def traversal_list(alist, i):
    #     while True:
    #         length = len(alist)
    #         i = i % (length)
    #         yield alist[i]
    #         i += 1

# 生成手机号
phone = create_phone()
# print(phone)



# 生成制定长度的字符串
def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

f = generate_random_str(24)
# print (f)