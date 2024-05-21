#判断数的合理性
def validate_input(user_input):
    try:
        num = int(user_input)
        if 1 <= num <= 100:
            return True, num
        else:
            print("请输入1至100之间的整数！")
            return False, None
    except ValueError:
        print("请输入有效的整数！")
        return False, None

def find_multiples(num):
    multiples = []
    times = 1
    while times*num <= 1000:
        multiples.append(times*num)
        times += 1
    return multiples

def write_to_file(num, multiples):
    filename = f"./{num}的倍数.txt"
    with open(filename, 'w') as file:   # with语句确保资源正确管理
        for i, multiple in enumerate(multiples, start=1):
            file.write(f"{i} {multiple}\n")
    print(f"结果已保存在文件 {filename}")

def main():
    user_input = input("请输入一个1-100之间的整数：")
    is_valid, num = validate_input(user_input)
    if not is_valid:    # 不是有效数字，结束程序
        return
    multiples = find_multiples(num)
    for i, multiple in enumerate(multiples, start=1):
        print(f"{i} {multiple}")
    write_to_file(num, multiples)

main()