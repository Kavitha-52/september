#include<stdio.h>

int add(int *,int *);

int main()

{

        int a,b;

        printf("enter 2 numbers:\n");

        scanf("%d %d",&a,&b);

        int sum=add(&a,&b);

        printf("sum=%d\n",sum);

}

int add(int *a,int  *b)

{

        int sum=0;

        sum=*a+*b;

  return sum;

}

