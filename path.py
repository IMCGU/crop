import glob
import os
import argparse


# a=(glob.glob("outputs/./*"))
# print(a)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input-dir', type=str, help='Directory with unaligned images.')
    parser.add_argument('--output-dir', type=str, help='Directory with aligned face thumbnails.')
    args = parser.parse_args()
def get_filepaths(directory):#取得某資料夾下的所有路徑
    
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(args.input_dir)
print(full_file_paths)



with open('testpath.txt', 'w') as f:#把路徑寫成txt檔
    for item in full_file_paths:
        f.write("%s\n" % item)

   





 
 
 
 

 