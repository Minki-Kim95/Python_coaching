# reverse string

# 1. 문자열 길이 읽어서 꽁무니부터 한글자씩 새로운 배열에 넣기


def convert(inputstring):
    length = len(inputstring)
    outputstring = ""

    for i in range(length - 1, -1, -1):
        outputstring = outputstring + inputstring[i]

    return outputstring


def main():
    inputstr = input('input string: ')
    output = convert(inputstr)
    print(output)


if __name__ == "__main__":
    main()
