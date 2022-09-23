#include<stdio.h>

void mystrcat(char * d,char *s);

int main()

{

 char d[20] ,s[20];

 printf("enter the string name:\n");

 scanf("%s %s",s,d);

 mystrcat(d,s);

}

void mystrcat(char *d,char *s)

{

        char *str=d;

       while(*d != '\0')

        {

                d++;

        }

        while(*s !='\0')

        {

                *d=*s;

                s++;

                d++;

        }

        *d='\0';

        printf("%s",str);

}

