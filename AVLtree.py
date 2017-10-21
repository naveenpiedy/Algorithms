from texttable import Texttable
from collections import deque

class Bst_node:
    def __init__(self, value=None, key=None, parent = None, height=(0, 0)):
        self.left_child = None
        self.parent = parent
        self.right_child = None
        self.balance_factor = 0
        self.value = value
        self.key = key

    def __getitem__(self):
        return self.value


class Bst:
    def __init__(self):
        self.root = Bst_node()

    def additem(self, key, value):
        current_node = None
        #print(self.root.key)
        if self.root.key == None:
            self.root.key = key
            self.root.value = value
        else:
            current_node = self.root
            self.additemr(current_node, key, value)

    def additemr(self, current_node, key, value):
        #print(key)
        if key == current_node.key:
            raise Exception('Key Already Exists')
        elif key < current_node.key:
            if current_node.left_child is not None:
                # current_node.height[0] = current_node.height[0] + 1
                #print(current_node.key, key)
                current_node = current_node.left_child
                #print(current_node.key, current_node.value)
                self.additemr(current_node, key, value)
            else:
                current_node.left_child = Bst_node(value, key, current_node)
                #current_node.left_child.parent = current_node
                self.update_balances(current_node.left_child)
                # current_node.height[0] = current_node.height[0] + 1
        elif key > current_node.key:
            if current_node.right_child is not None:
                # current_node.height[1] = current_node.height[1] + 1
                current_node = current_node.right_child
                self.additemr(current_node, key, value)
            else:
                current_node.right_child = Bst_node(value, key, current_node)
                #current_node.right_child.parent = current_node
                self.update_balances(current_node.right_child)

    def update_balances(self, current_node):
        if current_node.parent is not None:
            if current_node.parent.left_child == current_node:
                current_node.parent.balance_factor += 1
            elif current_node.parent.right_child == current_node:
                current_node.parent.balance_factor -= 1

        if current_node.balance_factor > 1 or current_node.balance_factor < -1:
            self.rebalance_tree(current_node)

            if current_node.parent.balance_factor != 0:
                self.update_balances(current_node.parent)


    def rebalance_tree(self, current_node):
        #print("jekk", current_node.key)
        if current_node.balance_factor < 0:
            if current_node.right_child.balance_factor > 0 :
                self.right_rotate(current_node.right_child)
                self.left_rotate(current_node)
            else:
                self.left_rotate(current_node)
        elif current_node.balance_factor > 0:
            if current_node.left_child.balance_factor < 0:
                self.left_rotate(current_node.left_child)
                self.right_rotate(current_node)
            else:
                self.right_rotate(current_node)

    def right_rotate(self, current_node):
        new_root = current_node.left_child
        if current_node == self.root:
            self.root = new_root
        if new_root.right_child != None:
            current_node.left_child = new_root.right_child
        else:
            current_node.left_child = None
        new_root.right_child, new_root.parent = current_node, current_node.parent
        current_node.balance_factor = current_node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + max(current_node.balance_factor, 0)


    def left_rotate(self, current_node):
        new_root = current_node.right_child
        if current_node == self.root:
            self.root = new_root
        if new_root.left_child != None:
            current_node.right_child = new_root.left_child
        else:
            current_node.right_child = None
        new_root.left_child, new_root.parent = current_node, current_node.parent
        current_node.balance_factor = current_node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor -1 + max(current_node.balance_factor, 0)

    def __inorder(self, current_node = None):
        if current_node is None:
            current_node = self.root
        if current_node.left_child is not None:
            yield from self.__inorder(current_node.left_child)
        yield current_node
        #print("Inorder", current_node.key)
        if current_node.right_child is not None:
            yield from self.__inorder(current_node.right_child)


    def __preorder(self, current_node = None):
        if current_node is None:
            current_node = self.root
        yield current_node
        if current_node.left_child is not None:
            yield from self.__preorder(current_node.left_child)
        if current_node.right_child is not None:
            yield from self.__preorder(current_node.right_child)

    def __postorder(self, current_node = None):
        if current_node is None:
            current_node = self.root
        if current_node.left_child is not None:
            yield from self.__postorder(current_node.left_child)
        if current_node.right_child is not None:
            yield from self.__postorder(current_node.right_child)
        yield current_node

    def __level_order(self, current_node = None):
        if current_node is None:
            current_node = self.root
        queue_inoperation = deque()
        list_to_be_sent = []
        queue_inoperation.append(current_node)
        while queue_inoperation:
            node_branching = queue_inoperation.popleft()
            list_to_be_sent.append(node_branching)
            if node_branching.left_child is not None:
                queue_inoperation.append(node_branching.left_child)
            if node_branching.right_child is not None:
                queue_inoperation.append(node_branching.right_child)

        self.__print_table(list_to_be_sent)


    def print_inordertable(self):
        inorder_list = self.__inorder()
        print("Inorder of tree")
        self.__print_table(inorder_list)

    def print_preordertable(self):
        preorder_list = self.__preorder()
        print("Preorder of Tree")
        self.__print_table(preorder_list)

    def print_postordertable(self):
        postorder_list = self.__postorder()
        print("Postorder of Tree")
        self.__print_table(postorder_list)

    def print_levelordertable(self):
        print("Level order of Tree")
        self.__level_order()

    def __print_table(self, list_to_be_printed):
        table = Texttable()
        table.add_rows([["Key", "Left_Child", "Right_Child", "Parent", "Balance Factor"]])
        for i in list_to_be_printed:
            # print(i.key)
            if i.parent is None:
                table.add_row([i.key, i.left_child.key, i.right_child.key, "Root", i.balance_factor])
            else:
                if i.left_child is not None and i.right_child is not None:
                    table.add_row([i.key, i.left_child.key, i.right_child.key, i.parent.key, i.balance_factor])
                elif i.right_child is not None:
                    table.row([i.key, "None", i.right_child.key, i.parent.key, i.balance_factor])
                elif i.left_child is not None:
                    table.add_row([i.key, i.left_child.key, "None", i.parent.key, i.balance_factor])
                else:
                    table.add_row([i.key, "None", "None", i.parent.key, i.balance_factor])
        print(table.draw())


