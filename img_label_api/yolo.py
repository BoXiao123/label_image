import os
import shutil
import cv2
import random
from voc import make_dir

def make_label(content,classes,new_label_path):
    out_file = open(new_label_path, 'w')
    for info in content:
        info=info.strip("\n").split(" ")
        label=info[0]
        if label not in classes:continue
        cls_id=classes.index(label)
        xmin=float(info[1])
        ymin=float(info[2])
        w=float(info[3])
        h=float(info[4])
        xcenter=xmin+0.5*w
        ycenter=ymin+0.5*h

        boundbox=(xcenter,ycenter,w,h)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in boundbox]) + '\n')
    out_file.close()

def make_yolo(args):
    classes = ["label_1","label_2","label_3"]
    jpeg_path=args.saved_dir+"/JPEGImages"
    label_path=args.saved_dir+"/labels"
    train_path=args.saved_dir+"/train.txt"
    valid_path=args.saved_dir+"/val.txt"
    make_dir([jpeg_path,label_path])
    all_file = os.listdir(args.detected_dir)
    all_file.sort()
    for each_file in all_file:
        filename = os.path.join(args.detected_dir, each_file)
        basename = each_file.split(".")[0]
        image_name = basename + ".jpg"
        old_image_path = os.path.join(args.image_path, image_name)
        new_image_path = os.path.join(jpeg_path, image_name)
        shutil.copyfile(old_image_path, new_image_path)
        img = cv2.imread(new_image_path)
        image_shape = img.shape
        new_label_path=os.path.join(label_path,each_file)
        file = open(filename, "r")
        content = file.readlines()
        make_label(content, classes, new_label_path)
        print valid_path
        nub = random.randint(0, 100)
        print nub
        train_percent = args.train_percent * 100
        if nub < train_percent:
            file = open(train_path, "a")
            file.write(new_image_path + "\n")

        else:
            file = open(valid_path, "a")
            file.write(new_image_path + "\n")
        file.close()
