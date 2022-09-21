#include<stdio.h>

int main()

{

	int num;

	printf("enter a number:\n");

	scanf("%d",&num);

if(num&1)// lsb & even odd both same logic

                printf("odd\n");

        else

                printf("even\n");

}



