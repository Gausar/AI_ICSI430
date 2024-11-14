// #include<stdio.h>

// int main(){
//     int a[5];
//     int s = 0;
//     for(int i = 0; i < 5; i++){
//         scanf("%d", &a[i]);
//     }
//     for(int i = 0; i < 5; i++){
//         s = s + a[i];
//     }
//     int dundaj = s / 5;
//     printf("Dundaj onoo : %d", dundaj);
//     return 0;
// }
#include <stdio.h>

void osohoor_erembleh(int arr[], int n) {
    int i, j, t;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] > arr[j]) {
                t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
        }
    }
}
int main() {
    int numbers[10];
    
    printf("10n too oruulna uu: \n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &numbers[i]);
    }
    
    osohoor_erembleh(numbers, 10);
    
    printf("Osohoor eremblegdsen toonuud : \n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
    }
    return 0;
}
