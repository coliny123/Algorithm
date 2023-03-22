def is_queuefull():
    global SIZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


def is_queueempty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False


def enqueue(data):
    global SIZE, queue, front, rear
    if is_queuefull():
        print("큐가 가득 찼습니다")
        return
    rear += 1
    queue[rear] = data


def dequeue():
    global SIZE, queue, front, rear
    if is_queueempty():
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1
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
    for _ in range(SIZE):
        print(f"(남은 인원:{SIZE-(rear+1)})", end="")
        data = input("대기자 명단에 등록하시오 : ")
        enqueue(data)

    for _ in range(SIZE):
        print(f"대기 줄 상태 : {queue}")
        print(f"{dequeue()} 님 식당에 들어감")

    print(f"대기 줄 상태 : {queue}")
    print("식당 영업 종료")
