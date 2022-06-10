#include "lists.h"

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *start;

	start = *head;
	*head->next = start;
	start->prev = *head;
	*head->n = n;
	if (*head == NULL)
		return (NULL)
	return (**head);
}
