class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크',  '걸스데이', '트와이스', '잇지', '여자친구']

node = TreeNode()
node.data = nameAry[0]
root = node

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

print("이진 탐색 트리 구성 완료")

delete_name = input("삭제할 그룹 이름 : ")

current = root
parent = None
while True:
    if delete_name == current.data:

        if current.left is None and current.right is None:
            if parent.left is current:
                parent.left = None
            else:
                parent.right = None
            del current
        elif current.left is not None and current.right is None:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.left
            del current
        elif current.left is None and current.right is not None:
            if parent.left is current:
                parent.left = current.left
            else:
                parent.right = current.left
            del current
        print(f"{delete_name} 가 삭제 됨")
        break
    elif delete_name < current.data:
        if current.left is None:
            print(f"{delete_name} 가 트리에 없음")
            break
        parent = current
        current = current.left
    else:
        if current.right is None:
            print(f"{delete_name} 가 트리에 없음")
            break
        parent = current
        current = current.right


