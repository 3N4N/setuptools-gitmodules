import toml
from collections.abc import Mapping
from pathlib import Path

def install_requires_setter(values):
    pass

def get_git_submodules():
    # TODO: get git submodule info
    return [ 'hardcoded-dep1' ]

def finalize_dist(dist):
    pp = toml.load('pyproject.toml')
    deps = pp.get('project')['dependencies']
    deps += get_git_submodules()
    print(f"Install dependencies: {deps}")
    setattr(dist,'install_requires', deps)

    # 'deps' replaced with that from pyproject.toml by setuptools
    # Unless we bind this function to a nothing function
    # I agree, it's a terrible way.  Not sure reliable to be stable.
    setattr(dist.metadata,'set_install_requires', install_requires_setter)
