# lsp_parser

![Github Actions Status](https://github.com/github_username/lsp-parser/workflows/Build/badge.svg)

Extension for JupyterLab-LSP to test listeners and language servers.

## Requirements

* JupyterLab >= 3.0
* jupyter_lsp

## Install

To install the extension, execute:

```bash
pip install -e .

jupyter server extension enable --sys-prefix --py lsp_parser
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall lsp_parser
```