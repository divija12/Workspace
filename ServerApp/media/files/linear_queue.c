#include <stdio.h>
#define max 5
int queue[5];
int front = -1;
int rear = -1;
int isEmpty()
{
    if(front == -1 && rear == -1)
        return 1;
    else
        return 0;
}
int isFull()
{
     if(rear == max - 1)
        return 1;
    else
        return 0;
}
void Enqueue(int n)
{
    if(isFull() == 0)
    {
        if(isEmpty())
            front = rear = 0;
        else
            rear += 1;
        queue[rear] = n;
    }
    else
        printf("Queue is full\n");
}
void Dequeue()
{
    if(isEmpty())
        printf("Queue is empty\n");
    else
    {
        printf("Deleted element is %d\n",queue[front]);
        front += 1;
    }
}
void get_front()
{
    printf("Element at front is %d\n",queue[front]);
}
void get_rear()
{
    printf("Element at rear is %d\n",queue[rear]);
}
void display()
{
    if(isEmpty())
        printf("Queue is Empty, no elements to display\n");
    int i;
    printf("Queue : ");
    for(i=front;i<=rear;i++)
        printf("%d  ",queue[i]);
    printf("\n");
}
int main()
{
    Enqueue(5);
    get_front();
    Enqueue(10);
    Enqueue(12);
    Enqueue(25);
    Enqueue(50);
    Enqueue(100);
    display();
    get_rear();
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    Dequeue();
    display();
}