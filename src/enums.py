
# Simulate an ENUM in python < 3.4
class META_E_RUN(type):
    # possible scenarios
    SUCCESS = 0
    FOLDER_NOT_FOUND = -1
    EMPTY_FOLDER = -2
    RUNNING_ERROR = -3

    desc = {}
    desc[SUCCESS] = 'Success'
    desc[FOLDER_NOT_FOUND] = 'Folder not found'
    desc[EMPTY_FOLDER] = 'Folder is empty'
    desc[RUNNING_ERROR] = 'Error while running program'

    def __len__(self):
        return len(self.desc)
    
    def __getitem__(self, pos):
        return self.desc[pos]
    
    def __iter__(self):
        return iter(self.desc)
    
    def describe(self, value):
        return self.desc[value]

# http://stackoverflow.com/questions/6187932/how-to-write-a-static-python-getitem-method
class E_RUN (object):
    __metaclass__ = META_E_RUN
    pass
