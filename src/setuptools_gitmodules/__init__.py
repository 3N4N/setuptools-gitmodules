import toml
from collections.abc import Mapping
from pathlib import Path
from types import MethodType

def get_git_submodules():
    # TODO: get git submodule info
    return [ 'hardcoded-dep1' ]

def install_requires_setter(self, values):
    pp = toml.load('pyproject.toml')
    deps = pp.get('project')['dependencies']
    deps += get_git_submodules()
    print(f"Install dependencies: {deps}")
    setattr(self,'install_requires', deps)

def finalize_dist(dist):
    # 'deps' replaced with that from pyproject.toml by setuptools
    # Unless we bind this attribute 'set_install_requires' to a function
    # And the function needs to be bound to dist object, otherwise it can't
    # update the dist object.  I don't know if this is the best way.  But it works.
    setattr(dist.metadata,'set_install_requires', MethodType(install_requires_setter, dist))
