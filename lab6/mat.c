#include<stdio.h>

int main(){
    int a[10][10], b[10][10], c[10][10];
    int n, m, k, t, s;
    scanf("%d", &n);
    scanf("%d", &m);
    scanf("%d", &k);
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &a[i][j]);
        }
    }
    for(int i = 0; i < k; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &b[i][j]);
        }
    }
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            c[i][j] = 0;
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            for(int p = 0; p < m; p++){
                c[i][j] += a[i][p] * b[p][j];
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < k; j++){
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}