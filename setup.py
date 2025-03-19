from setuptools import find_packages, setup

setup(
    name="text_cleaner_for_py",
    version="1.1.4",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.12.0",
        "requests>=2.31.0",
        "nltk",
    ],
    author="Roberto Lima",
    author_email="robertolima.izphera@gmail.com",
    description="🧹 Um pacote para limpeza e normalização de texto em Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/robertolima-dev/text-cleaner-for-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    license="MIT",
)
