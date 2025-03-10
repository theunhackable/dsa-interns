#include<stdio.h>

struct node{
    int data;
    struct node *link;
};

struct node *top=NULL;

void push(int x){
    struct node *newnode;
    newnode=(struct node*)malloc(sizeof(struct node));
    newnode->data=x;
    newnode->link=top;
    top=newnode;
}

void display(){
    struct node *temp;
    temp=top;
    if(temp==NULL){
        printf("Stack is empty");
    }
    else{
        while(temp!=NULL){
        printf("%d\n",temp->data);
        temp=temp->link;
    }
    }
}

void peek(){
    if(top==NULL){
        printf("Stack is Empty");
    }
    else{
        printf("Top element is %d",top->data);
    }
}

void pop(){
    struct node *temp;
    temp=top;
    if(top==NULL){
        printf("Stack is empty");
    }
    else{
        printf("The popped element is %d",top->data);
        top=top->link; // can also use temp->link as both are pointing to the same node
        free(temp);
    }
}