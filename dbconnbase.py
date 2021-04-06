from abc import ABCMeta, abstractmethod


class DBConnBase(metaclass=ABCMeta):

# other non-abstract methods here ...

    @abstractmethod
    def connect(self):
        pass

    def close(self):
        self._close()

    @abstractmethod
    def get_cursor(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
