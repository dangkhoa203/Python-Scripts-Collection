def encrypt(message,key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) + key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(message,key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def user_input():
    key = int(input("Nhập khóa K: "))
    message = input("Nhập thông điệp (Họ tên và Mã số sinh viên): ")
    mode = input("Chọn phương thức (mã hóa 'e' hoặc giải mã 'd'): ")

    return key, message, mode

def main():
    key, message, mode = user_input()

    # Thực hiện mã hóa hoặc giải mã
    if mode.lower() == 'e':
        encrypted_message = encrypt(message, key)
        print("Thông điệp đã mã hóa:", encrypted_message)
    elif mode.lower() == 'd':
        decrypted_message = decrypt(message, key)
        print("Thông điệp đã giải mã:", decrypted_message)
    else:
        print("Phương thức không hợp lệ. Vui lòng chọn 'e' để mã hóa hoặc 'd' để giải mã.")


main()