/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Initial c solution, found after I created this repo. Apparently, I submitted it on Dec. 28, 2021.
// O(n) time complexity, but does iterate twice.

struct ListNode* middleNode(struct ListNode* head){
    int i = 0;
    struct ListNode* pos = head;
    while (pos != NULL) {
        i++;
        pos = pos->next;
    }
    for (int j = 0; j < i / 2; j++) {
        head = head->next;
    }
    return head;
}
