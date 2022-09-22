#include<stdio.h>

int main()

{

        char a[]="hello";

        char b[20]="world";

        int i=0,j=0;

        while(a[i]!='\0')

        {

		i++;

	}

	while(b[j]!='\0')

	{

                a[i]=b[j];

                i++;

		j++;

        }

        a[i]='\0';

        printf("string concatination:%s",a);

}

