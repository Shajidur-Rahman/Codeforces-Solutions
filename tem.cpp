#include <iostream>

int main()
{
    using namespace std;
    int y;

    cout << "Enter any year: ";
    cin >> y, "\n";

    int y_len=y.length();

    if (y_len == 4)
    {
        if (y % 4 == 0)
        {
            cout << "This is a leap year";
        }
        else if (y % 100 == 0 && y % 400 == 0)
        {
            cout << "This is a leap year";
        }
        else if (y % 400 == 0)
        {
            cout << "This is a leap year";
        }
        else
        {
            cout << "This is not a leap year";
        }
    }
    else
    {
        cout << "Enter a valid int";
    }
}