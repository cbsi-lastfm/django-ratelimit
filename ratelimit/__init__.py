VERSION = (0, 6, 0, 'WEB-22032')
__version__ = '.'.join(map(str, VERSION))

ALL = (None,)  # Sentinel value for all HTTP methods.
UNSAFE = ['DELETE', 'PATCH', 'POST', 'PUT']
