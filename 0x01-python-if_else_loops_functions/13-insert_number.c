#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *start;
	listint_t *temp;

	start = *head;
	while(start != NULL)
	{
		if(start->n < number)
			start = start->next;
		else
			break;
	}
	temp = start;
	temp
