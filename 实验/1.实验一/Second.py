import random

def validate_input(user_input):
    try:
        num = int(user_input)
        if 1 <= num <= 10:
            return True, num
        else:
            print("请输入1至10之间的整数！")
            return False, None
    except ValueError:
        print("请输入有效的整数！")
        return False, None

def main():
    continue_game = True
    while continue_game:
        target_number = random.randint(1,10)
        attempts = 0
        while attempts < 5:
            user_input = input("请输入1至10之间的整数进行猜测：")
            is_valid, guessed_number = validate_input(user_input)
            if not is_valid:
                continue
            attempts += 1
            if guessed_number == target_number:
                print(f"恭喜您，猜对了！一共猜了{attempts}次！")
                break
            elif guessed_number < target_number:
                print("太小了，再试一次")
            else:
                print("太大了，再试一次")
        else:
            print("很遗憾，已经用完5次机会，下次继续努力！")
        choice = input("是否想要继续下一轮游戏？(输入 y 继续，其他键退出)：")
        continue_game = (choice.lower() == 'y')

main()