from setuptools import find_packages
from setuptools import setup


version = "1.3.3.dev0"

setup(
    name="recensio.altertum",
    version=version,
    description="Altertum customizations for Recensio",
    long_description=(open("README.txt").read() + "\n" + open("CHANGES.txt").read()),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="web zope plone theme Python CMS",
    author="Syslab.com GmbH",
    author_email="info@syslab.com",
    url="https://github.com/syslabcom/recensio.altertum/",
    project_urls={
        "Source": "https://github.com/syslabcom/recensio.altertum",
        "Tracker": "https://github.com/syslabcom/recensio.altertum/issues",
    },
    license="GPL",
    packages=["vocabularies"] + find_packages(exclude=["ez_setup"]),
    namespace_packages=["recensio"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "recensio.plone",
        "z3c.jbot",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
