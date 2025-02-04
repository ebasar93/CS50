x = input("File name:").lower().strip()

if ".gif" in x:
    print("image/gif")
elif ".jpg" in x:
    print("image/jpeg")
elif ".jpeg" in x:
    print("image/jpeg")
elif".png" in x:
    print("image/png")
elif ".pdf" in x:
    print("application/pdf")
elif ".txt" in x:
    print("plain/txt")
elif ".zip" in x:
    print("application/zip")
else:
    print("application/octet-stream")

