#include<stdio.h>

#include<stdlib.h>



typedef struct stu

{

	int data;

	struct stu *link;

}S;





S *head=NULL;

void insert(int data)

{

	S *temp=NULL;

	S *new=malloc(sizeof(S));

	if(new==NULL)

		printf("Memory is not allocated\n");

	else

	{

		if(head==NULL)

		{

			head=new;

			new->data=data;

			new->link=new;

		}

		else

		{

			new->data=data;

			new->link=head->link;

			head->link=new;

			head=new;

		}	

	}

}

/*

void print(S *ptr)

{

	if(ptr==NULL)

		printf("list is empty\n");

	else

	{

		///S *temp=ptr;

		while(ptr != NULL)

		{

			printf("%d ",ptr->data);

			ptr=ptr->link;

		}

		printf("\n");

	}

}

*/

void print()

{

	S *temp=head;

	if(temp==NULL)

		printf("list is empty\n");

	else

	{	

		temp=temp->link;

		do

		{

		printf("%d\n",temp->data);

		temp=temp->link;

		}while(temp != head->link);

		printf("%d\n",temp->data);



	}

}

int main()

{

int i,data,size;

printf("Enter the size of linked list: ");

scanf("%d",&size);

for(i=0;i<size;i++)

{

	printf("Enter data:");

	scanf("%d",&data);

	insert(data);

}

print();

return 0;

}











