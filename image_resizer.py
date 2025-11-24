import os
from PIL import Image

def resize_images(input_folder, output_folder, width, height, convert_format=None):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Process only images
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp")):
            try:
                img = Image.open(file_path)

                # Resize image
                resized_img = img.resize((width, height))

                # If converting format (jpg/png/webp)
                if convert_format:
                    new_filename = os.path.splitext(filename)[0] + "." + convert_format
                else:
                    new_filename = filename

                save_path = os.path.join(output_folder, new_filename)

                resized_img.save(save_path)
                print(f"Saved: {save_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    print("=== Batch Image Resizer Tool ===")

    input_folder = input("Enter input folder path: ")
    output_folder = input("Enter output folder path: ")
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))

    convert_choice = input("Convert format? (jpg/png/webp/bmp) or press Enter to skip: ")
    convert_format = convert_choice.strip().lower() if convert_choice else None

    resize_images(input_folder, output_folder, width, height, convert_format)

    print("\n✔ Task completed!")


