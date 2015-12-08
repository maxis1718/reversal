from setuptools import find_packages
from setuptools import setup

setup(
    name='reversal',
    description='A furious war between trading indices',
    url='https://github.com/maxis1718/reversal',
    version='0.1',

    author='Maxis Kao',
    author_email='maxis1718@gamil.com',

    license='MIT',
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    zip_safe=False
)
