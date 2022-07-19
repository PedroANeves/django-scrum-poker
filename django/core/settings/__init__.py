from .base import *

ENVIROMENT = os.environ.get("ENVIROMENT", "develop")

if ENVIROMENT=="develop":
    from .develop import *
elif ENVIROMENT=="ci":
    from .ci import *
elif ENVIROMENT=="qa":
    from .qa import *
elif ENVIROMENT=="staging":
    from .staging import *
elif ENVIROMENT=="production":
    from .production import *

try:
    from .local import *
except ImportError:
    pass
