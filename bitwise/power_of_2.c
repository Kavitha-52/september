#include<stdio.h>

int main()

{

        int num;

        printf("enter number:\n");

        scanf("%d",&num);

        if((num &(num-1))==0)

                printf("number is power of 2\n");

        else

                printf("number is not power of 2\n");

}

