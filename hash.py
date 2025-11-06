import hashlib
import os


# # Example usage
# text = "Hello, World! \n"

# #creating SHA256 hash
# hash_object = hashlib.sha256(text.encode())
# #getting the hexadecimal representation
# hash_digest=hash_object.hexdigest()
# # Displaying the hash
# print("SHA HASH of  ", text, "is" , hash_digest)
# funtion for hashing full files

def hash_file(file_path): #funtion to specify the path as a parameter
    
    h = hashlib.new("sha256") # create a hash object using sha256 algo 
        
    with open(file_path, "rb") as file: # open file in binary mode and reference it as a file    
        while True:
            chunk = file.read(1024)
            if chunk == b"": # if chunk is empty, we have reached the end of the file
                break
            h.update(chunk) # updates hash object h with each chunk
    return h.hexdigest()

def verify_intergrity(file1, file2):# funtion to compare two files
    hash1 = hash_file(file1) # get hash of first file
    hash2= hash_file(file2) # get hash of second file
    print("checking intergrity between '", file1, "' and '", file2, "'") 
    if hash1 == hash2:
        print("Files are identical. No modification detected")
    else:
        print("Files are different. A modification has been detected")
    
if __name__ == "__main__":
    print("SHA Hash of file is: ", hash_file("../sample_files/sample.txt")) #prints the hash of the file located at sample_files/sample.txt
    print(verify_intergrity("../sample_files/download2.jpeg", "../sample_files/download2.jpeg"))