import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i


def preorder(inStart, inEnd, postStart, postEnd):  # dfs
    if (inStart > inEnd) or (postStart > postEnd):
        return

    root = postorder[postEnd]  # 후위 순회 결과의 마지막 노드 = 루트노드

    leftNode = nodeNum[root] - inStart  # 왼쪽 서브트리 노드 수
    rightNode = inEnd - nodeNum[root]  # 오른쪽 서브트리 노드 수

    print(root, end=" ")
    preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)  # 왼쪽
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)  # 오른쪽


preorder(0, n - 1, 0, n - 1)
