import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="download-symbols",
    version="0.0.1",
    author="leo",
    author_email="1823280359@qq.com",
    description="download symbols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/culeo/download_ios_system_symbols",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    entry_points = {
        'console_scripts': ['download-symbols=download_symbols.download_symbols:main'],
    }
)
