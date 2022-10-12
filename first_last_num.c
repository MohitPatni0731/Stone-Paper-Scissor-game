#include <stdio.h>

int main()
{
    int num, sum=0, f_digit, l_digit;
    printf("Enter the number = ");
    scanf("%d", &num);
    
    l_digit = num % 10;
    
    while(num >= 10)
    {
        num = num / 10;
    }
    f_digit = num;
    printf("\n First digit = %d and Last digit = %d\n\n", f_digit, l_digit);
    
    return 0;
}
