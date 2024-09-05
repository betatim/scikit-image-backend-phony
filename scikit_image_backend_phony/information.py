from skimage.util._backends import BackendInformation


def info():
    implemented_functions = ["metrics.simple_metrics.mean_squared_error"]
    backend_info = BackendInformation(implemented_functions)
    return backend_info