# def main():
#     bsttree = Bst()
#     bsttree.additem(5, "Add")
#     bsttree.additem(7, "Add")
#     bsttree.additem(9, "Add")
#     bsttree.additem(6, [1,2,3,4,5])
#     bsttree.additem(4, 4578544)
#     bsttree.additem(1,5555)
#     #print(bsttree.root.key)
#     #print(bsttree.root.key, bsttree.root.value, bsttree.root.left_child.key, bsttree.root.right_child.key,
#         # bsttree.root.balance_factor)
#     bsttree.print_inordertable()
#     print("\n \n")
#     bsttree.print_preordertable()
#     print("\n \n")
#     bsttree.print_postordertable()
#     print("\n \n")
#     bsttree.print_levelordertable()
#    #print(listo)
#     # bsttree.print_inordertable()
#     # table = Texttable()
#     # table.add_rows([["Key", "Left_Child", "Right_Child", "Parent", "Balance Factor"]])
#     # for i in listo:
#     #     #print(i.key)
#     #     if i.parent is None:
#     #         table.add_row([i.key, i.left_child.key, i.right_child.key,"Root",i.balance_factor])
#     #     else:
#     #         if i.left_child is not None and i.right_child is not None:
#     #             table.add_row([i.key, i.left_child.key, i.right_child.key,  i.parent.key, i.balance_factor])
#     #         elif i.right_child is not None:
#     #             table.row([i.key, "None",  i.right_child.key,  i.parent.key,  i.balance_factor])
#     #         elif i.left_child is not None:
#     #             table.add_row([i.key,  i.left_child.key, "None", i.parent.key, i.balance_factor])
#     #         else:
#     #             table.add_row([i.key, "None", "None", i.parent.key, i.balance_factor])
#     # print(table.draw())
#
# if __name__ == '__main__':
#     main()




