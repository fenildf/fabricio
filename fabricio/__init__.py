from fabricio.tasks import infrastructure, skip_unknown_host
from fabricio.operations import local, log, move_file, remove_file, run

VERSION = (0, 4, 6)

__version__ = '.'.join(map(str, VERSION))
