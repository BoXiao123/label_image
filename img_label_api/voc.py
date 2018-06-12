import cv2
import shutil
import random
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import os

def make_voc(args):
    paths=[args.saved_dir+"/JPEGImages",args.saved_dir+"/Annotations",args.saved_dir+"/ImageSets",args.saved_dir+"/ImageSets/Main"]
    make_dir(paths)
    all_file=os.listdir(args.detected_dir)
    all_file.sort()
    for each_file in all_file:
        filename=os.path.join(args.detected_dir,each_file)
        basename=each_file.split(".")[0]
        nub=random.randint(0,100)
        train_percent=args.train_percent*100
        train_path = paths[3] + "/train.txt"
        val_path = paths[3] + "/val.txt"
        if nub<train_percent:
            file=open(train_path,"a")
            file.write(basename+"\n")
            file.close()
        else:
            file=open(val_path,"a")
            file.write(basename+"\n")
            file.close()
        image_name=basename+".jpg"
        old_image_path=os.path.join(args.image_path,image_name)
        new_image_path=os.path.join(paths[0],image_name)
        shutil.copyfile(old_image_path,new_image_path)
        img=cv2.imread(new_image_path)
        image_shape=img.shape
        xml_name=paths[1]+"/"+basename+".xml"
        file=open(filename,"r")
        content=file.readlines()
        make_xml(image_name, image_shape, xml_name, content)


def make_xml(img_name,img_shape,xml_name,content):
    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'VOC2007'
    node_filename = SubElement(node_root, 'filename')
    node_filename.text = img_name
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = str(img_shape[1])
    node_height = SubElement(node_size, 'height')
    node_height.text = str(img_shape[0])
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = str(img_shape[2])

    for info in content:
        info=info.strip("\n").split(" ")
        label=info[0]
        xmin=float(info[1])*img_shape[1]
        xmin=str(int(xmin))
        ymin=float(info[2])*img_shape[0]
        ymin=str(int(ymin))
        xmax=float(info[3])*img_shape[1]
        xmax=str(int(xmax)+int(xmin))
        ymax=float(info[4])*img_shape[0]
        ymax=str(int(ymax)+int(ymin))

        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = label
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = xmin
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = ymin
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = xmax
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = ymax

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    f = open(xml_name, 'w')
    dom.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
    f.close()


def make_dir(paths):
    for each_path in paths:
        if not os.path.exists(each_path):
            os.mkdir(each_path)



