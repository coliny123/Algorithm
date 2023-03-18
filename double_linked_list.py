class Node:
    def __init__(self):
        self.data = None
        self.plink = None
        self.nlink = None


def print_nodes(start):
    current = start
    if current.nlink is None:
        return
    print(f'정방향 --> ', end=" ")
    print(current.data, end=" ")
    while current.nlink is not None:
        current = current.nlink
        print(current.data, end=" ")
    print()
    print('역방향 --> ', end=" ")
    print(current.data, end=" ")
    while current.plink is not None:
        current = current.plink
        print(current.data, end=" ")
    print()


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data is find_data:          # DLL 맨 앞에 삽입
        node = Node()
        node.data = insert_data
        node.nlink = head
        head.plink = node
        node.plink = None
        head = node
        return

    current = head                      # DLL 중간 before 삽입
    while current.nlink != None:
        pre = current
        current = current.nlink
        if current.data is find_data:
            node = Node()
            node.data = insert_data
            node.nlink = current
            current.plink = node
            pre.nlink = node
            node.plink = pre
            return

    node = Node()                       # DLL 끝 삽입
    node.data = insert_data
    current.nlink = node
    node.plink = current


head, current, pre = None, None, None
data_array = ['민지', '혜린', '하니', '다니엘', '혜인']

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.nlink = node
        node.plink = pre

    print_nodes(head)
    insert_node('민지', '카리나')
    print_nodes(head)

    insert_node('다니엘', '윈터')
    print_nodes(head)

    insert_node('도환', '육정현')
    print_nodes(head)
