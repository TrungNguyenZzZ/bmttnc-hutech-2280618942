import hashlib
def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()
input_string = input("Nhập chuỗi cần băm:")
md5_hash = calculate_md5(input_string)
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
import hashlib
def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256() 
    sha256_hash.update(data.encode('utf-8'))  
    return sha256_hash.hexdigest()  
if __name__ == "__main__":
    data_to_hash = input("Nhập dữ liệu cần băm SHA-256: ")
    hash_value = calculate_sha256_hash(data_to_hash)
    print("Giá trị băm SHA-256:", hash_value)