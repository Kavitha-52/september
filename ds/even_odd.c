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

		new->data=data;

		new->link=NULL;

		if(head==NULL)

		{

			head=new;

		}

		else

		{

			temp=head;

			while(temp->link != NULL)

			{

				temp=temp->link;

			}

			temp->link=new;

		}	

	}

}





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





void print_even()

{

int count=1;

if(head==NULL)

	printf("List is empty!\n");

else

    {

      S *temp=head;

      while(temp!=NULL)

      {

        if(count%2==0)

         {

           printf("even nodes : %d\n",temp->data);

         }

        count++;

        temp=temp->link;

     }

     printf("\n");

   }

     

}

    

    

void print_odd()

{

int count=1;

if(head==NULL)

	printf("List is empty!\n");

else

    {

      S *temp=head;

      while(temp!=NULL)

      {

        if(count%2 !=0)

         {

           printf("odd nodes : %d\n",temp->data);

         }

        count++;

        temp=temp->link;

     }

     printf("\n");

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

print(head);

print_even();

print_odd();

return 0;

}



