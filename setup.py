"""
"""
from numpy.distutils.core import setup,Extension

doclines = __doc__.split("\n")


remap  = Extension(name = 'remap',
                include_dirs = ['.mod'],
                library_dirs = ['.'],
                libraries = ['Remap'],
                sources = ['remap.f90'])


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(name = "pyRemapping",
          version = '1.2.4',
          description = doclines[0],
          long_description = "\n".join(doclines[2:]),
          author = "Matthew Harrison",
          author_email = "matthew.harrison@noaa.gov",
          url = "none",
          license = 'CCL',
          platforms = ["any"],
          ext_modules = [remap],
          )
