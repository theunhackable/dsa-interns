#include <stdio.h>
int main()
{
    int n = 5;
    int e = 5;
    int a_a[5][5];
    int u[] = {0, 1, 2, 4, 2};
    int v[] = {1, 2, 4, 3, 3};
    int w[5][2];
    for (int i = 0; i < 5; i++)
    {
        w[i][0] = u[i];
        w[i][1] = v[i];
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            a_a[i][j] = 0;
        }
    }
    for (int i = 0; i < 5; i++)
    {
        int a = w[i][0], b = w[i][1];

        for (int j = 0; j < 5; j++)
        {
            if (j == a && i == b)
            {
                a_a[i][j] = 1;
                a_a[j][i] = 1;
            }
            else if (i == a && j == b)
            {
                a_a[i][j] = 1;
                a_a[j][i] = 1;
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%d ", a_a[i][j]);
        }
        printf("\n");
    }
}
