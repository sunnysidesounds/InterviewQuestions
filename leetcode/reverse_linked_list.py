

"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL


  public static Node reverseIterative(Node node){
        if(node == null || node.next == null){
            return node;
        }
        Node previous = null;
        Node current = node;
        while(current != null){
            Node next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        return previous;
    }


"""

def reverse_linked_list(head):
    if not head or not head.next:
        return head

    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous




if __name__ == '__main__':
    pass
