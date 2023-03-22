def is_queuefull():
    if rear >= SIZE-1:  # rear가 SIZE-1까지 왔지만 dequeue로 인해 앞이 비어있으면??
        return True
    else:
        return False


def is_queueempty():
    if rear == front:
        return True
    else:
        return False


def enqueue(data):
    global SIZE, queue, front, rear
    if is_queuefull():
        print("큐가 가득 찼습니다.")
        return
    rear += 1
    queue[rear] = data


def dequeue():
    global SIZE, queue, front, rear
    if is_queueempty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if is_queueempty():
        return None
    return queue[front+1]


SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

if __name__ == "__main__":
    while True:
        menu = input("삽입(i) / 추출(e) / 확인(v) / 종료(x) 중 하나를 선택하시오 : ").lower()
        if menu == "x":
            print("프로그램을 종료합니다")
            break
        if menu == "i":
            data = input("삽입할 데이터를 입력하시오: ")
            enqueue(data)
            print(f"큐 상태 : {queue}")
        elif menu == "e":
            data = dequeue()
            print(f"추출된 데이터 : {data}")
            print(f"큐 상태 : {queue}")
        elif menu == "v":
            data = peek()
            print(f"확인된 데이터 : {data}")
            print(f"큐 상태 : {queue}")
        else:
            print("메뉴에서 골라주세요")

