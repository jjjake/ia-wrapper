import re
from ast import literal_eval
from codecs import open

from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('internetarchive/__init__.py', 'r') as f:
    re_match = _version_re.search(f.read())
if re_match:
    version = literal_eval(re_match.group(1))
else:
    version = 'unknown'

with open('README.rst', 'r') as f:
    readme = f.read()
with open('HISTORY.rst', 'r') as f:
    history = f.read()

setup(
    name='internetarchive',
    version=version,
    url='https://github.com/jjjake/internetarchive',
    license='AGPL 3',
    author='Jacob M. Johnson',
    author_email='jake@archive.org',
    description='A Python interface to archive.org.',
    long_description=readme,
    include_package_data=True,
    zip_safe=False,
    packages=[
        'internetarchive',
        'internetarchive.cli',
    ],
    entry_points={
        'console_scripts': [
            'ia = internetarchive.cli.ia:main',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        'docopt>=0.6.0,<0.7.0',
        'jsonpatch>=0.4',
        'requests>=2.25.0,<3.0.0',
        'schema>=0.4.0',
        'tqdm>=4.0.0',
        'urllib3>=1.26.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
