#include<stdio.h>

int main()

{

int ones=0,zeroes=0,num;

printf("enter a number:\n");

scanf("%d",&num);



        while(num>0)

        {

                int k=num%2;

                num=num/2;

                if(k)

                        ones++;

		else

			zeroes++;

        }

        printf("number of ones are:%d\n number of zeroes are:%d\n",ones,zeroes);



}
