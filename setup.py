#!/usr/bin/env python

from setuptools import setup, find_namespace_packages

setup(
    name="proton-vpn-gtk-app",
    version="0.0.0",
    description="Proton VPN GTK app",
    author="Proton Technologies",
    author_email="contact@protonmail.com",
    url="https://github.com/ProtonVPN/proton-vpn-gtk-app",
    install_requires=["proton-vpn-api-core", "proton-vpn-network-manager-openvpn"],
    extras_require={
        "development": ["pygobject", "pycairo", "pygobject-stubs", "pytest", "pytest-coverage", "flake8"]
    },
    packages=find_namespace_packages(include=['proton.vpn.app.gtk']),
    include_package_data=True,
    python_requires=">=3.8",
    license="GPLv3",
    platforms="OS Independent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Security",
    ],
    entry_points={
        "console_scripts": [
            ['protonvpn-app=proton.vpn.app.gtk.__main__:main'],
        ],
    }
)