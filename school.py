class School():
    def __init__(self, name=None, new_roster={}):
        self._name = name
        self._roster = new_roster

    @property
    def roster(self):
        return self._roster

    @roster.setter
    def add_roster (self, roster):
        # self.roster_validation(roster)
        self.roster.append(roster)

    def add_student(self, name, grade):
        if grade in self.roster:
            self.roster[grade].append(name)
        else:
            self.roster[grade] = [name]
        return self.roster

    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        SG = {}
        for key, value in self.roster.items():
            SG[key] = sorted(value)
        return SG

    # def get_grade(self, grade):
    #     return

    # def roster_validation(self, roster):
    #     if not isinstance(roster, dict):
    #         raise('roster is invalid')
        #Need to get key/value int/list check to work properly

        # if not isinstance(roster.items(), (int,list)):
        #     raise('roster key must be integer')
        # if not isinstance(roster.value, list):
            # raise('roster value must be list')


#grade input and name input check each
