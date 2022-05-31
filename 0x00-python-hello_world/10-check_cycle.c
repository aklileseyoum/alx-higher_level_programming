#include "stdio.h"

int check_cycle(listint_t *list)
{
	listint_t *n;

	n = list;
	while(n != NULL)
	{
		n = n->next;
		if (n = list)
			return (1);
	}

	return (0);
}
