#include <stdio.h>
#include <stdlib.h>
int main()
{
    int nodes = 5;
    int edges = 5;
    int adj_matrix[5][5];
    int u[] = {0, 1, 2, 4, 2};
    int v[] = {1, 2, 4, 3, 3};

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            adj_matrix[i][j] = 0;
        }
    }

    for (int i = 0; i < 5; i++)
    {
        adj_matrix[u[i]][v[i]] = 1;
        adj_matrix[v[i]][u[i]] = 1;
    }

    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            printf("%d ", adj_matrix[i][j]);
        }
        printf("\n");
    }
}
