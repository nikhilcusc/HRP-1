'''
You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.'''
import initiali


def mergeLists(head1, head2): #Not in place
    t1 = SinglyLinkedList()
    t1h = None
    #ta = []
    while head1 and head2:
        #print(head1.data,head2.data,ta)
        if head1.data<head2.data:
            t1.insert_node(head1.data)
            #ta.append(head1.data)
            head1=head1.next
        else:
            t1.insert_node(head2.data)
            #ta.append(head2.data)
            head2=head2.next
    if head2==None:
        while head1:
            t1.insert_node(head1.data)
            head1=head1.next
    if head1==None:
        while head2:
            t1.insert_node(head2.data)
            head2=head2.next
    #print('ta',ta)
    return t1.head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()


#input
'''
1 #queries
3 #number of elements in 1st list
1
2
3
2
3
4

1
3
4
5
6
3
1
2
10
'''