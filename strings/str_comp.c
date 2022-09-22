#include<stdio.h>

int  string_cmp(char d[],char s[]);

int main()

{

        char s1[10],s2[10];

        printf("enter the two string:\n");

        scanf("%s %s",s1,s2);

       int i= string_cmp(s1,s2);

       if(i==0)

	       printf("two strings are equal\n");

       else if(i>0)

	       printf("string 1 is greater\n");

       else

	       printf("string 2 is greater\n");



        return 0;

}

int string_cmp(char s1[],char s2[])

{

        int i=0,j=0;

        while(s1[i]!='\0'&&s2[j]!='\0')

        {

		if(s1[i]>s2[i])

			return s1[i]-s2[j];

		else if(s1[i]<s2[j])

			return s1[i]-s2[j];

		else

			return s1[i]-s2[j];

		i++;

		j++;

	}

  

        }







