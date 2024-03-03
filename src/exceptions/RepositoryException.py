
class RepositoryException(Exception):
    """
    Exception for the Repository class.
    """
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg
