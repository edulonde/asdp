class Node:
    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:     #cria novo nó
            node = Node(label)
        if self.empty():     #verifica se a linha está vazia
            self.first = node
            self.last = node
        else:
            if index == 0:   #insere no início
                node.setNext(self.first)
                self.first = node
            elif index >= self.len_list: #insere no final
                self.last.setNext(node)
                self.last = node
            else: # insere no meio
                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1
                while curr_node != None:
                    if curr_index == index: #seta o curr_node como o proximo nó
                        node.setNext(curr_node)
                        prev_node.setNext(node) #seta o node como o proximo do prv_note
                        break
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index +=1
        self.len_list +=1 #atualizar lista

    def pop(self, index):
        if not self.empty() and index >= 0 and index < self.len_list:
            flag_remove = False
            if self.first.getNext() == None: #possui apenas um elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0: #remove do início mas possui mais de um elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:
                    if index == curr_index:
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index +=1
            if flag_remove:
                self.len_list -= 1
    def empty(self):
        if self.first == None:
            return True
        return False
    def lenght(self):
        return self.len_list
    def show(self):
        curr_node = self.first
        while curr_node != None:
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNext()
        print(' ')

lista = LinkedList()
lista.push('josé',0)
lista.push('Tuany',1)
lista.push('doug',0)
lista.push('catha',2)
lista.push('nuno',0)
lista.push('thud',2)
lista.show()
print(lista.lenght())
lista.pop(0)
lista.show()
print(lista.lenght())
lista.pop(0)
lista.show()
print(lista.lenght())
