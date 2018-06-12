#!/usr/bin/env python
# -*- coding: utf8 -*-


import argparse
from voc import make_voc
from yolo import make_yolo
from coco import make_coco

if __name__=="__main__":

    parser=argparse.ArgumentParser()
    parser.add_argument("--detected_dir",type=str,help="the directory of detection results",default="/home/b_xi/Detection")
    parser.add_argument("--image_path",type=str,help="the directory of original images",default="/home/b_xi/car8")
    parser.add_argument("--saved_dir",type=str,help="the directory you want to save the converted result",default="/home/b_xi/VOC2007")
    parser.add_argument("--train_percent",type=float,default=0.9)
    parser.add_argument("--convert_to",type=str,default='coco',help="the format you want to save to")
    args = parser.parse_args()

    if args.convert_to == "voc":
        make_voc(args)
    if args.convert_to=="yolo":
        make_yolo(args)
    if args.convert_to=="coco":
        make_coco(args)



