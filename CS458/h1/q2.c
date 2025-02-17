#include <stdio.h>

// function to swap two integers in an array
void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

// function for printing arrays.
void printArray(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        printf("%d%s", arr[i], (i == n - 1) ? "\n" : " ");
    }
}

int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n], oddArr[n], evenArr[n];
    int oddCount = 0, evenCount = 0;
    
    // scan in all the numbers you want to use.
    printf("Enter %d numbers:\n", n);
    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        if(arr[i] % 2 != 0) {
            oddArr[oddCount++] = arr[i];
        } else {
            evenArr[evenCount++] = arr[i];
        }
    }

    // find all permutations of the odd part
    // find all permutations of the even part
    // combine each odd permutation with each even

    printf("All permutations (odds first, then evens):\n");

    // Temporary arrays to avoid changing the originals:
    int i;
    int tempOdds[oddCount], tempEvens[evenCount];
    for(i = 0; i < oddCount; i++) {
        tempOdds[i] = oddArr[i];
    }
    for(i = 0; i < evenCount; i++) {
        tempEvens[i] = evenArr[i];
    }

    // Permute odd array
    void permuteOdds(int l, int r) {
        if(l == r) {
            // For each odd permutation, we permute the even array
            void permuteEvens(int el, int er) {
                if(el == er) {
                    // Print combined result: odd portion then even portion
                    // first, print odd portion
                    for(int od = 0; od < oddCount; od++) {
                        printf("%d ", tempOdds[od]);
                    }
                    // then print even portion
                    for(int ev = 0; ev < evenCount; ev++) {
                        printf("%d%s", tempEvens[ev], (ev == evenCount - 1) ? "\n" : " ");
                    }
                    return;
                }
                for(int k = el; k <= er; k++) {
                    swap(&tempEvens[el], &tempEvens[k]);
                    permuteEvens(el + 1, er);
                    swap(&tempEvens[el], &tempEvens[k]); // backtrack
                }
            }
            // permute the even array for each odd
            // reset the even array for each pass
            for(int idx = 0; idx < evenCount; idx++) {
                tempEvens[idx] = evenArr[idx];
            }
            permuteEvens(0, evenCount - 1);
            return;
        }
        for(int m = l; m <= r; m++) {
            swap(&tempOdds[l], &tempOdds[m]);
            permuteOdds(l + 1, r);
            swap(&tempOdds[l], &tempOdds[m]);
        }
    }

    permuteOdds(0, oddCount - 1);

    return 0;
}
