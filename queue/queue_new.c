#include <stdio.h>
#include <stdlib.h>

#define N 20

typedef struct Queue {
    int* arr;
    int front;
    int back;
} Queue;

Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->arr = (int*)malloc(N * sizeof(int));
    q->front = -1;
    q->back = -1;
    return q;
}

void push(Queue* q, int x) {
    if (q->back == N - 1) {
        printf("Queue Overflow\n");
        return;
    }
    q->back++;
    q->arr[q->back] = x;
    if (q->front == -1) {
        q->front++;
    }
}

void pop(Queue* q) {
    if (q->front == -1 || q->front > q->back) {
        printf("No Elements in Queue\n");
        return;
    }
    q->front++;
}

int peek(Queue* q) {
    if (q->front == -1 || q->front > q->back) {
        printf("No elements in queue\n");
        return -1;
    }
    return q->arr[q->front];
}

int empty(Queue* q) {
    return (q->front == -1 || q->front > q->back);
}

int main() {
    Queue* q = createQueue();
    push(q, 1);
    push(q, 2);
    push(q, 3);
    push(q, 4);

    printf("%d\n", peek(q)); 
    pop(q);

    printf("%d\n", peek(q));
    pop(q);

    printf("%d\n", peek(q));
    pop(q);

    printf("%d\n", peek(q));
    pop(q);

    printf("%d\n", empty(q));

    free(q->arr); // Manually free the allocated memory
    free(q); // Manually free the allocated memory
    return 0;
}
