import toml
from collections.abc import Mapping
from pathlib import Path
from types import MethodType

def get_git_submodules():
    # TODO: get git submodule info
    return [ 'hardcoded-dep1' ]

def install_requires_setter(self, values):
    deps = get_git_submodules() + values
    print(f"Install dependencies: {deps}")
    setattr(self,'install_requires', deps)

def finalize_dist(dist):
    # We can set install_requires of dist here, but it's replaced with
    # dependencies from pyproject.toml by setuptools.  Unless we bind this
    # attribute 'set_install_requires' to a function.  And the function needs
    # to be bound to dist object, otherwise it can't update the dist object.
    setattr(dist.metadata,'set_install_requires', MethodType(install_requires_setter, dist))
