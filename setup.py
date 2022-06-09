import setuptools

setuptools.setup(name='coca',
      version='1.0.1',
      description='a spell checker for French',
      author='Mathilde, Xin',
      author_email="carolina.maeghan@gmail.com, chenxin9812@gmail.com",
      url='https://github.com/pypa/sampleproject',
      packages=setuptools.find_packages(),
      install_requires=[
            'requests',
            'spacy'
      ]

      )
