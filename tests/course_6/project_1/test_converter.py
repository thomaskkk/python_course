from course_6.project_1.converter import convert_img_size, convert_img_orientation

from PIL import Image
import os

src_img = "/home/thomas/python_course/course_6/project_1/images/ic_add_location_black_48dp"
dest_img = "/home/thomas/python_course/course_6/project_1/test_img/ic_add_location_black_48dp"

def test_img_size():
    convert_img_size(src_img, dest_img)
    
    #open image to check size
    im = Image.open(dest_img)
    width, height = im.size
    assert width == 128 and height == 128
    
    #delete file after assertion
    if os.path.exists(dest_img):
        os.remove(dest_img)


def test_img_format():
    convert_img_orientation(src_img, dest_img)
    
    #open image to check format
    im = Image.open(dest_img)
    img_format = im.format
    assert img_format == "JPEG"

    #delete file after assertion
    if os.path.exists(dest_img):
        os.remove(dest_img)

#def test_not_img():
#    pass