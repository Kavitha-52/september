#include<stdio.h>

int main()

{

        int arr[]={1,2,3,4,5,4,3,5,2},n,i;

        n=sizeof(arr)/sizeof(arr[0]);

        printf("duplicate elements are:");

        for(i=0;i<n;i++)

        {

                for(int j=i+1;j<n;j++)

                {

                    if(arr[i]==arr[j])

		    {

			    for(int k=j;k<n;k++)

			    {

				    arr[k]=arr[k+1];

			    }

			    j--;

			    n--;

		    }

                }



        }

	for(i=0;i<n;i++)

	{

		printf("%d ",arr[i]);

	}

}
