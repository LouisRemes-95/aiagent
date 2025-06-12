import os

def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(full_path, "r") as f:
            content = f.read(10000)
            if f.read(1) != "":
                content += f'...File "{file_path}" truncated at 10000 characters'
            return content
        
    except Exception as e:
        print(f"Error: {e.__class__.__name__}: {e}")