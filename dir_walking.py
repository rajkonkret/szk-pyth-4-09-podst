import os

for root, dirs, files in os.walk("../szk-pyth-4-09-pods"):
    for file in files:
        abs_root = os.path.abspath(root)
        print(abs_root)
        if dirs:
            print("Directories:")
            for dir_ in dirs:
                print(dir_)
            print()
        if files:
            print("Files:")
            for filename in files:
                print(filename)
            print()

total_size = 0
for dirpath, _, filenames in os.walk("../szk-pyth-4-09-pods"):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if not os.path.islink(fp):
            total_size += os.path.getsize(fp)

print(total_size)  # 265800758 -> 265806957
print(total_size/1024/1024)  # 253.52456188201904
# 11:30
