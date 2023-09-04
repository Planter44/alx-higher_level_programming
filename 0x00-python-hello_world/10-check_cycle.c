#include "lists.h"

/**
 * check_cycle -Checks if linked list haves a cycle.
 * @list:the linked list.
 * Return: 1 if list haves a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
