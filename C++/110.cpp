#include <iostream>
using namespace std;
int main(){
    string a;
    cin >> a;
    int number = a.count("4") + a.count("7");
    if (a == 4 || a == 7){
        cout << "YES";
    }
    else{
        cout << "NO";
    }
    return 0;
}
