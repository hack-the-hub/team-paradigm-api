from setuptools import setup

setup(
    name='vb_ddb',
    version='1.0.0',
    description='A DynamoDB Database abstraction library for Venuebooker',
    url='https://github.com/VenueBookerHQ/vb_ddb',
    license='The Unlicense',
    packages=[
        'vb_contact',
        'vb_ask_an_expert',
        'vb_newsletter',
    ],
    author='Apoclyps',
    author_email='kyle90adam@hotmail.com',
    install_requires=[
        'boto3==1.4.2',
        'tornado==4.4.2',
        'lettuce==0.2.23',
        'pyrestful==0.5.0',
    ]
)
