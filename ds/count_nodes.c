#include<stdio.h>

#include<stdlib.h>



typedef struct stu

{

	int data;

	struct stu *next;

}S;

int count=0;

S *head=NULL;

void insert(int data)

{

	S *temp=NULL;

	S *new=malloc(sizeof(S));

	if(new==NULL)

		printf("Memory is not allocated\n");

	else

	{

		new->data=data;

		new->next=NULL;

		if(head==NULL)

		{

			head=new;

		}

		else

		{

			temp=head;

			while(temp->next != NULL)

			{

				temp=temp->next;

			}

			temp->next=new;

		}	

	}

}



int count_nodes()

//void count_nodes()

{

S *new=head;

while(new !=NULL)

{

new=new->next;

count++;

}

//printf("no. of nodes are:%d\n",count);

return count;

}





void display()

{

	if(head==NULL)

		printf("list is empty\n");

	else

	{

		S *temp=head;

		while(temp != NULL)

		{

			printf("%d ",temp->data);

			temp=temp->next;

			//count++;

		}

		printf("\n");

		//printf("No. of nodes are:%d\n",count);

	}

}



int main()

{  

     insert(1);

     insert(2);

     insert(3);

     insert(1);

     insert(2);

     insert(3);

     insert(10);

    display();

   int  x=count_nodes();

    printf("No. of nodes are :%d\n",x);

     return 0;

     }
