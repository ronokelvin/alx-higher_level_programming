#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: structure for a singly linked list node
 * used in the context of a Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints elements of a singly linked list.
 * @h: Pointer to the head node of the list.
 *
 * Return: Number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: Pointer to the head node of the list.
 * @n: Value to be stored in the new node.
 *
 * Return: Address of the newly created node.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees memory allocated for a linked list.
 * @head: Pointer to the head node of the list.
 */
void free_listint(listint_t *head);

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to a pointer to the head node of the list.
 *
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
