def is_valid_input(user_input):
    try:
        num = int(user_input)
        if 1 <= num <= 100:
            print(f"您输入的是整数：{num}")
            return True
        else:
            print("对不起，您输入的数字范围不正确，请重新输入！")
            return False
    except ValueError:
        print("对不起，您输入的不是整数，请重新输入！")
        return False

def main():
    attempts = 0
    while attempts < 3:
        user_input = input("请输入1至100之间的整数：")
        if is_valid_input(user_input):
            break
        attempts += 1
    else:
        print("对不起，您已经3次输入错误，程序退出。")

main()
