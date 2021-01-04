import logging


class BatchStatus:
    def __init__(self):
        self._started = False
        self._stopped = False
        self._killed = False
        self._defunct = False

    @property
    def started(self):
        return self._started

    @property
    def stopped(self):
        return self._stopped

    @property
    def killed(self):
        return self._killed

    @property
    def running(self):
        return self._started and not self._stopped

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        self.stop()

    def start(self):
        if self.started:
            raise RuntimeError('Context is already started ({}).'.format(__name__))

        self._started = True

    def stop(self):
        if not self.started:
            raise RuntimeError('Context cannot be stopped as it never started ({}).'.format(__name__))

        self._stopped = True

        if self._stopped:  # Stopping twice has no effect
            return

    def kill(self):
        if not self.started:
            raise RuntimeError('Cannot kill an unstarted context.')

        if self.stopped:
            raise RuntimeError('Cannot kill a stopped context.')

        self._killed = True

    # def error(self, exc_info, *, level=logging.ERROR):
    #     logging.getLogger(__name__).log(level, repr(self), exc_info=exc_info)
    #
    # def fatal(self, exc_info, *, level=logging.CRITICAL):
    #     logging.getLogger(__name__).log(level, repr(self), exc_info=exc_info)
    #     self._defunct = True
    #
    # def as_dict(self):
    #     return {
    #         'status': self.status,
    #         'name': self.name,
    #         'stats': self.get_statistics_as_string(),
    #         'flags': self.get_flags_as_string(),
    #     }


class BaseContext(BatchStatus):
    def __init__(self):
        BatchStatus.__init__(self)
