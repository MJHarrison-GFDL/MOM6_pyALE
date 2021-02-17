"""
"""
from numpy.distutils.core import setup,Extension

doclines = __doc__.split("\n")


vertmap_ALE = Extension(name = 'vertmap_ALE',
                include_dirs = ['.mod'],
                library_dirs = ['.'],
                libraries = ['ALE'],
                sources = ['pyale.f90'])


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = "pyALE",
          version = '1.2.4',
          description = doclines[0],
          long_description = "\n".join(doclines[2:]),
          author = "Matthew Harrison",
          author_email = "matthew.harrison@noaa.gov",
          url = "none",
          license = 'CCL',
          platforms = ["any"],
          ext_modules = [vertmap_ALE],
          )
