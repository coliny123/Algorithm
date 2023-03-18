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


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data is find_data:      # 첫번째 노드 삽입
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head                  # 중간 노드 삽입
    while current.link != head:
        pre = current
        current = current.link
        if current.data is find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()                   # 마지막 노드 삽입
    node.data = insert_data
    current.link = node
    node.link = head


def delete_node(delete_data):
    global head, current, pre

    if head.data is delete_data:     # 첫번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del current
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data is delete_data:
            pre.link = current.link
            del current
            return


def find_node(find_data):
    global head, current, pre

    current = head
    if current.data is find_data:
        return current
    while current.link != head:
        current = current.link
        if current.data is find_data:
            return current
    return Node()


head, current, pre = None, None, None
data_array = ['민지', '혜린', '하니', '다니엘', '헤인']

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

    print_nodes(head)
    insert_node('민지', '카리나')
    print_nodes(head)

    insert_node('하니', '윈터')
    print_nodes(head)

    insert_node('도환', '육정현')
    print_nodes(head)

    delete_node('카리나')
    print_nodes(head)

    delete_node('윈터')
    print_nodes(head)

    delete_node('육정현')
    print_nodes(head)

    delete_node('도환')
    print_nodes(head)

    f_node = find_node('민지')
    print(f_node.data)

    f_node = find_node('하니')
    print(f_node.data)

    f_node = find_node('도환')
    print(f_node.data)
