import logging

LOG_FORMAT = "%(asctime)s [%(levelname)s]: %(message)s"
DATE_FORMAT = "%d.%m.%Y, %H:%M:%S"

logger = logging.getLogger(__name__)

def main():
    logger.info("Setting up bot")
    # отключение логгеров библиотек, чтобы не засорять консоль
    logging.getLogger("requests").setLevel(logging.ERROR)
    logging.getLogger("aiogram").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logger.info("Done. Running bot.")

if __name__ == "__main__":
    # настройка логгера
    logging.basicConfig(
        level=logging.DEBUG,
        format= LOG_FORMAT,
        datefmt= DATE_FORMAT
    )
    log_name = "work.log"
    fh = logging.FileHandler(log_name)
    fmt = logging.Formatter(LOG_FORMAT)
    fmt.datefmt = DATE_FORMAT
    fh.setLevel(logging.WARNING)
    logging.getLogger().addHandler(fh)
    logging.basicConfig(
        handlers=[
            fh
        ]
    )

    main()