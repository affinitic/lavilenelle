from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='lavilenelle.skin',
      version=version,
      description="La chorale La Vilenelle Site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='https://github.com/affinitic/lavilenelle',
      license='gpl',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['lavilenelle'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.themingplugins',
          # -*- Extra requirements: -*-
      ])
