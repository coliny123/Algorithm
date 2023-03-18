import random


class Node:
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    if current.link is None:
        return
    print(current.data, end=" ")
    while current.link != start:
        current = current.link
        print(current.data, end=" ")
    print()

def count():
    global head, current, pre

    odd, even = 0, 0
    if head is None:
        return False
    current = head
    while True:
        if current.data % 2 == 0:
            even += 1
        else:
            odd += 1
        if current.link is head:
            break
        current = current.link

    return odd, even


def make_zero(odd, even):
    if odd > even:
        reminder = 1
    else:
        reminder = 0
    current = head
    while True:
        if current.data % 2 is reminder:
            current.data *= -1
        if current.link is head:
            break
        current = current.link

data_array = []
for _ in range(7):
    data_array.append(random.randint(1, 100))
head, current, pre = None, None, None


if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    node.link = head

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head

    odd_count, even_count = count()
    print(f'홀수 --> {odd_count} \t 짝수 --> {even_count}')
    make_zero(odd_count, even_count)
    print_nodes(head)