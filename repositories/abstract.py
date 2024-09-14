import abc


class BaseRepository(abc.ABC):
    """
    Base repository class.
    """
    @abc.abstractmethod
    def get_by_id(self, entity_id: str):
        pass
