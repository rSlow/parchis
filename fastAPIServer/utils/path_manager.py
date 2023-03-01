from pathlib import Path


def get_router_prefix(path: str):
    """
    @param path: name of file (__file__)
    @return: APIRouter prefix in "/prefix" format
    """
    return "/" + Path(path).stem
