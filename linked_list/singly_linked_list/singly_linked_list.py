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
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.link

    def delete_last(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            prev = temp

            while temp.link:
                prev = temp
                temp = temp.link
            prev.link = None

    def delete_at(self, index):
        if self.head is None:
            print("list is empty")
        elif index < 0 or index >= self.get_size():
            raise IndexError(f"Invalid index {index}")
        elif index == 0:
            self.delete_first()
        else:
            counter = 0
            temp = self.head

            while counter != index-1:
                temp = temp.link
                counter += 1
            temp.link = temp.link.link

    def get_mid(self):
        if self.head is None:
            print("list is empty")
            return
        length = self.get_size()
        mid = length // 2
        print(f"Middle node of the list is : {self.__get(mid)}")

    def get_value_at(self, index):
        if index < 0 or index >= self.get_size():
            raise IndexError(f"Invalid index {index}")
        else:
            return self.__get(index)

    def __get(self, index):
        """ this is a private method """
        temp = self.head
        counter = 0

        while counter != index:
            counter += 1
            temp = temp.link
        return temp.data


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






