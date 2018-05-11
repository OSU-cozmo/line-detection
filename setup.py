from setuptools import setup

setup(
    name = 'CosmOSU Line Detection',
    version = '0.1',
    description = 'Line detection using Anki\'s Cozmo',
    url='https://github.com/OSU-cozmo/line-detection',
    license = 'MIT',
    packages = ['lineDetection'],
    install_requires=['cozmo[camera]'],
    zip_safe = True)
