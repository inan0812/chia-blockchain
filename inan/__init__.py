from pkg_resources import DistributionNotFound, get_distribution, resource_filename

try:
    __version__ = get_distribution("inan-blockchain").version
except DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

PYINSTALLER_SPEC_PATH = resource_filename("inan", "pyinstaller.spec")