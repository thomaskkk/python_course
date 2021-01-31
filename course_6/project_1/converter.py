#!/usr/bin/python3

from PIL import Image
import os

#src_img = "/home/thomas/python_course/course_6/project_1/images/ic_add_location_black_48dp"
#dest_img = "/home/thomas/python_course/course_6/project_1/test_img/ic_add_location_black_48dp"
img_format = "JPEG"
img_rotate = 90
img_width = 128
img_height = 128

def converter(src_dir, dest_dir):
    """Convert image of all images from source dir and saves on destination dir"""
    for (root, dirs, files) in os.walk(src_dir):
        for name in files:
            convert_img_size(os.path.join(root, name), dest_dir + name)
            convert_img_orientation(dest_dir + name, dest_dir + name)


def convert_img_size(src_img, dest_img):
    """Convert images to the desired width, height and format"""
    try:
        im = Image.open(src_img)
        im.resize((img_width, img_height)).convert('RGB').save(dest_img, img_format)
    except:
        print("Not a valid source image: " + src_img)

def convert_img_orientation(src_img, dest_img):
    """Rotate images and save with the desired format"""
    try:
        im = Image.open(src_img)
        im.rotate(img_rotate).convert('RGB').save(dest_img, img_format)
    except:
        print("Not a valid source image: " + src_img)

if __name__ == '__main__':
    src_dir = "/home/thomas/python_course/course_6/project_1/images/"
    dest_dir = "/home/thomas/python_course/course_6/project_1/opt/icons/"
    converter(src_dir, dest_dir)