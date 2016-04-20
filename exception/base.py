#
# Copyright 2014 Oracle, Inc.
#


class APIException(Exception):
    """
    This represents an exception returned by a service in response to a
    bad status code.

    TODO: Rename or move

    TODO: inherit from something reasonable.
    """

    def __init__(self, message=None, errors=None, traceback=None, response=None, reference=None, location=None):
        print 'APIException __init__ is called'
        if not message:
            if hasattr(self, 'message'):
                message = self.message
            elif not errors:
                raise ValueError('Message is required')

        self.message = message
        self.errors = errors
        self.traceback = traceback
        self.response = response
        self.reference = reference
        self.location = location

    def _recursive_error(self, e):
        # if the exception detail is just a string, return the unicode version
        if isinstance(e, basestring):
            return unicode(e)

        # if the exception detail does not have an errors dictionary
        if not getattr(e, 'errors', None) or not isinstance(e.errors, dict):
            # return the message or None if it doesn't have a message attribute
            return unicode(getattr(e, 'message', None))

        # if the exception details has an errors dictionary, format it
        return dict((k, self._recursive_error(v)) for (k, v) in e.errors.items())

    def __str__(self):
        return str(self._recursive_error(self))
