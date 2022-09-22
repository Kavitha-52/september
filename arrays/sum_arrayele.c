#include<stdio.h>

int main()

{

	int arr[]={1,2,3,4,5,6},n,sum=0;

	n=sizeof(arr)/sizeof(arr[0]);

	for(int i=0;i<n;i++)

	{

		sum=sum+arr[i];

	}

	printf("sum of array elements are:%d\n",sum);

}

