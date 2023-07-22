import os
import shutil

def organize_files_by_extension(dir_path):
    for filename in os.listdir(dir_path):
        # Get the full path of the file
        file_path = os.path.join(dir_path, filename)
        
        # Check if it's a regular file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            
            # Remove the dot from the extension
            extension = extension[1:]
            
            # Create a new directory path
            new_dir_path = os.path.join(dir_path, extension)
            
            # Create a new directory if it doesn't exist
            os.makedirs(new_dir_path, exist_ok=True)
            
            # Create a new file path in the new directory
            new_file_path = os.path.join(new_dir_path, filename)

            # If a file with the same name already exists in the new directory
            if os.path.exists(new_file_path):
                base_filename, extension = os.path.splitext(filename)
                i = 1

                # Modify the file name until it doesn't match any existing file
                while os.path.exists(new_file_path):
                    new_filename = f"{base_filename}_{i}{extension}"
                    new_file_path = os.path.join(new_dir_path, new_filename)
                    i += 1

            # Move the file
            shutil.move(file_path, new_file_path)


if __name__ == '__main__':
    # Use the function
    organize_files_by_extension('C:/Users/kundj/Downloads')
