
class SinglyLinkedList(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def from_list(vals: list):
        head = SinglyLinkedList(vals[0])
        current = head
        for i in vals[1:]:
            current.next = SinglyLinkedList(i)
            current = current.next

        return head

    @staticmethod
    def from_list_recursive(vals: list):
        if len(vals) == 0:
            return None

        current = SinglyLinkedList(vals[0])
        current.next = SinglyLinkedList.from_list_recursive(vals[1:])

        return current

    def print(self, isHead=True):

        if self.next == None:
            return f"{{ {self.value} , None }}"

        printed = f"{{ {self.value}, {self.next.print(False)} }}"

        if(isHead):
            print(printed)
        else:
            return printed


ll = SinglyLinkedList.from_list(range(10))
ll.print()
