# file_processing_tools_template
A demo project of the file_processing_tools library: https://github.com/hc-sc-ocdo-bdpd/file-processing-tools

<br>

## Installation

To begin installation, clone this repository and then follow one of the below options.

<br>

### Option 1: `venv`

> Pre-requisite(s): `Python (v3)`, `ffmpeg`, `Tesseract`. See [here](https://hc-sc-ocdo-bdpd.github.io/file-processing-tools/1_tutorial/1_installation.html#additional-dependencies) for installation. These are not hard requirements; they are used for transcription (audio-to-text) and OCR (image-to-text)

Create the virtual environment in VSCode: `View` (top left of the screen) > `Command Palette` > `Python: Create Environment` > `Venv` > `your-python-version` > `requirements.txt`

<br>

### Option 2: `Dockerfile`

> Pre-requisite(s): Docker

1. Install the VSCode extension: `Remote Development` (by Microsoft)
2. In the top navigation menu: `View` > `Command Palette` > `Dev Containers: Rebuild and Reopen in Container`

If step 2 does not work, then try after replacing the code in `.devcontainer/devcontainer.json` with the following:

```json
{
	"name": "Your Dev Container",
	"image": "docker.io/benjaminluohc/file_processing_tools:latest"
}
```
