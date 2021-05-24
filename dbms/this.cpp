#include <iostream>  
using namespace std;  
int main()  
{  
 int N;

cin >> N;

int average =0;

int arr[N];

for(int i=0;i<N;i++){
    cin >> arr[i];
}
cout << "First 5 numbers divide on 3 without remainder:";
for(int i=0;i<N;i++){
    if(arr[i] % 3 == 0){
        cout << " " <<arr[i] ;
    }
}
