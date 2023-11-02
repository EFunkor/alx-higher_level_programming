#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks for singly linked list that has a cycle.
* @head: A ptr to head of the linked list.
*
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *head)
{
listint_t *slow = head; /* Slow pointer moves one step at a time */
listint_t *fast = head; /* Fast pointer moves two steps at a time */

if (head == NULL)
{
return (0); /* No cycle in empty list */
}

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
        return (1); /* Cycle detected */
}
}

return (0); /* No cycle found */
}
