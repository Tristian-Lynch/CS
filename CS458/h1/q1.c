#include <stdio.h>

// We will store the paths in a 2D array
// the maximum number of steps is 1000, this can be changed
// based on how much memory is available.
int path[1000][2];

void printPath(int length) {
    for(int i = 0; i < length; i++) {
        // Print the path we stored
        printf("(%d,%d)", path[i][0], path[i][1]);
        if(i < length - 1) {
            // If it's not the last point, print an arrow
            printf(" -> ");
        } else {
            // If it's the last point, print a newline we can start a new path
            printf("\n");
        }
    }
}

void findPaths(int x, int y, int n, int k, int step) {
    path[step][0] = x;
    path[step][1] = y;

    // If we reached the destination
    if(x == n && y == k) {
        printPath(step + 1);
        return;
    }

    // Diagonal up
    if(x+1 <= n && y+1 < n) {
        findPaths(x+1, y+1, n, k, step+1);
    }
    // Diagonal down
    if(x+1 <= n && y-1 >= 0) {
        findPaths(x+1, y-1, n, k, step+1);
    }
}

int main() {
    int n, k;
    // Read n and k
    printf("Enter n (size of grid... n*n): ");
    scanf("%d", &n);
    printf("Enter k (point n,k... where we are going): ");
    scanf("%d", &k);
    // Find paths
    findPaths(0, 0, n, k, 0);
    return 0;
}