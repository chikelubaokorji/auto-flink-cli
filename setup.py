from setuptools import setup

setup(
    name='auto-flink-cli',
    version='0.1.0',
    packages=['auto_flink'],
    entry_points={
        'console_scripts': [
            'auto_flink = auto_flink.__main__:main'
        ]
    })
