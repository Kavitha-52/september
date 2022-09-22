#include<stdio.h>
int main()
{
	int arr[]={12,34,4,123,87,99},i,n;
	n=sizeof(arr)/sizeof(arr[0]);
	int small=arr[0],ss=0;
	for(i=1;i<n;i++)
	{
		if(arr[i]<small)
		{
			ss=small;
			small=arr[i];
		}
		else if(arr[i]<ss)
			ss=arr[i];
	}
	printf("smallest element:%d\n second small element:%d\n",small,ss);
}
