from loguru import logger


def Alert_Error(message: str):
    return logger.error(f"\n{message}\n")


def Alert_Warning(message: str):
    return logger.warning(f"\n{message}\n")


def Alert_Info(message: str):
    return logger.info(f"\n{message}\n")


def Alert_Debug(message: str):
    return logger.debug(f"\n{message}\n")


def Alert_Success(message: str):
    return logger.success(f"\n{message}\n")


def Alert_Critical(message: str):
    return logger.critical(f"\n{message}\n")


def Alert_Exception(message: str):
    try:
        raise Exception(message)
    except Exception:
        logger.exception("Exceção capturada:")



