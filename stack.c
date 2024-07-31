#include<stdio.h>

struct Node {
    int data;
    struct Node *next;
};

struct Node *top = NULL;

void push(int value) {
    struct Node *newNode;
    newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = top;
    top = newNode;
}

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

void peek() {
    if (top == NULL) {
        printf("Stack is Empty\n");
    } else {
        printf("Top element is %d\n", top->data);
    }
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
    push(10);
    push(20);
    push(30);
    display();
    peek();
    pop();
    display();
    peek();
    return 0;
}
