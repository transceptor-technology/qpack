#
#  Got documentation from: http://peterdowns.com/posts/first-time-with-pypi.html
#
#   1. Create tag:
#       git tag 0.0.1 -m "Adds a tag so that we can put this new version on PyPI."
#
#   2. Push tag:
#       git push --tags origin master
#
#   3. Upload your package to PyPI Test:
#       python setup.py register -r pypitest
#       python setup.py sdist upload -r pypitest
#
#   4. Upload to PyPI Live
#       python setup.py register -r pypi
#       python setup.py sdist upload -r pypi
#

from distutils.core import setup
setup(
    name='qpack',
    packages=['qpack'],
    version='0.0.1',
    description='Fast and efficient data serializer',
    author='Jeroen van der Heijden',
    author_email='jeroen@transceptor.technology',
    url='https://github.com/transceptor-technology/qpack',
    download_url='https://github.com/transceptor-technology/trender/tarball/1.0.4',
    keywords=['template', 'engine', 'render'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
)