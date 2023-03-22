def is_queuefull():
    if (rear+1) % SIZE == front:
        return True
    else:
        return False


def is_queueempty():
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global SIZE, circular_queue, front, rear
    if is_queuefull():
        print("큐가 가득 찼습니다.")
        return
    rear = (rear+1) % SIZE
    circular_queue[rear] = data


def dequeue():
    global SIZE, circular_queue, front, rear
    if is_queueempty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % SIZE
    data = circular_queue[front]
    circular_queue[front] = None
    return data


def peek():
    global SIZE, circular_queue, front, rear
    if is_queueempty():
        print("큐가 비었습니다.")
        return None
    return circular_queue[(front + 1) % SIZE]


SIZE = 5
circular_queue = [None for _ in range(SIZE)]
front, rear = 0, 0


if __name__ == "__main__":
    while True:
        menu = input("삽입(i) / 추출(e) / 확인(v) / 종료(x) 중 하나를 선택하시오 : ").lower()
        if menu == "x":
            print("프로그램을 종료합니다")
            break
        if menu == "i":
            data = input("삽입할 데이터를 입력하시오: ")
            enqueue(data)
            print(f"큐 상태 : {circular_queue}")
            print(f"front : {front}, rear : {rear}")
        elif menu == "e":
            data = dequeue()
            print(f"추출된 데이터 : {data}")
            print(f"큐 상태 : {circular_queue}")
            print(f"front : {front}, rear : {rear}")
        elif menu == "v":
            data = peek()
            print(f"확인된 데이터 : {data}")
            print(f"큐 상태 : {circular_queue}")
            print(f"front : {front}, rear : {rear}")
        else:
            print("메뉴에서 골라주세요")

