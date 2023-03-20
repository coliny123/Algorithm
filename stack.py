def is_stackfull():
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    else:
        return False


def is_stackempty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False


def push(push_data):
    global SIZE, stack, top
    if is_stackfull():
        print("스택이 가득 찼습니다.")
        return
    top += 1
    stack[top] = push_data


def pop():
    global SIZE, stack, top
    if is_stackempty():
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek():
    global SIZE, stack, top
    if is_stackempty():
        print("스택이 비었습니다.")
        return None
    else:
        return stack[top]


SIZE = int(input("스택의 크기를 입력하세요 : "))
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":

    while True:
        menu = input("삽입(i) / 추출(e) / 확인(v) / 종료(x) 중 하나를 고르시오 : ").lower()
        if menu == "x":
            print("프로그램 종료")
            break
        elif menu == "i":
            insert_data = input("입력할 데이터 : ")
            push(insert_data)
            print(f"스택상태 : {stack}")
        elif menu == "e":
            ret_data = pop()
            print(f"추출한 데이터 : {ret_data}")
            print(f"스택상태 : {stack}")
        elif menu == "v":
            peek_data = peek()
            print(f"확인된 데이터 : {peek_data}")
            print(f"스택상태 : {stack}")
        else:
            print("메뉴안에서 골라주세요")


