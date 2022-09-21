#include<stdio.h>

int main()

{

	int num;

	printf("enter a number:\n");

	scanf("%d",&num);

        if(num & 1)

                printf("lsb of %d is set\n",num);

        else

                printf("lsb of %d is not set\n",num);

}



