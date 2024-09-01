import importlib

def get(name):
    module_name, func_name = name.rsplit(".", maxsplit=1)
    mod = importlib.import_module(
        "scikit_image_backend_phony.implementations." + module_name
    )
    func = getattr(mod, func_name, None)
    can_has = getattr(mod, f"can_has_{func_name}", None)

    return can_has, func