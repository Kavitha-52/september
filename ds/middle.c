#include<stdio.h>

#include<stdlib.h>



typedef struct stu

{

	int data;

	struct stu *next;

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

			ptr=ptr->next;

		}

		printf("\n");

	}

}

*/

void print()

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

		}

		printf("\n");

	}

}





void print_middle()

{

S *slow_ptr=head;

S *fast_ptr=head;

if(head!=NULL)

{

while(fast_ptr!=NULL && fast_ptr->next!=NULL)

{



slow_ptr=slow_ptr->next;

fast_ptr=fast_ptr->next->next;

}

printf("middle element is [%d]\n",slow_ptr->data);

}

}





int search()

{

int element;

if(head==NULL)

{

	printf("list is empty\n");

}

else

{

	printf("enter the element to be searched:\n");

	scanf("%d",&element);

	S * temp=head;

	while(temp!=NULL)

	{

		if(temp->data==element)

		{

			printf("ELEMENT FOUND \n");

			exit(0);

		}

		else

		{

			temp=temp->next;

		}

	}

	printf("Searched element not found\n");

}

}







int main()

{

int i,data,size,element;

printf("Enter the size of linked list: ");

scanf("%d",&size);

for(i=0;i<size;i++)

{

	printf("Enter data:");

	scanf("%d",&data);

	insert(data);

}

//print(head);

print();



print_middle();

search();





return 0;

}





