from importlib import metadata
from .rsyncmirror import RsyncMirror

__version__ = metadata.version(__package__)
__all__ = ['__version__', 'RsyncMirror']

del metadata
