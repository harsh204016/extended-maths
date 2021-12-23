from setuptools import setup
from setuptools import find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
      
      setup(
            name='extended_maths',
            version='0.0',
            long_description=long_description,
            long_description_content_type='text/markdown',
            packages=find_packages(),
            description='Mathmatical functions',
            packages=['extended_maths'],
            author_email='harshgupta204016@gmail.com',
            url="https://github.com/harsh204016/extended-maths",
            zip_safe=False
      )
