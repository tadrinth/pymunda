from setuptools import setup

setup(name='pymunda',
      version='0.1',
      description='Calculator of probabilities for a certain tabletop skirmish game',
      url='http://github.com/tadrinth/pymunda',
      author='Michael Wittig',
      author_email='mwittig@gmail.com',
      license='MIT',
      packages=['pymunda'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
)