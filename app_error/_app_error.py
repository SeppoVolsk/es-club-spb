from selenium.common import exceptions as e
import traceback


class _AppError:
    def message(self, error: Exception):
        match type(error):
            case e.NoSuchElementException:
                message = "Такой элемент не существует!"
            case e.ElementNotInteractableException:
                message = "Элемент представлен в DOM, но с ним невозможно взаимодействовать!"
            case e.TimeoutException:
                message = "Время истекло!"
            case _:
                message = f"Неизвестная ошибка! {error.__class__.__name__}"
        return message


E = _AppError()
