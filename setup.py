"""
lsp_parser setup
"""
import setuptools
from pathlib import Path

from jupyter_packaging import (
    get_version,
    get_data_files
)

HERE = Path(__file__).parent.resolve()

name = "lsp_parser"
version = get_version((HERE / name / '_version.py'))
license = (HERE / "LICENSE").read_text()
long_description = (HERE / "README.md").read_text()

data_files_spec = [
    ("etc/jupyter/jupyter_server_config.d", "jupyter-config/server-config", "lsp_parser.json"),
    # For backward compatibility with notebook server
    ("etc/jupyter/jupyter_notebook_config.d", "jupyter-config/nb-config", "lsp_parser.json"),
]

setup_args = dict(
    name=name,
    version=version,
    license=license,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    data_files=get_data_files(data_files_spec),
    install_requires=["jupyter_server>=1.6,<2"],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.6",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "JupyterLab", "JupyterLab3"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Jupyter",
    ],
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
