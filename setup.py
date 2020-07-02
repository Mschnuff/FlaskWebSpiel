try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Moritz',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'kappels@internet-sicherheit.de',
    'version': '0.1',
    'install_requires': ['nose', 'flask'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
