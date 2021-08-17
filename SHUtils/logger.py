class Logger(object):
    from typing import TextIO, AnyStr

    log: TextIO
    terminal: TextIO

    def __init__(self, stream: TextIO, file_name: str = 'PyProject.log'):
        self.log = open(file_name, 'a')
        self.terminal = stream

    def __del__(self):
        self.log.close()

    def write(self, message: AnyStr):
        self.log.write(message)
        self.terminal.write(message)

    def flush(self):
        pass


def set_logger_stream(file_name: str = 'PyProject.log'):
    import sys

    sys.stdout = Logger(stream=sys.stdout, file_name=file_name)
    sys.stderr = Logger(stream=sys.stderr, file_name=file_name)


if '__main__' == __name__:
    set_logger_stream('nuancer.log')
    print('🎃🎃🎃' + '報可開生即通管子麼朋小白下命北，期個道知人有看基經了這的成十經數。')
    raise ValueError('9527')
