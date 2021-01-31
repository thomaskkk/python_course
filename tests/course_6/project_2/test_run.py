from course_6.project_2.run import txt_to_dictionary


def test_txt_to_dictionary():
    dir = "/home/thomas/python_course/course_6/project_2/"
    file = "sample_007.txt"
    dictionary = []
    dictionary = txt_to_dictionary(dir, file)
    expected = [
        {"title": "Good deal for a 2015 RAV4"},
        {"name": "Anonymous"},
        {"date": "2018-04-17"},
        {"feedback": "Called them to locok for a: second-hand!"}
    ]
    assert dictionary == expected
