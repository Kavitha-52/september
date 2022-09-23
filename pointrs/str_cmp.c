#include<stdio.h>

int  mystrcmp(char *s1,char *s2);

int main()

{

        int res;

 char s1[10] ,s2[10];

 printf("enter the string name:\n");

 scanf("%s %s",s1,s2);

 res=mystrcmp(s1,s2);

 if(res==0)

         printf("strings are equal");

 else if(res>0)

         printf("string 1 greater");

 else

         printf("string2 greater");

}

int  mystrcmp(char *s1,char *s2)

{

       while(*s1 !='\0'&& *s2 !='\0')

        {

                 if(*s1>*s2)

                return *s1-*s2;

		 else if(*s1<*s2)

                 return *s1-*s2;

                s1++;

                s2++;

        }



       return *s1-*s2;

}

