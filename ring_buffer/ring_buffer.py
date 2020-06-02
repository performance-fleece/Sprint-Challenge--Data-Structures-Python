from double import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if empty
        # add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        # if full
        elif self.storage.length == self.capacity:
            # if current is None/head,
            if self.current == None:
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)

            #  current is tail, set to head/None

            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = None
            # not head/tail
            else:
                self.current = self.current.next
                self.current.prev.delete()
                self.current.insert_before(item)

    def get(self):
        ring_buffer_items = []

        current = self.storage.head
        while current.next:
            ring_buffer_items.append(current.value)
            current = current.next
        ring_buffer_items.append(current.value)
        return ring_buffer_items
