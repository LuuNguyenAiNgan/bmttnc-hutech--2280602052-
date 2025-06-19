class PlayfairCipher:
    def __init__(self):
        pass
    def create_playfair_matrix(self, key):
        # Chuyển "J" thành "I" trong khóa
        key = key.replace("J", "I")
        key_upper = key.upper()
        # Tạo tập hợp các ký tự duy nhất trong khóa
        key_set = set(key_upper)
        # Bảng chữ cái tiếng Anh, bỏ qua 'J'
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # Tìm các ký tự còn lại không có trong khóa
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        
        # Khởi tạo ma trận Playfair
        matrix = list(key_upper)
        for letter in remaining_letters:
            matrix.append(letter)
            # Dừng khi ma trận đủ 25 ký tự (5x5)
            if len(matrix) == 25:
                break
        
        # Chuyển đổi danh sách thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        # Tìm tọa độ (hàng, cột) của một ký tự trong ma trận
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""

        # Xử lý văn bản từng cặp ký tự
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            
            # Xử lý nếu số lượng ký tự lẻ hoặc hai ký tự giống nhau
            if len(pair) == 1: # Xử lý nếu số lượng ký tự lẻ
                pair += "X"
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2: # Cùng hàng
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: # Cùng cột
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else: # Tạo hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2: # Cùng hàng
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2: # Cùng cột
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else: # Tạo hình chữ nhật
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự 'X' nếu nó là ký tự cuối cùng và là ký tự được thêm vào
        banro = ""
        for i in range(0, len(decrypted_text), 2):
            if i + 2 <= len(decrypted_text) and decrypted_text[i+1] == "X" and decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + decrypted_text[i+1]
        
        if banro[-1] == "X":
            banro = banro[:-1]
        
        return banro