from setuptools import setup, find_packages


setup (
    name = 'cf',
    version = '1.0',
    url = 'https://github.com/guilhermeleobas/cf',
    license = 'MIT',
    author = 'Guilherme Leobas',
    # description = 'Get inputs and outputs from Codeforces and others online judges',
    long_description = open('README.md').read(),
    keywords = 'Codeforces',
    install_requires = open('requirements.txt').read().splitlines(),
    packages = find_packages(exclude=['docs', 'test*']),
    include_package_data = True,
    extras_require = {
        'test': ['pytest'],
    },
    entry_points = {
        'console_scripts': [
            # 'skele=skele.cli:main',
            'cf=cf.cf:main'
        ],
    },
)
