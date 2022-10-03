#include<stdio.h>
#include<stdlib.h>

#define N 5
int stack[N];
int top=-1;
void push()
{
	int x;
	printf("enter element:");
	scanf("%d",&x);
	if(top==N-1)
		printf("stack is full\n");
	else
	{
		top++;
		stack[top]=x;
	}
}
void pop()
{
	int item;
	if(top==-1)
		printf("stack is empty\n");
	else
	{
		item=stack[top];
		top--;
		printf("poped element is :%d\n",item);
	}
}
void display()
{
	int i;
	for(i=top;i>=0;i--)
	{
		printf("pushed element is: %d\n",stack[i]);
	}
}
/*void main()
  {
  push();
  push();
  push();
  display();
  pop();
  display();
  }*/
void main()
{
	int ch;
	do
	{
		printf("enter choice:1)push 2)pop 3)display 4)exit\n");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:push();
			       break;
			case 2:pop();
			       break;
			case 3:display();
			       break;
		        case 4:exit(0);
			default:printf("Invalid choice");
		}
	}while(ch!=0);
	scanf("%d",&ch);
}
