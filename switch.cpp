#include <iostream>
#include <clocale>
using namespace std;

int main() {
    setlocale(LC_ALL, "Russian");

    // задание 1 - калькулятор
    cout << "задание 1 (калькулятор)" << endl;
    double a, b;
    char op;
    cout << "введите два числа: ";
    cin >> a >> b;
    cout << "введите знак (+ - * / %): ";
    cin >> op;

    switch (op) {
    case '+':
        cout << a << " + " << b << " = " << a + b << endl;
        break;
    case '-':
        cout << a << " - " << b << " = " << a - b << endl;
        break;
    case '*':
        cout << a << " * " << b << " = " << a * b << endl;
        break;
    case '/':
        if (b == 0) {
            cout << "ошибка: на ноль делить нельзя" << endl;
        } else {
            cout << a << " / " << b << " = " << a / b << endl;
        }
        break;
    case '%':
        if ((int)b == 0) {
            cout << "ошибка: на ноль делить нельзя" << endl;
        } else {
            cout << (int)a << " % " << (int)b << " = " << (int)a % (int)b << endl;
        }
        break;
    default:
        cout << "ошибка: такого знака нет" << endl;
    }

    // задание 2 - день недели
    cout << endl << "задание 2 (день недели)" << endl;
    int day;
    cout << "введите число от 1 до 7: ";
    cin >> day;

    switch (day) {
    case 1: cout << "Понедельник" << endl; break;
    case 2: cout << "Вторник" << endl; break;
    case 3: cout << "Среда" << endl; break;
    case 4: cout << "Четверг" << endl; break;
    case 5: cout << "Пятница" << endl; break;
    case 6: cout << "Суббота" << endl; break;
    case 7: cout << "Воскресенье" << endl; break;
    default:
        cout << "ошибка: число должно быть от 1 до 7" << endl;
    }

    // задание 3 - свое задание
    // Текст задания: ввести номер месяца (от 1 до 12) и вывести
    // к какому времени года он относится. Если номер неправильный,
    // вывести сообщение об ошибке.
    cout << endl << "задание 3 (время года)" << endl;
    int month;
    cout << "введите номер месяца: ";
    cin >> month;

    switch (month) {
    case 12:
    case 1:
    case 2:
        cout << "Зима" << endl;
        break;
    case 3:
    case 4:
    case 5:
        cout << "Весна" << endl;
        break;
    case 6:
    case 7:
    case 8:
        cout << "Лето" << endl;
        break;
    case 9:
    case 10:
    case 11:
        cout << "Осень" << endl;
        break;
    default:
        cout << "ошибка: месяцев всего 12" << endl;
    }

    return 0;
}
