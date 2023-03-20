import webbrowser
import time

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


SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls:
        push(url)
        webbrowser.open('http://' + url)
        print(url, end=" --> ")
        time.sleep(1)

    print("방문 종료")
    time.sleep(3)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('http://'+url)
        print(url, end=' --> ')
        time.sleep(1)
    print("방문 종료")