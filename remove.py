import os

# 遍历所有子文件夹，统计每个子文件夹中的照片数量
photo_counts = {}
for dirpath, dirnames, filenames in os.walk("training"):
    photo_counts[dirpath] = len(filenames)

# 删除照片数量大于等于 100 的子文件夹
for dirpath, photo_count in photo_counts.items():
    if photo_count >= 30:
        print("Deleting folder:", dirpath)
        for filename in os.listdir(dirpath):
            file_path = os.path.join(dirpath, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(e)
        os.rmdir(dirpath)