#include<stdio.h>
#define N 5
int queue[N];
int front=-1;
int rear=-1;
void enqueue(int );
void dequeue();
void display();

int main()
{
	enqueue(2);
	enqueue(4);
	enqueue(6);
	display();
	dequeue();
	dequeue();
	enqueue(8);
	enqueue(10);
	display();
	dequeue();

}

void enqueue(int x)
{
	if(rear==N-1)
	{
		printf("Queue is full\n");
	}
	else if(front==-1 && rear==-1)
	{
		front=rear=0;
		queue[rear]=x;
	}
	else
	{
		rear++;
		queue[rear]=x;
	}
}

void dequeue()
{
	if(front==-1&&rear==-1)
	{
		printf("queue is empty\n");
	}
	else if(front==rear)
	{
		front=rear=-1;
	}
	else
	{
		printf("deque element is :%d\n",queue[front]);
		front++;
	}
}

void display()
{
	int i;
	if(front==-1&&rear==-1)
	{
		printf("queue is empty\n");
	}
	else
	{
		for(i=front;i<rear+1;i++)
		{
			printf("enque element is %d\n",queue[i]);
		}
	}
}
