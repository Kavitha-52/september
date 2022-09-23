#include<stdio.h>

#include<stdlib.h>

typedef struct stu

{

	int id;

	char name[10];

	float marks;

	struct stu *link;

}S;



S* head=NULL;



void insert()

{

	S *temp=NULL;

	S* new=malloc(sizeof(S));

	if(new==NULL)

		printf("memory not alloacted:\n");

	else

		{

			printf("enter id,name and marks :\n");

			scanf("%d %s %f",&new->id,new->name,&new->marks);

			new->link=NULL;

			if(head==NULL)

				head=new;

			else

			{

				temp=head;

				while(temp->link!=NULL)

				{

					temp=temp->link;

				}

				temp->link=new;

			}

		}

}



void print(S* ptr)

{

	if(ptr==NULL)

		printf("list is empty:\n");

	else

		printf("student details are:\n");

		while(ptr!=NULL)

		{

			printf("%d %s %f\n",ptr->id,ptr->name,ptr->marks);

			ptr=ptr->link;

		}

	

}



S * delete_position(int p)

{

S * ptr,*preptr;

ptr=head->link;

preptr=head;

for(int i=1;i<(p-1);i++)

{

	ptr=ptr->link;

	preptr=preptr->link;

}

preptr->link=ptr->link;

free(ptr);

return head;

}





void delete_head()

{

	S *ptr=head;

	head=head->link;

	free(ptr);

	

}



void insert_beforekey(int key)

{

	S *temp1,*temp2;

	temp1=head;

	S* new=malloc(sizeof(S));

	printf("enter id name and marks:\n");

        scanf("%d %s %f",&new->id,new->name,&new->marks);



	while(temp1->link!=NULL)

        {

		if(temp1->id==key)

		{

                 temp2->link=new;

		 new->link=temp1;

		 break;

		}

		else 

		{

			temp2=temp1;

			temp1=temp1->link;

		}

	}

}



void insert_at_first()

{

        S* new=malloc(sizeof(S));

        printf("enter id name and marks:\n");

        scanf("%d %s %f",&new->id,new->name,&new->marks);

	new->link=head;

	head=new; 

}



int main()

{

	int ch,size,i,p,key;

	do

	{

	printf("enter a choice:1.insert 2.print 3.delete_position 4.delete_head 5.insert before key 6.insert at first\n");

	scanf("%d",&ch);

	switch(ch)

	{

		case 1:printf("enter the size of linked list:\n");

		       scanf("%d",&size);

		       for(i=0;i<size;i++)

		       {

			       insert();

		       }

		       break;



		case 2: print(head);

			break;



		case 3:printf("enter position to delete:\n");

		       	scanf("%d",&p);

		       	head=delete_position(p);

		       	break;



		case 4:printf("after head node deletion:\n");

		       delete_head();

		       break;



		case 5:printf("enter key:\n");

		       scanf("%d",&key);

		       insert_beforekey(key);

		       break;



		case 6:	insert_at_first(key);

			break;

	}

	}while(ch!=0);

}





