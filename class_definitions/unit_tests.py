import unittest

from class_definitions.student import Student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s("Stester", "Clas", "CIS", 3.5)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        student = s("Stester", "Clas", "CIS", 3.5)
        self.assertEqual(student.last_name, "Stester")
        self.assertEqual(student.first_name, "Clas")
        self.assertEqual(student.major, "CIS")
        self.assertEqual(student.gpa, 3.5)

    def test_object_created_all_attributes(self):
        self.assertEqual(self.student.last_name,"Stester")
        self.assertEqual(self.student.first_name, "Clas")
        self.assertEqual(self.student.major, "CIS")
        self.assertEqual(self.student.gpa, 3.5)


    def test_student_str(self):
        self.assertEqual(str(self.student), "Stester, Clas has major CIS with gpa: 3.5")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(Exception):
            student = s()
            student.set_first_name("Clas")
            student.set_major("CIS")
            student.set_gpa(3.5)

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(Exception):
            student = s()
            student.set_last_name("Stester")
            student.set_major("CIS")
            student.set_gpa(3.5)

    def test_object_not_created_error_major(self):
        with self.assertRaises(Exception):
            student = s()
            student.set_last_name("Stester")
            student.set_first_name("Clas")
            student.set_gpa(3.5)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(Exception):
            student = s()
            student.set_last_name("Stester")
            student.set_first_name("Clas")
            student.set_major("CIS")


if __name__ == '__main__':
    unittest.main()
