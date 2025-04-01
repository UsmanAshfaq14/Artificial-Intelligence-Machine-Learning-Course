# try:
#     # Open (or create) a file 'example.txt' in write mode
#     file = open("exam.txt", "w", encoding="utf-8")
#     file.write("Hello, Python File Handling with Error Handling!\n")
#     file.write("This file demonstrates try-except for file operations.\n")
# except IOError as e:
#     # Catch any I/O errors during file writing
#     print("An error occurred while writing to the file:", e)
# else:
#     print("File written successfully!")
# finally:
#     # Ensure the file is closed if it was opened
#     try:
#         file.close()
#     except NameError:
#         # 'file' variable might not be defined if open() failed
#         pass

# Reading from a file with error handling using a context manager
try:
    # Using 'with' ensures the file is closed automatically after reading
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()  # Read the entire file content
        print("File Content:\n", content)
except FileNotFoundError as fnf_error:
    # Handle the case where the file doesn't exist
    print("Error: File not found:", fnf_error)
except IOError as e:
    # Handle other I/O errors during file reading
    print("An error occurred while reading the file:", e)
