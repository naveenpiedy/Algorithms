from texttable import Texttable
from collections import deque

class Node:
    def __init__(self, letter = None, word_ends = None, ):
        self.letter = letter
        self.word_ends_here = word_ends
        self.children = dict()

    def addChildren(self, letter, data = None):
        if not isinstance(letter, Node):
            self.children[letter] = Node(letter, data)
        else:
            self.children[letter.letter] = letter

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        current_node = self.root
        word_ended = True
        stops_here = 0

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_ended = False
                stops_here = i
                break

        if not word_ended:
            while stops_here < len(word):
                current_node.addChildren(word[stops_here])
                current_node = current_node.children[word[stops_here]]
                stops_here +=1

        current_node.word_ends_here = word

    def print_table(self):
        current_node = self.root
        bfs_q = deque()
        bfs_q.append(current_node)
        level_order_list = []
        while bfs_q:
            temp = bfs_q.popleft()
            level_order_list.append(temp)
            #print(temp.children)
            for i, j in temp.children.items():
                bfs_q.append(j)

        table = Texttable()
        table.add_rows([['Letter', 'Children', 'Word']])
        for i in level_order_list:
            if i.word_ends_here:
                table.add_row([i.letter, i.children, i.word_ends_here])
            else:
                table.add_row([i.letter, i.children, "No End word"])

        print(table.draw())

# def main():
#     trie = Trie()
#     words = "hello"
#     for word in words.split():
#         trie.add_word(word)
#     trie.print_table()
#
# if __name__ == '__main__':
#     main()

