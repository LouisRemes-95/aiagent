import os

def get_files_info(working_directory, directory=None):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        return "\n".join([
                f"{content}: file_size={os.path.getsize(os.path.join(full_path, content))}, is_dir={os.path.isdir(os.path.join(full_path, content))}"
                for content in os.listdir(full_path)
            ])
        
    except Exception as e:
        return f"Error: {e.__class__.__name__}: {e}"
