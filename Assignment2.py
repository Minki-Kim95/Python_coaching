# 두 문자열의 공통된 글자 출력
# 1. 각각의 단어를 중복 제거한 문자열로 새로 가공하고 알파벳 26칸 담는 문자열에 각각의 알파벳에 맞는 자리에 넣기, 그리고 a~z 를 둘다 1 성립하면 모아서 출력
# -> problem: this method is only for english
# 2. 모든 문자열의 아스키코드를 저장하여 정렬 그리고 찾기(정렬후 찾으면 복잡도 줄일 수 있을듯)

# To do: find why this code print wrong letter 


def findcommon(input1, input2):
    input1_list = []
    input2_list = []

    for i in input1:
        input1_list.append(ord(i))

    input1_list = list(set(input1_list))    # delete duplications
    input1_list.sort()

    for i in input2:
        input2_list.append(ord(i))


    input2_list = list(set(input2_list))    # delete duplications
    input2_list.sort()

    output = ""

    k = 0
    # k를 사용하는 이유: 이중 포문에서 두 리스트 비교중 일치하는 것을 찾으면
    # 일치하는 원소의 그 전 원소들은 비교할 필요가 없으므로 (미리 리스트를 정렬해둔 덕에)
    # 그 다음부터 확인하도록 알고리즘 고안
    # for j in range(k, lenth2):   input2_list[j]
    for i in input1_list:
        for j in input2_list[k:]:
            if i == j:
                k = input2_list.index(j) + 1   # 일치한 것을 찾은 경우, 일치한 원소의 그 다음 원소부터 읽도록 k 값 변경
                output = output + chr(i)
                break

    return output


def main():
    input1 = input("input string1: ")
    input2 = input("input string2: ")

    output = findcommon(input1, input2)

    print(output)


if __name__ == "__main__":
    main()


