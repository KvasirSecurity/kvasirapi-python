from distutils.core import setup

setup(
    name='KvasirAPI',
    version='1.0.0',
    packages=['KvasirAPI', 'KvasirAPI/jsonrpc'],
    url='https://github.com/KvasirSecurity/kvasirapi-python',
    license='BSD',
    author='Kurt Grutzmacher',
    author_email='grutz@jingojango.net',
    description='Python API for Kvasir',
    install_requires=['jsonrpclib', 'pyyaml'],
    classifiers = [
      "Programming Language :: Python",
      "Intended Audience :: Developers",
      "Operating System :: OS Independent",
      "Development Status :: 5 - Production/Stable",
      "License :: OSI Approved :: BSD License",
      "Topic :: Security",
    ]
)
