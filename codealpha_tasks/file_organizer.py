import os
import shutil
TARGET_FOLDER="C:/Users/lenovo/Downloads"

# file type mapping

FILE_TYPES={
    "Documents":[".pdf",".docs",".txt"],
    "Images":[".jpg",".jpeg",".png",".gif"],
    "videos":[".mp4",".mkv",".avi"],
    "music":[".mp3",".wav"],
    "Archives":[".zip",".rar"],
    "Scripts":[".py",".js",".html",".css"],
    "Spreadsheets":[".xls",".xlsx",".csv"]
}

def organize_folder():
    for file in os.listdir(TARGET_FOLDER):
        file_path=os.path.join(TARGET_FOLDER,file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved=False

            for folder,extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    folder_path=os.path.join(TARGET_FOLDER,folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path,os.path.join(folder_path, file))
                    print(f"moved '{file}' to '{folder}'")
                    moved= True
                    break
                if not moved:
                    other_path= os.path.join(TARGET_FOLDER,"others")
                    os.makedirs(other_path,exist_ok= True)
                    shutil.move(file_path,os.path.join(other_path, file))
                    print(f"moved '{file}' to 'others'")

# run the script
if __name__=="__main__":
  print("organizing your folder...")
  organize_folder()
  print("done")


