def operation(a: int, b: int) -> None:
    """运算"""
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a**b)
    print(a//b)


def main():
    a = eval(input())
    b = eval(input())
    operation(a, b)


if __name__ == "__main__":
    main()
