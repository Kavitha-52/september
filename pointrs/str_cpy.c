#include<stdio.h>

void mystrcpy(char *d,char *s);

int main()

{

 char d[20] ,s[10];

 printf("enter the string names:\n");

 scanf("%s %s",s,d);

 mystrcpy(d,s);

}

void mystrcpy(char * d,char *s)

{

        char *str=d;

        while(*s !='\0')

        {

                *d=*s;

                s++;

               d++;

        }

        *d='\0';

                printf("strcpy=%s",str);

}

