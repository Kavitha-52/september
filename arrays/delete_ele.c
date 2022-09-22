#include<stdio.h>
int main()
{
        int arr[]={1,2,3,4,5,6},n,i,pos;
        n=sizeof(arr)/sizeof(arr[0]);
        printf("enter position:\n");
        scanf("%d",&pos);
        if(pos >=n+1)
                printf("deletion not possible:\n");
        else
        {
                for(i=pos-1;i<n;i++)
                {
                        arr[i]=arr[i+1];
                        //n--;
                }
                printf("resultant array is :");
                for(i=0;i<n-1;i++)
                {
                        printf("%d ",arr[i]);

                }
        }
}
