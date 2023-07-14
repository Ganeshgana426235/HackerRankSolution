//c language code 

#include<stdio.h>
int main()
{
    int n,i,j,d1=0,d2=0,res;
    scanf("%d",&n);
    int a[n][n],k=n-1;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(i==j)
                d1+=a[i][j];
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(j==k){
                d2+=a[i][j];
                k-=1;
            }
    
    res=d1-d2;
    if(res <0)
        res= res*-1;
    printf("%d",res);
    return 0;
}