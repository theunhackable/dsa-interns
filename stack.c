#include<stdio.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *top = NULL;


void display() {
    struct Node *current;
    current = top;
    if (current == NULL) {
        printf("Stack is empty\n");
    } else {
        while (current != NULL) {
            printf("%d\n", current->data);
            current = current->next;
        }
    }
}
void push(int value) {
    struct Node *newNode;
    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = top;
    top = newNode;
}



void pop() {
    struct Node *temp;
    temp = top;
    if (top == NULL) {
        printf("Stack is empty\n");
    } else {
        printf("The popped element is %d\n", top->data);
        top = top->next; 
        free(temp);
    }
}

int main() {
    push(11);
    push(13);
    push(14);
    push(15);
    push(18);
    display();
    peek();
    pop();
    display();
    return 0;
}
