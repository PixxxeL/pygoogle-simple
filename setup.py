from distutils.core import setup
import pygoogle

setup(
    name = "pygoogle-simple",
    version = pygoogle.__version__,
    packages = ["pygoogle"],
    url = 'https://code.google.com/p/pygoogle/',
    author = 'Kiran Bandla',
    author_email = 'kbandla@in2void.com',
    maintainer = 'pixel',
    maintainer_email = 'ivan.n.sergeev@gmail.com',
    license = 'MIT',
    description = 'Search in google by AJAX Google API.',
    download_url = 'https://github.com/PixxxeL/pygoogle-simple.git',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
