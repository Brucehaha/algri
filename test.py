# def num(d, multi):
# #     """
# #
# #     :param d: multiplied by 3 gives a result containing all d
# #     :param multi:  multiplied by "multi" gives a result containing all d
# #     :return: return digit match eg. multiplied by 3 gives a result containing all ones.
# #     """
# #     digits = list()
# #     for x in range(0,100):
# #         digit = x
# #         result = str(x*multi)
# #         set_digit = set()
# #
# #         for i in result:
# #             set_digit.add(i)
# #         if len(set_digit)==1 and set_digit.pop() == str(d):
# #             digits.append(digit)
# #
# #     return digits
# #
# #
# # # The first prisoner selected turns the light off whenever it is found on. Each other prisoner turn the light on the very first time they find it off, Otherwise, they are to leave it in the state they found it. When the first prisoner selected leaves the light off for the 5th time. They can try to leave the room safely
# #
# #
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traversal(self, root):
    res = []
    if root:
        traversal(root.left)
        res.append(root.data)
        res = res + self.inorderTraversal(root.right)
    return res

# pseudocode for a function to traverse through each element in a binary tree
def ptraverse(root):
    # Set current to root of binary tree
    current = root
    stack = []  # initialze stack
    done = 0

    while not done:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

        # get back from the empty subtree to the top node and visit the Node
        # if the stack is empty you are done
        else:
            # current is None, reassgin its parent Node to current, and check the right node of parent node
            if len(stack) > 0:
                # assign current with parent node
                current = stack.pop()
                print(current.data)

                # check right node

                current = current.right

            else:
                done = 1


# Driver program to test above function

""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

ptraverse(root)


def findZeros(n):
    """

    :param n:
    :return:
    """
    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 2 and
    # update Count
    i = 2
    while (n / i >= 1):
        count += int(n/i)
        i *= 2

    return int(count/4)

print(findZeros(222))


import string
digit = string.digits+'ab'

def int12base(x):
    if x < 0:
        sign = -1
    elif x == 0:
        return digit[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:

        digits.append(digit[int(x % 12)])
        x = int(x / 12)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

print(int12base(10))





def get3(array, sum):
    array.sort()
    size = len(array)
    left = 0
    right = size-1
    # iterate array,
    numbers=[]
    for x in range(0, size-2):
        left = x+1
        right = size -1
        while left < right:
            if array[x]+array[left]+array[right] == sum:
                numbers.append([array[x],array[left], array[right]])
                left += 1
                right -= 1
            if array[x]+array[left]+array[right] < sum:
                left += 1
            else:
                right -= 1
    return numbers

myarray = [22, 6, 45, 40, 10, 18, 21]
print(get3(myarray, 72))