from setuptools import setup, find_packages


setup (
    name = 'cftool',
    version = '1.0.7',
    url = 'https://github.com/guilhermeleobas/cftool',
    license = 'MIT',
    author = 'Guilherme Leobas',
    description = 'Get inputs and outputs from Codeforces and others online judges',
    long_description = open('README.md').read(),
    keywords = 'Codeforces',
    install_requires = open('requirements.txt').read().splitlines(),
    packages = find_packages(exclude=['docs', 'test*']),
    include_package_data = True,
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
            # 'skele=skele.cli:main',
            'cftool=cftool.cftool:main'
        ],
    },
)
