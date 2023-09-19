import hashlib

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    try:
        # Create a hash object based on the specified algorithm
        if hash_algorithm == "sha256":
            hash_obj = hashlib.sha256()
        elif hash_algorithm == "md5":
            hash_obj = hashlib.md5()
        else:
            print("Unsupported hash algorithm.")
            return None

        # Open the file in binary mode and read it in chunks
        with open(file_path, "rb") as file:
            while True:
                data = file.read(65536)  # Read in 64KB chunks
                if not data:
                    break
                hash_obj.update(data)

        # Calculate the hexadecimal representation of the hash
        file_hash = hash_obj.hexdigest()
        return file_hash

    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    hash_algorithm = input("Choose a hash algorithm (sha256/md5): ").lower()

    file_hash = calculate_file_hash(file_path, hash_algorithm)
    if file_hash:
        print(f"{hash_algorithm.upper()} hash of the file '{file_path}' is: {file_hash}")
