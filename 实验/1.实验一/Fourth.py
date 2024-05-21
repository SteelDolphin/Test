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

def clear_records():
    with open("game_results.txt", "w") as file:
        file.write("")
def save(round_number, attempts, guessed_number, hint):
    with open("game_results.txt", "a") as file:
        file.write(f"第{round_number}轮猜测记录：\n")
        file.write("次数  猜测数字     提示\n")
        for i, guess in enumerate(guessed_number, start=1):
                file.write(f"{i}       {guess}       {hint[i-1]}\n")
        file.write(f"第{round_number}轮猜测共进行了{attempts}次\n\n")

def print_records():
    try:
        with open("game_results.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("记录文件不存在或为空！")

hints = {1: "太小了", 0: "猜对了", -1: "太大了"}
def main():
    continue_game = True
    round = 0
    attempt = []
    clear_records()
    while continue_game:
        round += 1
        target_number = random.randint(1,10)
        attempts = 0
        guessed_numbers = []
        hint = []
        while attempts < 5:
            user_input = input("请输入1至10之间的整数进行猜测：")
            is_valid, guessed_number = validate_input(user_input)
            if not is_valid:
                continue
            attempts += 1
            guessed_numbers.append(guessed_number)
            if guessed_number == target_number:
                hint.append(hints[0])
                print(f"恭喜您，猜对了！一共猜了{attempts}次！")
                break
            elif guessed_number < target_number:
                hint.append(hints[1])
                print("太小了，再试一次")
            else:
                hint.append(hints[-1])
                print("太大了，再试一次")
        else:
            print("很遗憾，已经用完5次机会，下次继续努力！")
        attempt.append(attempts)
        save(round, attempts, guessed_numbers, hint)
        choice = input("是否想要继续下一轮游戏？(输入 y 继续，其他键退出)：")
        continue_game = (choice.lower() == 'y')
    print_records();
    sum = 0
    print("轮数    猜测次数")
    for i, t in enumerate(attempt, start=1):
        print(f"{i}     {t}")
        sum += t
    print(f"目前平均战绩：{sum // len(attempt)}次猜中！")

main()