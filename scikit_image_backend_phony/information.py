from skimage.util._backends import BackendInformation


def info():
    implemented_functions = ["skimage.metrics.simple_metrics.mean_squared_error"]
    backend_info = BackendInformation(implemented_functions)
    return backend_info
