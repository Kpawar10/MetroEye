import json
import os
import cv2

# Train
annotation_file = "C:\\Users\\kriti\\Downloads\\archive\\CrowdHuman\\dataset\\annotation_train.odgt"
image_folder = "C:\\Users\\kriti\\Downloads\\archive\\CrowdHuman\\dataset\\Images"
label_folder = "head_dataset/labels/train"

#val
annotation_file = "C:\\Users\\kriti\\Downloads\\archive\\CrowdHuman\\dataset\\annotation_val.odgt"
image_folder = "C:\\Users\\kriti\\Downloads\\archive\\CrowdHuman\\dataset\\Images_val"
label_folder = "head_dataset/labels/val"

os.makedirs(label_folder, exist_ok=True)

# Convert annotations
with open(annotation_file, "r") as f:
    for line in f:
        data = json.loads(line)

        image_name = data["ID"] + ".jpg"
        image_path = os.path.join(image_folder, image_name)

        img = cv2.imread(image_path)
        if img is None:
            continue

        h, w, _ = img.shape

        label_path = os.path.join(label_folder, data["ID"] + ".txt")

        with open(label_path, "w") as label_file:
            for gt in data["gtboxes"]:
                # Use "hbox" for head detection
                x, y, bw, bh = gt["hbox"]

                x_center = (x + bw/2) / w
                y_center = (y + bh/2) / h
                width = bw / w
                height = bh / h

                label_file.write(f"0 {x_center} {y_center} {width} {height}\n")