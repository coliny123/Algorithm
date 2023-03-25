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
