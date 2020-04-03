import math
import os
import random
import re
import sys

import initiali
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if head==None:
        return

    while head!=None:
        print(head.data)
        head= head.next
    return


llist_count = 2
k = [4,5]
llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(k[_])
    llist.insert_node(llist_item)

printLinkedList(llist.head)
