#include<stdio.h>
#include<math.h>
 
int main(){
    int n;
    double x,y,pf,pi;
    scanf("%d",&n);
    while(n--){
        scanf("%lf",&x);
        y = (-1 + pow((1 + 8*x),0.5))/2;
        pf = modf(y,&pi);
        printf("%.0lf\n",pi);
    }
    return 0;
}
