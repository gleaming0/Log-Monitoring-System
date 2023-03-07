import os
from django.core.files.storage import FileSystemStorage

#path = "/backup/rsync"
path = "/home/master/projects/mysite/static/rsync"
file_list = os.listdir(path)
tar = [file for file in file_list if file.endswith(".tar.gz")]
sql = [file for file in file_list if file.endswith(".sql")]
file_list = tar + sql
file_list.sort(reverse=True)
# file_list_tar = [file for file in file_list if file.endswith(".log")]
context = {'file_list': file_list}

print(path)
print(tar)
print(sql)
print(file_list)

try:
    fs =FileSystemStorage('/backup/rsync')
    with fs.open('jeonjucom_20230223135401.tar.gz') as tar:
        print("yes")
except Exception as ex:
    print("no")
    print("msg:", ex)
