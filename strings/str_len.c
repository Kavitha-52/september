#include<stdio.h>

int str_len(char str[10])

{

	int i=0;

	while(str[i]!='\0')

	{

		i++;

	}

	return i;

	

}



int main()

{

	char str[10];

	printf("enter a string:\n");

	scanf("%s",str);

	int x=str_len(str);

	printf("string length:%d",x);

}
