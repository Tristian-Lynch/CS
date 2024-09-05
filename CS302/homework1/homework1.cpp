#include <iostream>

using namespace std;

int main(){
    int a[] = {4,3,1,7,8};
    int max = a[0];
    int n = sizeof(a)/sizeof(a[0]);
    

    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            cout << "i:" << i << " j:" << j << endl;
            if(a[j] > a[j+1]) {
                
            }
        }
    }

    return 0;
}