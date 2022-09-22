#include<stdio.h>

int main()

{

        int arr[]={12,34,4,123,87,99},i,n;

        n=sizeof(arr)/sizeof(arr[0]);

        int large=arr[0],sl=0;
        for(i=1;i<n;i++)
        {
                if(arr[i]>large)
                {
                        sl=large;
                        large=arr[i];
                }
                else if(arr[i]>sl)
                        sl=arr[i];
        }
        printf("largest element:%d\n second large element:%d\n",large,sl);

}

