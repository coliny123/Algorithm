import random

def is_stackfull():
    global SIZE, stack, top
    if top >= SIZE-1:
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
        return
    top += 1
    stack[top] = push_data


def pop():
    global SIZE, stack, top
    if is_stackempty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data


def peek(peek_data):
    global SIZE, stack, top
    if is_stackempty():
        return None
    return stack[top]


SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    snack_arr = ['빼빼로', '홈런볼', '초코파이', '포카칩', '뿌셔뿌셔', '계란과자']
    random.shuffle(snack_arr)  # list 항목 섞기

    print("과자집에 가는길 :", end=" ")
    for snack in snack_arr:
        push(snack)
        print(f"{snack} -->", end=" ")
    print("과자집")

    print("우리집에 오는길 :", end=" ")
    for i in snack_arr:
        print(f"{pop()} -->", end=" ")

    print("우리집")