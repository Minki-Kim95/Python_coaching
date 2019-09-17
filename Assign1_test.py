# 길이를 입력 받아서 입력은 앞에서부터 출력은 뒤에서부터 읽으면서 체크하는 걸 만들면 될듯

import Assignment1 as hw1


def check_fn():
    test_string = "123456789"
    output = hw1.convert(test_string)
    if output == "987654321":
        return True
    else:
        return False


def main():
    check = check_fn()

    if check:
        print("Good Job!")
    else:
        print("Try again")


if __name__ == "__main__":
    main()

