from PIL import Image
import os
from reformatFolder import *

def cleanUp(JPGfolder, folder_to_format):
    for outer_item in os.listdir(JPGfolder):
        outer_item_path = os.path.join(JPGfolder, outer_item)
        if os.path.isdir(outer_item_path):
            print(f"\nRemoving files from: {outer_item_path}")
            for inner_item in os.listdir(outer_item_path):
                item_path = os.path.join(outer_item_path, inner_item)
                if isEligibile(item_path):
                    os.remove(item_path)
            print(f"Removing dir: {outer_item_path}\n")
            os.rmdir(outer_item_path)

    for outer_item in os.listdir(folder_to_format):
        os.remove(os.path.join(folder_to_format, outer_item))

def convert_jpgs_to_pdf(folder_path, output_pdf_path):
    

    for outer_item in os.listdir(folder_path):
        outer_item_path = os.path.join(folder_path, outer_item) 
        outputPdfFolder = os.path.join(output_pdf_path, outer_item)
        
        if os.path.isdir(outer_item_path):
            jpg_files = [f for f in os.listdir(outer_item_path) if isEligibile(f)]
            jpg_files.sort()

            if not jpg_files:
                print(outer_item_path)
                print("No .jpg files found in the specified folder.\n")
                continue

            if not os.path.exists(outputPdfFolder):
                os.makedirs(os.path.dirname(outputPdfFolder), exist_ok=True)

            image_list = []
            for jpg_file in jpg_files:
                if jpg_file.startswith("avatar92"):
                    continue
                image_path = os.path.join(outer_item_path, jpg_file)
                image = Image.open(image_path)
                image = image.convert('RGB')  # Convert to RGB to ensure compatibility with PDF
                image_list.append(image)

            # Save images as a single PDF
            pdfPath = os.path.join(outputPdfFolder + ".pdf")
            image_list[0].save(pdfPath, format='PDF', save_all=True, append_images=image_list[1:])
            print(f"\nPDF saved successfully as '{outputPdfFolder}\n")

format_folder_path = "E:\data\FolderToFormat"
formatted_folder_path = "E:\data\FormattedFolder"

remove_non_jpg_files(format_folder_path, formatted_folder_path)
output_pdf_path = "E:\data\pdfs"

convert_jpgs_to_pdf(formatted_folder_path, output_pdf_path)
cleanUp(formatted_folder_path, format_folder_path)


