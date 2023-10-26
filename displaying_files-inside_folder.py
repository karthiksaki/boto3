import os

file_count = 0
folder_count = 0
subfolder_count = 0

for folderName, subfolders, filenames in os.walk(r'D:\Tesco\Real-Time_Devops\open_cloud-main\CI_CODE'):
    print('The current folder is ' + folderName)
    folder_count += 1

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        subfolder_count += 1

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        file_count += 1

print(f"Total number of folders: {folder_count}")
print(f"Total number of subfolders: {subfolder_count}")
print(f'Total number of files: {file_count}')
