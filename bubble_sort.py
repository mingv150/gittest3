def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排好序，无需再比较
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 1. 生成密钥对（公钥+私钥）
key = RSA.generate(2048)  # 2048 位密钥长度
private_key = key.export_key()  # 导出私钥
public_key = key.publickey().export_key()  # 导出公钥

# 2. 用公钥加密
def encrypt(message, pub_key):
    rsa_key = RSA.import_key(pub_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.encrypt(message.encode())

# 3. 用私钥解密
def decrypt(ciphertext, priv_key):
    rsa_key = RSA.import_key(priv_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    return cipher.decrypt(ciphertext).decode()




# 测试冒泡排序函数
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = bubble_sort(test_array)
    print("排序后的数组master c1:", sorted_array)
    # 测试流程
    msg = "Hello, Asymmetric Encryption!"
    encrypted = encrypt(msg, public_key)
    decrypted = decrypt(encrypted, private_key)

    print("明文:", msg)
    print("加密后:", encrypted.hex())  # 转十六进制方便查看
    print("解密后:", decrypted)