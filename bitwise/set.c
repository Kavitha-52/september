#include<stdio.h>

int main()

{

	int num,pos,set,clear,toggle;

	printf("enter a  number and pos:\n");

	scanf("%d %d",&num,&pos);

	set=num|(0x1<<pos);

	clear=num^(~(0x1<<pos));

	toggle=num^(0x1<<pos);

	printf("set:%d\n clear:%d\n toggle:%d\n",set,clear,toggle);

}

