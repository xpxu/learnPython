



class TaskMetadataProperty(object):
    def __init__(self, property_name):
        self.property_name = property_name

class Task(object):
    status_detail = TaskMetadataProperty('status_detail')

t = Task
s = t.status_detail
print s.property_name
del s.property_name
s.property_name = 'YES'
print s.property_name

