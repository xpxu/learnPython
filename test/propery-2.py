



class TaskMetadataProperty(property):
    def __init__(self, property_name):
        def get(self):
            return self.property_name

        def set(self, value):
            self.property_name = 'OK'
            # return kv.task_metadata.update(self.request.id, task_meta)

        def delete(self):
            del self.property_name

        super(TaskMetadataProperty, self).__init__(get, set, delete)
        self.property_name = property_name

class Task(object):
    status_detail = TaskMetadataProperty('status_detail')

t = Task()
t.property_name = 'Jame'
s = t.status_detail
print type(s)
print s.property_name
# del s.property_name
s.property_name = 'YES'
print s.property_name

