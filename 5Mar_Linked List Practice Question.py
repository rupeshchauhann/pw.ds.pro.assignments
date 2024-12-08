# 1. Define a Doubly Linked List
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# 2. Reverse a Linked List In-Place
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 3. Detect Cycle in a Linked List
# Using Floyd's Cycle Detection Algorithm
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 4. Merge Two Sorted Linked Lists
def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next

# 5. Remove Nth Node from the End of a Linked List
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next

# 6. Remove Duplicates from a Sorted Linked List
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# 7. Find the Intersection of Two Linked Lists
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    a, b = headA, headB

    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

# 8. Rotate a Linked List by k Positions to the Right
def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the length of the list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Make the list circular
    tail.next = head

    # Find the new head
    k = k % length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head

# 9. Add Two Numbers Represented by Linked Lists
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# 10. Clone a Linked List with Next and Random Pointer
class RandomListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def clone_random_list(head):
    if not head:
        return None

    # Step 1: Create new nodes
    current = head
    while current:
        new_node = RandomListNode(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the lists
    current = head
    new_head = head.next
    while current:
        temp = current.next
        current.next = temp.next
        current = current.next
        if temp.next:
            temp.next = temp.next.next

    return new_head

# 11. Clone a Linked List with Arbitrary Pointers in O(N) Time
# This is functionally the same as #10 but generalized for 'arbit' pointers.
# Use the same method as described above.
