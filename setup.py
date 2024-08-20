from setuptools import setup, find_packages

setup(
    name='bmi_calculator',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='A simple BMI calculator package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Shahin ABDI',
    author_email='shahin.abdi.pro@gmail.com',
    url='https://github.com/shahinabdi/BMICalculator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)c