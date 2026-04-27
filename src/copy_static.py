import shutil
import os

# “Walk the tree → recreate folders → copy leaves”
def copy_static_to_public(src_dir, dest_dir):
    # 1. Ensure a clean destination by deleting it if it exists
    if os.path.exists(dest_dir):
        print(f"Cleaning Public Directory: {dest_dir}")
        shutil.rmtree(dest_dir)
    
    # 2. Create the destination directory
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Created clean Public Directory: {dest_dir}")

    # 3. Recursive copy function
    def copy_recursive(src, dest):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)

            if os.path.isdir(src_path):
                # Recursively handle subdirectories
                os.makedirs(dest_path, exist_ok=True)
                copy_recursive(src_path, dest_path)
            
            else:
                # Copy file and log progress
                shutil.copy(src_path, dest_path)
                print(f"Copied {src_path} --> {dest_path}")

    # Start the process
    copy_recursive(src_dir, dest_dir)

# get paths for static dir and public dir
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# base_dir = os.path.dirname(os.path.abspath(__file__))
# static_dir = os.path.join(base_dir, "static")
# public_dir = os.path.join(base_dir, "public")
# print("STATIC:", static_dir)
# print("PUBLIC:", public_dir)

# run the function
# copy_static_to_public(static_dir, public_dir)