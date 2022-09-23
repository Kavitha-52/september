#include<stdio.h>

void charreplace(char *,char,char);

int main()

{

char str[20];

char ch1,ch2;

printf("enter a string:");

scanf("%s",str);

printf("enter a character to remove from the string:");

scanf("\n%c",&ch1);

printf("enter a character  need to replace:");

scanf("\n%c",&ch2);

charreplace(str,ch1,ch2);

return 0;

}

void charreplace(char *str, char ch1, char ch2)

{

	char *ptr=str;

	while(*str !='\0')

	{

		if(*str==ch1)

		{

			*str=ch2;

		}

		str++;

	}

	printf("%s",ptr);

	}
