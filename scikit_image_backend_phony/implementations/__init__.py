import importlib


def get_implementation(name):
    """Get this backends implementation of the function

    The name passed to this function will be the full name of the function that
    is being dispatched. It will include modules and sub-modules.

    The returned function should have the same signature as the function that
    is being dispatched, raise the same exceptions, etc.

    If the backend does not contain an implementation then this function should
    return `None`.
    """
    module_name, func_name = name.rsplit(".", maxsplit=1)

    try:
        mod = importlib.import_module(
            "scikit_image_backend_phony.implementations." + module_name
        )
    except ModuleNotFoundError as e:
        return None

    func = getattr(mod, func_name, None)

    return func


def can_has(name, *args, **kwargs):
    """Evaluate if the backend wants to take a call or not.

    Given the name of the function and the arguments with which it was called
    in the frontend, decide if this backend has a suitable implementation.

    If the deicison is negative, it should come fast.

    Can be as simple as checking the types of the arguments, or as complex
    as inspecting the types and shapes of the array arguments as well as
    the additional arguments.
    """
    return True
