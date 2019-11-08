import doubly_linked_list


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        queue_store = doubly_linked_list.DoublyLinkedList()
        self.storage = queue_store

    def enqueue(self, item):
        return self.storage.add_to_head(item)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return len(self.storage)
