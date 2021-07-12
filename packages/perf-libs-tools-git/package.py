# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
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
#     spack install perf-libs-tools-git
#
# You can edit this file again by typing:
#
#     spack edit perf-libs-tools-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PerfLibsToolsGit(MakefilePackage):
    """This project provides tools to enable users of HPC applications to understand 
    which routines from Arm Performance Libraries are being called."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ARM-software/perf-libs-tools"
    git      = "https://github.com/ARM-software/perf-libs-tools.git"

    # notify when the package is updated.
    maintainers = ['OliverPerks', 'chrisgoodyer']

    version('master', branch='master')

    # Patch to remove xblas.h include and non gcc routines
    patch('simple.patch')


    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')
        makefile.filter(r'\s*CC\s*=.*',  'CC = '  + spack_cc)

    def install(self, spec, prefix):
        make()

        # Install
        install_tree('lib', prefix.lib)
        install_tree('tools', prefix.bin)

    def setup_run_environment(self, env):
        env.prepend_path("PYTHONPATH", join_path(self.prefix, "bin"))
