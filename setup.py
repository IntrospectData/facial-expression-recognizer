from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fer_capture',
    version='0.2.0',
    license='MIT',
    description='Takes an image or video/stream as input and returns detected faces and emotions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bradley Reimers',
    author_email = 'b.a.reimers@gmail.com',
    url='https://github.com/IntrospectData/id-fer-capture',
    download_url='https://github.com/IntrospectData/id-fer-capture/archive/v0.2.0.tar.gz',
    keywords = ['facial', 'detection', 'emotion', 'recognition', 'ai', 'machine', 'vision', 'artificial', 'intelligence'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'opencv-python',
        'python-magic',
    ],
    extras_require = {
    'gpu':  ['tensorflow-gpu'],
    'cpu': ['tensorflow']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
  ],
)
