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

To try it out and