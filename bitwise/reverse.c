#include<stdio.h>

int main()

{

	int num,y;

	printf("enter a number:\n");

	scanf("%d",&num);

printf("reverse bits are:");

        while(num>0)

        {

               int y=num&1;

                num=num>>1;

                printf("%d",y);

        }

}
