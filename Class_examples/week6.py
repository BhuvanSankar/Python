
class Student(object):
    def __init__(self, name, snum):
        """Constructor: Student(str, str)"""
        self._name = name
        self._snum = snum
        self._courses = []
        self._results = {}
        
    def get_name(self):
        return self._name

    def get_courses(self):
        return self._courses
    
    def add_courses(self, courses):
        self._courses.extend(courses)

    def add_results(self, results):
        self._results.update(results)
    
    def __str__(self):
        """ return the name of the student
        __str__() -> str
        """
        return self._name
    
    def __repr__(self):
        return "Student({0}, {1})".format(self._name, self._snum)
    
