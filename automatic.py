import cv2 as cv
import os 
import shutil
from glob import glob

SOURCE_ROOT = 'images/archive/No_Apply_Grayscale/No_Apply_Grayscale/Vehicles_Detection.v8i.yolov8'
TARGET_ROOT = 'images/archive/Processed_Grayscale'

SPLITS = ['train', 'valid', 'test']

def convert_img_to_grayscele(source_images_dir, target_images_dir):
    os.makedirs(target_images_dir, exist_ok=True)
    image_paths = glob(os.path.join(source_images_dir, "*.jpg"))

    for img_path in image_paths:
        img = cv.imread(img_path)
        if img is None:
            print(f"[!!] Skipped : {img_path}")
            continue

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray_rgb = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  # Convert grayscale to RGB fake RGB

        file_name = os.path.basename(img_path)
        cv.imwrite(os.path.join(target_images_dir, file_name), gray_rgb)

def copy_labels(source_labels_dir, target_labels_dir):
        os.makedirs(target_labels_dir, exist_ok=True)
        for label_file in glob(os.path.join(source_labels_dir, "*.txt")):
            shutil.copy(label_file, target_labels_dir)
            

def process_all():
        for split in SPLITS:
            print(f"\n {split.upper()} SPLIT PROCESSING...")

            source_images = os.path.join(SOURCE_ROOT, split, "images")
            source_labels = os.path.join(SOURCE_ROOT, split, "labels")

            target_images = os.path.join(TARGET_ROOT, split, "images")
            target_labels = os.path.join(TARGET_ROOT, split, "labels")

            convert_img_to_grayscele(source_images, target_images)
            copy_labels(source_labels, target_labels)

            print(f"\n {split.upper()} SPLIT PROCESSING COMPLETED! Images : {len(glob(target_images + '/*.jpg'))})")



if __name__ == "__main__":
    process_all()
    print("\n\n[INFO] All splits processed successfully!")