class Student:
    """student class"""

    def __init__(self, lname, fname, major, gpa):
        if lname is None:
            raise Exception
        else:
            self.last_name = lname
        if fname is None:
            raise Exception
        else:
            self.first_name = fname
        if major is None:
            raise Exception
        else:
            self.major = major
        if isinstance(gpa, float) and 0.0 < gpa <= 4.0:
            self.gpa = gpa
        else:
            raise Exception

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

    def set_last_name(self, lname):
        if lname is None:
            raise Exception
        else:
            self.last_name = lname

    def set_first_name(self, fname):
        if fname is None:
            raise Exception
        else:
            self.first_name = fname

    def set_major(self, major):
        if major is None:
            raise Exception
        else:
            self.major = major

    def set_gpa(self, gpa):
        if isinstance(gpa, float) and 0.0 < gpa <= 4.0:
            self.gpa = gpa
        else:
            raise Exception

