// Importa el módulo standard de Input / Output
#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int data;
    struct node* next;
} node;

node *head;
head = (node*)malloc(sizeof(node));
head->data = 1;
head->next = (node*)malloc(sizeof(node));
node* create (int data, node* next)
{
    node *new_node = (node*)malloc(sizeof(node));
    if (new_node == NULL){
        printf("Error creating new node\n");
        exit(0);
    }
    new_node->data = data;
    new_node->next = next;

    return new_node;
}

void print_list(node *head){
    node *current = head

    while (current != NULL){
        printf("%d\n", current->data);
        current = current->next;
    }
}


int main(){
    print_list
}