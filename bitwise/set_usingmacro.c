

#include<stdio.h>

#define SET(num,pos) num |(0x1<<pos)

#define CLEAR(num,pos) num &(~(0x1<<pos))

#define TOGGLE(num,pos) num ^(0x1<<pos)

int main()

{

        int num,pos,set,clear,toggle,lsb,msb,nth_bit;

        printf("enter number and position:\n");

        scanf("%d %d",&num,&pos);

        printf("set=%d\n",SET(num,pos));

        printf("clear=%d\n",CLEAR(num,pos));

        printf("toggle=%d\n",TOGGLE(num,pos));



}

