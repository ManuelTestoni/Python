#include <stdio.h>

#define MAX 100

int matrix1[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

int matrix2[3][3] = {
    {9, 8, 7},
    {6, 5, 4},
    {3, 2, 1}
};

int result[3][3] = {
    {0, 0, 0},
    {0, 0, 0},
    {0, 0, 0}
};

int r1,c1,r2,c2=3;


int** multiplyMatrices() {
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            result[i][j] = 0;
            for (int k = 0; k < c1; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }
    return result;
}
