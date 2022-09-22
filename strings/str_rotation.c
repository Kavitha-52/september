#include<stdio.h>

#include<string.h>

void str_rotation(char str[])

{

	int l=strlen(str);

	char temp=str[l-1];



	for(int i=l-1;i>=0;i--)

	{

		str[i]=str[i-1];

	}

	str[0]=temp;

	printf("%s\n",str);

}



int main()

{

	char str[20];

	printf("enter a string:\n");

	scanf("%s",str);

	for(int i=0;i<2;i++)

	{

		str_rotation(str);

	}

	return 0;

}

