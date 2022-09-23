#include<stdio.h>

int mystrlen(char * str);

int main()

{

        char name[20];

        int count;

        printf("enter name:");

         scanf(" %s",name);

        count= mystrlen(name);

         printf("strlen=%d\n",count);

        return 0;

}

int mystrlen(char *str)

{

        int count=0;

       while(*str!='\0')

        {

                str++;



                count++;

        }

                return count;

}

