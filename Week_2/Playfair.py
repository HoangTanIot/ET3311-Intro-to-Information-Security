def prepare_key(key):
    # Chuẩn bị khóa: loại bỏ các ký tự trùng lặp và 'J'
    key = key.upper().replace("J", "I")
    key_set = set()
    prepared_key = []
    for char in key:
        if char not in key_set and char.isalpha():
            key_set.add(char)
            prepared_key.append(char)
    # Thêm các ký tự còn lại của bảng chữ cái (trừ 'J')
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in key_set:
            prepared_key.append(char)
    return prepared_key

def create_matrix(key):
    # Tạo ma trận 5x5 từ khóa đã chuẩn bị
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(key[i:i+5])
    return matrix

def prepare_text(plaintext):
    # Chuẩn bị bản rõ: loại bỏ các ký tự không phải chữ cái và thêm 'X' nếu cần
    plaintext = plaintext.upper().replace("J", "I")
    prepared_text = []
    for char in plaintext:
        if char.isalpha():
            prepared_text.append(char)
    # Thêm 'X' nếu độ dài bản rõ lẻ
    if len(prepared_text) % 2 != 0:
        prepared_text.append('X')
    return prepared_text

def find_position(matrix, char):
    # Tìm vị trí của ký tự trong ma trận
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    # Chuẩn bị khóa và ma trận
    prepared_key = prepare_key(key)
    matrix = create_matrix(prepared_key)
    # Chuẩn bị bản rõ
    prepared_text = prepare_text(plaintext)
    ciphertext = []
    # Mã hóa từng cặp ký tự
    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        # Nếu cùng hàng
        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        # Nếu cùng cột
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        # Nếu tạo thành hình chữ nhật
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])
    return ''.join(ciphertext)

# Nhập liệu từ người dùng
plaintext = input("Nhập bản rõ: ")
key = input("Nhập khóa: ")

# Mã hóa và in kết quả
ciphertext = playfair_encrypt(plaintext, key)
print("Bản rõ:", plaintext)
print("Khóa:", key)
print("Bản mã:", ciphertext)