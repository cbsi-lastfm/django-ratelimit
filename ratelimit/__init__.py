VERSION = (0, 6, 0)
__version__ = '.'.join(map(str, VERSION)) + '+WEB-22032'

ALL = (None,)  # Sentinel value for all HTTP methods.
UNSAFE = ['DELETE', 'PATCH', 'POST', 'PUT']
