#include<stdio.h>

int main()

{

	int arr[]={1,2,3,4,5,4,3,5,2},n,i;

	n=sizeof(arr)/sizeof(arr[0]);

	int res=arr[0];

	for(i=1;i<n;i++)

	{

		res=res ^ arr[i];

	}

	printf("uniqe element in array is :%d\n",res);

}
