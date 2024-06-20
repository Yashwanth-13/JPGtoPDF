import os
import shutil

def isEligibile(f):
    if (f.lower().endswith('.jpg')):
        return True
    elif( f.lower().endswith('.jpeg')):
        return True
    
    return False



def remove_non_jpg_files(folder_path,  formattedFolderPath):

    print("\n\n\t\t\tDELETING EVERYTHING EXCEPT .jpg FILES")

    if not os.path.isdir(folder_path):
        print(f"The provided path '{folder_path}' is not a valid directory.")
        return
    

    # Iterate over all items in the folder
    for outer_item in os.listdir(folder_path):
        outer_item_path = os.path.join(folder_path, outer_item)
        if os.path.isdir(outer_item_path):
            chapterName = split(outer_item)
            # Iterate over all items in the subfolder
            print(f"\nRemoving files from: {outer_item_path}")
            for inner_item in os.listdir(outer_item_path):
                item_path = os.path.join(outer_item_path, inner_item)
                
                # Check if the item is a file and does not end with .jpg
                
                if os.path.isfile(item_path) and not isEligibile(item_path):
                    os.remove(item_path)
            print("Done")
                
            chapterPath = os.path.join(formattedFolderPath, chapterName)
            if not os.path.exists(chapterPath):
                os.makedirs(os.path.dirname(chapterPath), exist_ok=True)
            print(f"Moving {outer_item_path} to {chapterPath}")
            shutil.move(outer_item_path, chapterPath)
        

    print("Cleanup complete. Only .jpg files remain in the folder and everything has been moved.\n\n")


def split(folderPath):
    chapterName = "Chapter"
    nextOne = False

    store = folderPath.split(" ")
    for i in store:
        if i == "Chapter":
            nextOne = True
            continue
        if nextOne:
            chapterName += " " + i
            break

    return chapterName
