#include <iostream>
using namespace std;

int main() {
    int n, a, k, s, p;
    long long pr;

    // 1а - сколько нечетных
    cout << "задача 1а" << endl;
    cout << "n = ";
    cin >> n;
    k = 0;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a % 2 != 0) {
            k = k + 1;
        }
    }
    cout << "нечетных: " << k << endl;

    // 1б - кратных 3 и не кратных 5
    cout << "задача 1б" << endl;
    cout << "n = ";
    cin >> n;
    k = 0;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a % 3 == 0 && a % 5 != 0) {
            k = k + 1;
        }
    }
    cout << "количество: " << k << endl;

    // 3а - сумма кратных 5 (50 чисел)
    cout << "задача 3а" << endl;
    s = 0;
    for (int i = 0; i < 50; i++) {
        cin >> a;
        if (a % 5 == 0) {
            s = s + a;
        }
    }
    cout << "сумма: " << s << endl;

    // 3б - сумма нечетных и отрицательных (50 чисел)
    cout << "задача 3б" << endl;
    s = 0;
    for (int i = 0; i < 50; i++) {
        cin >> a;
        if (a % 2 != 0 && a < 0) {
            s = s + a;
        }
    }
    cout << "сумма: " << s << endl;

    // 4 - количество и сумма тех что делятся на 5 и не делятся на 7
    cout << "задача 4" << endl;
    cout << "n = ";
    cin >> n;
    k = 0;
    s = 0;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a % 5 == 0 && a % 7 != 0) {
            k = k + 1;
            s = s + a;
        }
    }
    cout << "количество: " << k << endl;
    cout << "сумма: " << s << endl;

    // 5 - произведение тех что кратны p
    cout << "задача 5" << endl;
    cout << "n = ";
    cin >> n;
    cout << "p = ";
    cin >> p;
    pr = 1;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a % p == 0) {
            pr = pr * a;
        }
    }
    cout << "произведение: " << pr << endl;

    return 0;
}
