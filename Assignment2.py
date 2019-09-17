# 두 문자열의 공통된 글자 출력
# 1. 각각의 단어를 중복 제거한 문자열로 새로 가공하고 알파벳 26칸 담는 문자열에 각각의 알파벳에 맞는 자리에 넣기, 그리고 a~z 를 둘다 1 성립하면 모아서 출력
# this method is only for english

# To do: find why this code print wrong letter 


def findcommon(input1, input2):
    input1_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    input2_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in input1:
        input1_list.insert(ord(i) - ord('a'), 1)

    for i in input2:
        input2_list.insert(ord(i) - ord('a'), 1)

    output = ""
    for i in range(0, 27):
        if input1_list[i] == 1 & input2_list[i] == 1:
            output = output + chr(i + ord('a'))

    return output


def main():
    input1 = input("input string1: ")
    input2 = input("input string2: ")

    output = findcommon(input1, input2)

    print(output)


if __name__ == "__main__":
    main()


