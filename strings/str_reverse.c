#include<stdio.h>

void str_reverse(char str[10])

{

	int i=0,j=0;

	while(str[j]!='\0')

        {

        j++;

	}

        j=j-1;

	while(i<j)

	{

		char temp=str[i];

		str[i]=str[j];

		str[j]=temp;

		i++;

		j--;

                }

	printf("%s",str);



}

int main()

{

        char str[10];

        printf("enter a string:\n");

        scanf("%s",str);

        str_reverse(str);

}

