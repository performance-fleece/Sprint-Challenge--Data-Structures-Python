from double import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #if empty
        ## add to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
        #if full 
        elif self.storage.length == self.capacity :
            # if current is None, 
            if self.current == self.current.head:
                self.current = self.storage.head.next
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
            
            # if full, current is tail, set to head

            elif self.current == self.storage.tail:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.current = self.current.head
                

        #storage full, current is not tail 

    def get(self):
        pass

