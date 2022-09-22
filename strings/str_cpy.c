#include<stdio.h>

int main()

{

	char a[]="hii";

	char b[20];

	int i=0;

	while(a[i]!='\0')

	{

		b[i]=a[i];

		i++;

	}

	b[i]='\0';

	printf("string copied:%s",b);

}

