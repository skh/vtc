from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Video Toolchain'
  
setup(
        name ='vtc',
        version ='1.0.0',
        author ='Sonja Krause-Harder',
        author_email ='me@skh.io',
        url ='https://github.com/skh/vtc',
        description ='Video Toolchain.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'vtc = src.vtc:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GPLv3",
            "Operating System :: OS Independent",
        ),
        keywords ='youtube skh',
        install_requires = requirements,
        zip_safe = False
)