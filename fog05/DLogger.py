import logging
import time
import sys

class DLogger:
    class __SingletonLogger:
        def __init__(self, file_name=None, debug_flag=False):

            if file_name is None:
                self.log_file = 'fosagent_log.log' # str('fosagent_log_%d.log' % int(time.time()))
            else:
                self.log_file = file_name

            self.debug_flag = debug_flag

            log_format = '[%(asctime)s] - [%(levelname)s] > %(message)s'
            log_level = logging.INFO

            self.logger = logging.getLogger(__name__ + '.fog05.agent')

            self.logger.setLevel(log_level)
            formatter = logging.Formatter(log_format)
            if not debug_flag:
                log_filename = self.log_file
                handler = logging.FileHandler(log_filename)
            else:
                handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        def info(self, caller, message):
            self.logger.info('< {} > {}'.format(caller, message))

        def warning(self, caller, message):
            self.logger.warning('< {} > {}'.format(caller, message))

        def error(self, caller, message):
            self.logger.error('< {} > {}'.format(caller, message))

        def debug(self, caller, message):
            self.logger.debug('< {} > {}'.format(caller, message))

    instance = None
    enabled = True

    def __init__(self, file_name=None, debug_flag=False):

        if not DLogger.instance:
            DLogger.instance = DLogger.__SingletonLogger(file_name, debug_flag)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def info(self, caller, message):
        if self.enabled:
            self.instance.info(caller, message)

    def warning(self, caller, message):
        if self.enabled:
            self.instance.warning(caller, message)

    def error(self, caller, message):
        if self.enabled:
            self.instance.error(caller, message)

    def debug(self, caller, message):
        if self.enabled:
            self.instance.debug(caller, message)
