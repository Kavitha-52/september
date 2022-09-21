#include<stdio.h>

#define BITS 4

int main()

{

	int num,msb;

	printf("enter a number:\n");

	scanf("%d",&num);

msb=1<<(BITS-1);

        if(num & msb)

                printf("msb of %d is set\n",num);

        else

                printf("msb of %d is not set\n",num);

}



