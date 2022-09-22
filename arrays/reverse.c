#include<stdio.h>

int reverse_array(int arr[],int n)

{

	int i,j,temp;

	for(i=0;i<n/2;i++)

	{

		temp=arr[i];

		arr[i]=arr[n-1-i];

		arr[n-1-i]=temp;

	}

}

int main()

{

	int arr[]={1,2,3,4,5,6,7},n;

	n=sizeof(arr)/sizeof(arr[0]);

	reverse_array(arr,n);



	printf("after reversing array elements are:\n");

	

	for(int i=0;i<n;i++)

	{

		printf("%d ",arr[i]);

	}

	return 0;

}
