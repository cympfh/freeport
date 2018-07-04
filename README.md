# freeport - Python3 Library

Scan and pick a free port

## usage

```python
from freeport import freeport

port = freeport()  # pick a free port from 8000
port = freeport(8080, 10000)  # from 8080-10000

if port is not None:
    srv = YourServer()
    srv.listen(port=port)
else:
    print('No free port')
```

## install

```bash
pip install git+https://github.com/cympfh/py-freeport
```

or clone and `./setup.py`.
