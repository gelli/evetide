from setuptools import setup, find_packages
from evetide import __version__

setup(
    name = 'evetide',
    version = __version__,
    packages = find_packages(),
    author = 'Christian Gellweiler',
    author_email = 'cgellweiler@gmail.com',
    url = 'https://github.com/gelli/evetide',
    entry_points = {
        'console_scripts': [
            'evetide = evetide.main:main',
        ],
    },
    install_requires = [
    ],
#    package_data = {
#        'river': [
#            'templates/*',
#        ],
#    },
)
