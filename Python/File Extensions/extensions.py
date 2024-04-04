file_name = input("Enter your file name: ").lstrip()

index = file_name.index(".")

file_suffix = file_name[index:]

match file_suffix:
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")