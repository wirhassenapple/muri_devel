from setuptools import find_packages, setup

package_name = 'muri_dev_ta1_action_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='benji',
    maintainer_email='benjamin.keppler@stud.hs-kempten.de',
    description='provision of actual action server for GoTo',
    license='Apache-2.',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
