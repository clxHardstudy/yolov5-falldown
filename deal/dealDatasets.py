import os
import random
import shutil


"""
    copy图片与对应的labels
"""
# 定义源文件夹和目标文件夹路径
source_images_dir = '/Users/clx/Projects/datasets/FddOrigin/train/images'
source_labels_dir = '/Users/clx/Projects/datasets/FddOrigin/train/labels'
target_images_dir = '/Users/clx/Projects/datasets/datasets/train/images'
target_labels_dir = '/Users/clx/Projects/datasets/datasets/train/labels'

# 创建目标文件夹
os.makedirs(target_images_dir, exist_ok=True)
os.makedirs(target_labels_dir, exist_ok=True)

# 获取源文件夹下所有图片的文件名列表
image_files = os.listdir(source_images_dir)

# 计算选择图片的数量
num_images_to_copy = int(len(image_files) * 0.5)

# 从图片文件列表中随机选择50%的图片
selected_image_files = random.sample(image_files, 5000)

# 将选中的图片复制到目标文件夹中
for image_file in selected_image_files:
    image_path = os.path.join(source_images_dir, image_file)
    shutil.copy(image_path, target_images_dir)

    # 复制对应的标签文件
    label_file = image_file.replace('.png', '.txt')
    label_path = os.path.join(source_labels_dir, label_file)
    shutil.copy(label_path, target_labels_dir)


"""
    labels文件修改
"""
# import os
#
# # 定义目标文件夹路径
# target_labels_dir = '/Users/clx/Projects/datasets/FddOrigin/valid/labels'
#
# # 获取目标文件夹下所有以 'rgb_' 开头的 txt 文件
# target_files = [file for file in os.listdir(target_labels_dir) if file.startswith('rgb_')]
#
# # 遍历目标文件，修改文件内容
# for file_name in target_files:
#     file_path = os.path.join(target_labels_dir, file_name)
#     with open(file_path, 'r+') as file:
#         # 读取文件内容
#         content = file.read()
#
#         # 修改第一个字符
#         if content[0] == '0':
#             new_content = '1' + content[1:]
#         elif content[0] == '1':
#             new_content = '0' + content[1:]
#
#         # 将修改后的内容写入文件
#         file.seek(0)
#         file.write(new_content)
#         file.truncate()


# import os
#
# # 定义目标文件夹路径
# target_labels_dir = '/Users/clx/Projects/datasets/datasets/train/labels'
#
# # 获取目标文件夹下所有以 'rgb_' 开头的 txt 文件
# target_files = [file for file in os.listdir(target_labels_dir) if file.startswith('rgb_')]
#
# # 遍历目标文件，删除文件
# for file_name in target_files:
#     file_path = os.path.join(target_labels_dir, file_name)
#     os.remove(file_path)

