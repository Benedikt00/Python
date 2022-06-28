import os

folderRel = "18.6.2022" # ohne / am ende


folderRel.replace("\\", "/")

if folderRel[:-1] != "/":
    folderRel = folderRel + "/"

listPicNames = []

folder = r"C:\Users\bsimb\Documents\Programmieren_Privat\GitHub\Feuerwehr_2.0\pages\aktuelles\18.6.2022"

folder.replace("\\", "/")
print(folder)

for count, filename in enumerate(os.listdir(folder)):
    dst = f"Bild {str(count + 100)}.jpg"
    src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst = f"{folder}/{dst}"

for count, filename in enumerate(os.listdir(folder)):
    dst = f"Bild {str(count + 1)}.jpg"
    listPicNames.append(dst)
    src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    dst = f"{folder}/{dst}"
    # rename() function will
    # rename all the files
    os.rename(src, dst)

#<img src="images/slide-1.jpg" alt="img" /><img src="images/slide-2.jpg" alt="img" /><img src="images/slide-3.jpg" alt="img" />

for name in listPicNames:
    s = f"<img src=\"{folderRel}{name}\" class=\"bild\" alt=\"img\" />"
    print(s)