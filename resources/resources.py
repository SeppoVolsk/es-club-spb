from resources._colors import _Colors
from resources._links import _Links
from resources._messages import _Messages
from resources._strings import _Strings
from resources._values import _Values


class Resources():
    messages = _Messages()
    links = _Links()
    strings = _Strings()
    values = _Values()
    colors = _Colors()


R: Resources = Resources()
