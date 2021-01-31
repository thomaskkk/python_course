from course_6.project_1.convert import convert_img_size, convert_img_format

import PIL, os

src_img = "/home/thomas/python_course/course_6/project_1/images/ic_add_location_black_48dp"
dest_img = "/home/thomas/python_course/course_6/project_1/test_img/ic_add_location_black_48dp"

def test_img_size():
    convert_img_size(src_img, dest_img)
    im = Image.open(dest_img)
    width, height = im.size
    assert width == "128" and height == "128"

def test_img_format():
    convert_img_format(src_img, dest_img)
    im = Image.open(dest_img)
    img_format = im.format
    assert img_format == "jpeg"

#def test_img_orientation():
#    pass