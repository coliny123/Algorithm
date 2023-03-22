import random


def is_queuefull():
    if (rear+1) % SIZE == front:
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
        return
    rear = (rear+1) % SIZE
    queue[rear] = data


def dequeue():
    global SIZE, queue, front, rear
    if is_queueempty():
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if is_queueempty():
        return None
    return queue[(front+1) % SIZE]


SIZE = 6
queue = [None for _ in range(SIZE)]
front, rear = 0, 0

if __name__ == "__main__":
    call_list = [('고장', 3), ('사용', 9), ('환불', 4), ('기타', 1)]
    total = 0
    for i in range(SIZE-1):
        print(f"귀하의 대기 예상시간은 {total}")
        print(f"현재 대기 콜 : {queue}")
        print()
        random.shuffle(call_list)
        total = total + call_list[0][1]
        enqueue(call_list[0])

    print(f"최종 대기 콜 : {queue}")
    print("프로그램 종료!")