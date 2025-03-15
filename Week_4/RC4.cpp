#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

// Hàm mã hóa RC4
void rc4_encrypt(const string& plaintext, const string& key, 
                vector<unsigned char>& keystream, 
                vector<unsigned char>& ciphertext) {
    // Khởi tạo mảng S
    unsigned char S[256];
    for (int i = 0; i < 256; i++) {
        S[i] = i;
    }
    
    // KSA (Key Scheduling Algorithm)
    int j = 0;
    for (int i = 0; i < 256; i++) {
        j = (j + S[i] + key[i % key.length()]) % 256;
        swap(S[i], S[j]);
    }
    
    // PRGA (Pseudo-Random Generation Algorithm)
    int i = 0;
    j = 0;
    for (char c : plaintext) {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        swap(S[i], S[j]);
        unsigned char k = S[(S[i] + S[j]) % 256];
        keystream.push_back(k);
        ciphertext.push_back(c ^ k); // XOR để mã hóa
    }
}

int main() {
    // Định nghĩa khóa và bản rõ
    string key = "MySecretKey";  // Khóa mật tự định nghĩa
    string plaintext = "Hanoi University of Science and Technology";
    
    cout << "Ban ro: " << plaintext << endl;
    
    // Vector để lưu dòng khóa và bản mã
    vector<unsigned char> keystream;
    vector<unsigned char> ciphertext;
    
    // Thực hiện mã hóa
    rc4_encrypt(plaintext, key, keystream, ciphertext);
    
    // In dòng khóa
    cout << "\nDong khoa (keystream) - dang thap phan:\n";
    for (unsigned char k : keystream) {
        cout << (int)k << " ";
    }
    cout << endl;
    
    // In bản mã dạng thập phân
    cout << "\nBan ma (ciphertext) - dang thap phan:\n";
    for (unsigned char c : ciphertext) {
        cout << (int)c << " ";
    }
    cout << endl;
    
    // In bản mã dạng hex
    cout << "\nBan ma (ciphertext) - dang hex:\n";
    for (unsigned char c : ciphertext) {
        cout << hex << setw(2) << setfill('0') << (int)c << " ";
    }
    cout << dec << endl; // Quay lại định dạng thập phân
    
    return 0;
}