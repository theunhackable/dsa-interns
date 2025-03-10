#include<stdio.h>

typedef struct node{
    int data;
    struct node *link;
}Node;

Node *front=NULL;
Node *rear=NULL;

void enqueue(int x){
    Node *newnode;
    newnode=(Node*)malloc(sizeof(Node));
    newnode->data=x;
    newnode->link=NULL;
    if(front==NULL && rear==NULL){
        front=rear=newnode;
    }
    else{
        rear->link=newnode;
        rear=newnode;
    }
}

void dequeue(){
    if(front==NULL && rear==NULL){
        printf("Queue is empty");
    }
    else{
    Node *temp;
    temp=front;
    front=front->link;
    free(temp);
    }
}

void peek(){
    if(front==NULL && rear==NULL){
        printf("Queue is empty");
    }
    else{
        printf("First element is : %d",front->data);
    }
}

int main(){
    enqueue(10);
    enqueue(20);
    enqueue(30);
    dequeue();
    peek();
}