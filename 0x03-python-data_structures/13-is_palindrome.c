#include "lists.h"
#include <stddef.h>
void reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer
 * Return: 0, or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *mid_node = NULL;
	int res = 1;
	listint_t *second_half = slow;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}
		prev_slow->next = NULL;
		reverse_list(&second_half);
		res = compare_lists(*head, second_half);
		reverse_list(&second_half);
		if (mid_node != NULL)
		{
			prev_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (res);
}
/**
 * reverse_list - used to reverse a list
 * @head: double pointer
 * Return: 0
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * compare_lists - compares two lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 0
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n == list2->n)
		{
			list1 = list1->next;
			list2 = list2->next;
		}
		else
			return (0);
	}
	if (list1 == NULL && list2 == NULL)
		return (1);
	return (0);
}

