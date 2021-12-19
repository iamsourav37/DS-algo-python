from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def get_size(self):
        if self.head is None:
            return 0
        else:
            iter = self.head
            length = 0
            while iter is not None:
                length += 1
                iter = iter.link
            return length

    def insert_first(self, data):
        self.head = Node(data=data, link=self.head)

    def insert_last(self, data):
        if self.head is None:
            self.insert_first(data)
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = Node(data=data, link=None)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_size():
            raise IndexError(f"Invalid index {index}")
        elif index == 0:
            self.insert_first(data)
        else:
            temp = self.head
            counter = 0
            while counter != index-1:
                temp = temp.link
                counter += 1
            new_node = Node(data=data, link=temp.link)
            temp.link = new_node

    def insert_after(self, key, data):
        if self.head is None:
            print("list is empty")
            return
        else:
            temp = self.head
            while temp:
                if temp.data == key:
                    new_node = Node(data=data, link=temp.link)
                    temp.link = new_node
                    return
                else:
                    temp = temp.link
            else:
                print(f"{key} is not found")

    def insert_before(self, key, data):
        if self.head is None:
            print("list is empty")
            return
        else:
            if self.head.data == key:
                self.insert_first(data)
                return
            else:
                temp = prev = self.head
                while temp:
                    if temp.data == key:
                        new_node = Node(data=data, link=prev.link)
                        prev.link = new_node
                        return
                    else:
                        prev = temp
                        temp = temp.link
                else:
                    print(f"{key} is not found")

    def delete_first(self):
        pass

    def delete_last(self):
        pass

    def delete_at(self, index):
        pass

    def delete_after(self, key):
        pass

    def delete_before(self, key):
        pass

    def find_mid(self):
        pass

    def show(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            list = ""
            temp = self.head
            while temp:
                list += f"{temp.data}--->"
                temp = temp.link
            list += "None"
            print(list)






