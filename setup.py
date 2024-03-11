from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quantbit_calibration_process/__init__.py
from quantbit_calibration_process import __version__ as version

setup(
	name="quantbit_calibration_process",
	version=version,
	description="tract details of measurable equipment calibration process",
	author="tejal kumbhar",
	author_email="tejal.kumbhar@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
