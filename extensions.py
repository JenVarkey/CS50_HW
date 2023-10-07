file = input("File name: ").lower().strip()
if file[file.__len__() - 3:] == "gif":
    print("image/gif")
elif file[file.__len__() - 3:] == "jpg" or file[file.__len__() - 4:] == "jpeg":
    print("image/jpeg")
elif file[file.__len__() - 3:] == "png":
    print("image/png")
elif file[file.__len__() - 3:] == "pdf":
    print("application/pdf")
elif file[file.__len__() - 3:] == "zip":
    print("application/zip")
elif file[file.__len__() - 3:] == "txt":
    print("text/plain")
else:
    print("application/octet-stream")