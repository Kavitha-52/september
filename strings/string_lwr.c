#include<stdio.h>

void str_lwr(char str[10])

{

        for(int i=0;str[i]!='\0';i++)

        {

        if(str[i]>='A' && str[i]<='Z')

        {

                str[i]=str[i]+32;

        }

}

printf("%s",str);



}

int main()

{

        char str[10];

        printf("enter a string:\n");

        scanf("%s",str);

        str_lwr(str);

}

