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
S *reverse(S *ptr)
{
S *prev=NULL;
S *cur=NULL;
S *next=NULL;

if(ptr==NULL)
printf("List is empty\n");
else if(ptr->link==NULL)
printf("list has only 1 element\n");
else
{
next=ptr;
while(next)
{
prev=cur;
cur=next;
next=next->link;
cur->link=prev;
}
ptr=cur;
}
return ptr;

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
printf("Before reverse the linked list:\n");
print(head);
head=reverse(head);
printf("After reverse the linked list:\n");
print(head);
return 0;
}


/*
int main()
{  
       int size,i,data,choice;
        printf("Enter the size of linked list: ");
        scanf("%d",&size);
	while(1)
	{
		printf("1.add_first 2.display 3.reverse 4 exit\n");
		printf("enter ur choice\n");
		scanf("%d",&choice);
		
		switch(choice)
		{
			case 1:
			      for(i=0;i<size;i++)
                                {
	                         printf("Enter data:");
	                         scanf("%d",&data);
	                         insert(data);
                                } 
	                        break;
			case 2:print(head);
			       break;
			case 3:head=reverse(head);
			       printf("after reverse the linked list:\n");
			       print(head);
			       break;
			case 4:exit(0);
		}
		
	}
}*/
