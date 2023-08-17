import logging

from resources.resources import R

_format_template = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

class ColorFormatter(logging.Formatter):

    FORMATS = {
        logging.DEBUG: R.colors.GREY + _format_template + R.colors.RESET,
        logging.INFO: R.colors.CYAN + _format_template + R.colors.RESET,
        logging.WARNING: R.colors.YELLOW + _format_template + R.colors.RESET,
        logging.ERROR: R.colors.ORANGE_BG + _format_template + R.colors.RESET,
        logging.CRITICAL: R.colors.BOLD_RED + _format_template + R.colors.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


l = logging.getLogger()
l.setLevel(R.values.LOGGING_LEVEL)
"""
File Handler
"""
file_handler = logging.FileHandler(__name__)
file_handler.setFormatter(logging.Formatter(_format_template))
file_handler.setLevel(R.values.LOGGING_LEVEL)
l.addHandler(file_handler)
"""
Console Handler
"""
console_color_handler = logging.StreamHandler()
console_color_handler.setFormatter(ColorFormatter())
console_color_handler.setLevel(R.values.LOGGING_LEVEL)
l.addHandler(console_color_handler)

