# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-treescope
#
# You can edit this file again by typing:
#
#     spack edit py-treescope
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyTreescope(PythonPackage):
    """Treescope is an interactive HTML pretty-printer and N-dimensional array
    ("tensor") visualizer, designed for machine learning and neural networks
    research in IPython notebooks."""

    homepage = "https://github.com/google-deepmind/treescope"
    pypi = "treescope/treescope-0.1.10.tar.gz"

    license("Apache-2.0", checked_by="abhishek1297")

    version("0.1.10", sha256="20f74656f34ab2d8716715013e8163a0da79bdc2554c16d5023172c50d27ea95")

    variant(
        "notebook",
        default=False,
        description="Enable extra dependencies for notebook demos",
    )

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-flit-core@3.8:3", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy@1.25.2:")
        with when("+notebook"):
            depends_on("py-ipython")
            depends_on("py-palettable")
            depends_on("py-jax@0.4.23:")
