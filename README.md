# label_image_tool
This is a tool for labeling images.
The img_label_boxed.exe is for Windows7, no library installation requirements.
This tool can be used for making classification, tracking, and detection Datasets.
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/1.png)

## Classification
After type the username and password, click Classification button
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/2.png)
Click Open Dir Button to select a image
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/3.png)
Choose a checkbox,and click classify button. You can also go to any frame with the GO button on the upright corner.

The classied images will be copied to corresponding folders.
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/4.png)

## Tracking
Click Tracking Button, and draw bounding box by mouse, the coordinates of bounding box will be shown in the bottom.
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/5.png)
Click track button, then go to next image. The results will be saved in the results.txt
		The format is : image_name x/width y/height w/width h/height
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/6.png)

## Detection
Click Detection Button, draw bouding box of one object, then choose a checkbox and click detect object button. After drawn all objects in this frame, click detect image button and go to next image.
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/7.png)
The results will be saved in Detection/image_name.txt. 
		The format is : label x/width y/height w/width h/height
![](https://github.com/BoXiao123/label_image_tool/raw/master/images/8.png)
