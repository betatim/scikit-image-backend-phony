# scikit-image-backend-phony

This repository contains an example scikit-image backend. The goal of this
backend is to provide a basic implementation that can be used to test the
dispatching mechanism and serve as documentation of how the dispatching
mehanism in scikit-image works.

This backend only implements one function,
`skimage.metrics.mean_squared_error`. This keeps things straightforward
when reading the code.

> This repository should be moved to the scikit-image GitHub org at some
> point.


## Installing

To install this backend checkout the repository and run
```
pip install -e.
```


## Using it

After installing the backend it will automatically be used for the function
that the backend implements:

```python
import numpy as np
from skimage.metrics import mean_squared_error

mean_squared_error(np.asarray([0.,0.5]), np.asarray([0., 0.9]))
```

If the backend was used a warning will be emitted telling you so:
```
DispatchNotification: Call to 'skimage.metrics.simple_metrics.mean_squared_error' was dispatched to the 'phony' backend. Set SKIMAGE_NO_DISPATCHING=1 to disable this.
```