# ============================================= Task 7 - Image Resizer Tool ==================================

import os
from PIL import Image

def resize_images():


    input_folder = input("Enter the path to the input folder: ").strip()
    output_folder = input("Enter the path to the output folder: ").strip()
    width = int(input("Enter new width (px): "))
    height = int(input("Enter new height (px): "))
    format_choice = input("Enter output format (jpg/png/webp, leave blank to keep original): ").strip().lower()


    os.makedirs(output_folder, exist_ok=True)


    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)


        try:
            with Image.open(file_path) as img:
                
                resized_img = img.resize((width, height))


                if format_choice:
                    save_name = os.path.splitext(filename)[0] + f".{format_choice}"
                    save_path = os.path.join(output_folder, save_name)
                    resized_img.save(save_path, format_choice.upper())
                else:
                    save_path = os.path.join(output_folder, filename)
                    resized_img.save(save_path)

                print(f"✅ Resized and saved: {save_path}")

        except Exception as e:
            print(f"⚠️ Skipped {filename}: {e}")

    print("\n🎯 All images processed successfully!")

if __name__ == "__main__":
    resize_images()
