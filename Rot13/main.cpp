/*
*   Nama  : Muhammad Aziz Rosyid Hidayat
*   NIM   : 12320068
*   Kelas : C
*/

#include <iostream>
using namespace std;

int main() {
    string plainText = "Aku adalah seorang programmer pemula! Saat ini saya sedang belajar c++.";
    string encodedText;
    char alphabet;
    int asciiValue;
    for (int i = 0; i < plainText.length(); i++) {
        if (isalpha(plainText[i])) {
            asciiValue = int(tolower(plainText[i])) + 13;
            asciiValue = asciiValue > 122 ? asciiValue - 26 : asciiValue;
            alphabet = asciiValue;
        } else {
            alphabet = plainText[i];
        }
        if (isupper(plainText[i])) {
            alphabet = toupper(alphabet);
        }
        encodedText += alphabet;
    }
    cout << encodedText;

    return 0;
}
