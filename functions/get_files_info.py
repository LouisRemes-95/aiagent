import os

def get_files_info(working_directory, directory=None):
    if not os.path.abspath(directory).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    try:
        return "\n".join([f"{content}: file_size={os.path.getsize(content)}, is_dir={os.path.isdir(content)}" for content in os.listdir(directory)])
    except Exception as e:
        print(f"Error: {e.__class__.__name__}: {e}")
