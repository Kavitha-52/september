#include<stdio.h>

int main()

{

	char a[]="helloworld";

	char b='l';

	int i=0,flag=0;

	while(a[i]!='\0')

	{

		if(a[i]==b)

		{

			flag=1;

			break;

		}

		i++;

	}

	if(flag==1)

		printf("first occurance at %d",i);

	else

		printf("the character not found");

}



