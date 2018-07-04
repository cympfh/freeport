import socket


__all__ = ['freeport']


def freeport(sub=8000, sup=65535, host='127.0.0.1'):
    """
    >>> p = freeport()
    >>> type(p)
    <class 'int'>
    >>> p >= 8000
    True
    """
    for port in range(sub, sup + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result != 0:
            return port
        sock.close()
