from distutils.core import setup

setup(
    name='KvasirAPI',
    version='1.0.0',
    packages=['KvasirAPI', 'KvasirAPI/jsonrpc'],
    url='https://github.com/KvasirSecurity/kvasirapi-python',
    license='BSD',
    author='Kurt Grutzmacher',
    author_email='grutz@jingojango.net',
    description='Python API for Kvasir', requires=['pytest', 'jsonrpclib', 'pyyaml']
)
