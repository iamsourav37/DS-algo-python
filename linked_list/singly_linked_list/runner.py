from singly_linked_list import SinglyLinkedList


if __name__ == "__main__":
    singly_list = SinglyLinkedList()

    singly_list.insert_first(12)
    singly_list.insert_first(90)
    singly_list.insert_first(21)

    singly_list.insert_last(33)
    singly_list.insert_last(36)
    singly_list.insert_last(32)

    singly_list.insert_at(1, 111)
    singly_list.insert_at(2, 222)
    singly_list.insert_at(5, 555)
    singly_list.insert_at(4, 4433)

    singly_list.insert_after(12, 122112)
    singly_list.insert_after(90, 900009)

    singly_list.insert_before(12, 110001)
    singly_list.insert_before(21, 20)

    singly_list.delete_last()
    singly_list.delete_last()
    singly_list.delete_last()

    singly_list.delete_first()
    singly_list.delete_first()

    singly_list.delete_at(2)
    singly_list.delete_at(4)

    singly_list.get_mid()

    singly_list.show()

    print(f"node at 2 is {singly_list.get_value_at(2)}")
