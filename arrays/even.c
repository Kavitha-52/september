#include<stdio.h>

int even_element(int arr[],int n)

{

	int b[10],i,j=0;

	for(i=0;i<n;i++)

	{

		if(arr[i]%2==0)

		{

			b[j]=arr[i];

		//	j++;

		}

	}

	for(i=0;j<n;i++)

		printf("%d ",b[j]);

}

	

int main()

{

	int arr[]={1,2,3,4,5,6,7,8,9},n;

	n=sizeof(arr)/sizeof(arr[0]);

	even_element(arr,n);

}

