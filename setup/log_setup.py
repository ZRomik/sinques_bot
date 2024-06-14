import logging
from .config_reader import read_param

LOG_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s"
DATE_FORMAT = "%d.%m.%Y, %H:%M:%S"

# настройка системы логирования
logging.basicConfig(
    level=logging.DEBUG,
    format=LOG_FORMAT,
    datefmt=DATE_FORMAT
)
log_name = read_param("LOGNAME")
if not log_name:
    log_name = "work.log"
fh = logging.FileHandler(log_name)
fh.encoding = "utf-8"
fh.mode = "w"
fmt = logging.Formatter(LOG_FORMAT)
fmt.datefmt = DATE_FORMAT
fh.setFormatter(fmt)
fh.setLevel(logging.WARNING)
logging.getLogger().addHandler(fh)
logging.basicConfig(
    handlers=[
        fh,
    ]
)
