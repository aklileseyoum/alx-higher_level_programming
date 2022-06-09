#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
	int i;

	i = 0;
	while (start != NULL){
		printf("%d", start->n);
		start = start->next;
		i++;
	}

	return (i);
}
