#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - An fxn that checks if a list is a palindrome.
 * @head: A ptr to the ptr to the head of the linked list
 * Return: 0 if list is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *quick = *head;
	listint_t *timid = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1); /*its a palindrome */
	while (quick != NULL && quick->next != NULL)
	{
		quick = quick->next->next;
		temp = timid->next;
		timid->next = prev;
		prev = timid;
		timid = temp;
	}

	if (quick != NULL)
		timid = timid->next;

	while (prev != NULL && timid != NULL)
	{
		if (prev->n != timid->n)
			return (0);
		prev = prev->next;
		timid = timid->next;
	}

	return (1);
}
