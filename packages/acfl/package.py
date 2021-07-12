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
#     spack install acfl
#
# You can edit this file again by typing:
#
#     spack edit acfl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import llnl.util.tty as tty
import subprocess

_os_map = {
        'ubuntu18.04': 'Ubuntu-18.04',
        'ubuntu20.04': 'Ubuntu-20.04',
        'sles15': 'SLES-15',
        'centos7': 'RHEL-7',
        'centos8': 'RHEL-8',
        'amzn2': 'RHEL-7'
        }



_versions = {
            '21.0': {
                'RHEL-7': ('fa67a4b9c1e562ec73e270aa4ef7a969af99bdd792ce8916b69ee47f7906110b', 
                    'https://developer.arm.com/-/media/Files/downloads/hpc/arm-allinea-studio/21-0/ACfL/arm-compiler-for-linux_21.0_RHEL-7_aarch64.tar'),
                'RHEL-8': ('a1bf517fc108100878233610ec5cc9538ee09cd114670bfacab0419bbdef0780', 
                    'https://developer.arm.com/-/media/Files/downloads/hpc/arm-allinea-studio/21-0/ACfL/arm-compiler-for-linux_21.0_RHEL-8_aarch64.tar'),
                'SLES-15': ('0307c67425fcf6c2c171c16732353767f79a7dd45e77cd7e4d94675d769cce77', 
                    'https://developer.arm.com/-/media/Files/downloads/hpc/arm-allinea-studio/21-0/ACfL/arm-compiler-for-linux_21.0_SLES-15_aarch64.tar'),
                'Ubuntu-18.04': ('f57bd4652ea87282705073ea81ca108fef8e0725eb4bc441240ec2fc51ff5980', 
                    'https://developer.arm.com/-/media/Files/downloads/hpc/arm-allinea-studio/21-0/ACfL/arm-compiler-for-linux_21.0_Ubuntu-18.04_aarch64.tar'),
                'Ubuntu-20.04': ('dd93254b9fe9baa802baebb9da5d00e0076a639b47f3515a8645b06742900eea', 
                    'https://developer.arm.com/-/media/Files/downloads/hpc/arm-allinea-studio/21-0/ACfL/arm-compiler-for-linux_21.0_Ubuntu-20.04_aarch64.tar')
                }
            }

def get_os():
   spack_os = spack.architecture.platform().default_os
   if spack_os in _os_map:
       return _os_map[spack_os]
   else:
       return 'RHEL-7' # Default value

class Acfl(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://developer.arm.com/tools-and-software/server-and-hpc/downloads/arm-allinea-studio"
    url      = "ACFL"

    maintainers = ['OliverPerks']

    # Build Versions: establish OS for URL
    acfl_os=get_os()

    # Build Versions
    for ver, packages in _versions.items():
        pkg = packages.get(acfl_os)
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1])
    



    def install(self, spec, prefix):
        
        exe='./arm-compiler-for-linux_{0}_{1}.sh'.format(spec.version, get_os())
        subprocess.call([exe, "--accept", "--force", "--install-to", prefix])

