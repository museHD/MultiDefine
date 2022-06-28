<h1 align="center">MultiDefine</h1>

## About the Project:
📝This program queries Google, WikiPedia and Oxford Dictionary for the definitions of multiple words and compiles these definitions into a single list of definitions.

It was created to help with my schoolwork, which often involved finding definitions of a long list of technical words. I realised I was wasting a lot of time manually searching the definitons of each of the words and writing them down, so I decided to automate this process.

## Getting Started

### Prerequisites
* The program has been built and tested on Windows 10+ machines, so its recommended to use a Windows Machine
* If using MacOS or other environments, try the manual installation process. If you have any issues, please create a new issue [here](https://github.com/museHD/MultiDefine/issues)
* For manual installation, [Python](https://www.python.org/downloads/) needs to be installed

Use one of the following methods to use the program:

- #### Manual Installation
  Open a terminal,
  ``` 
  cd <PATH FOR INSTALLATION>
  git clone https://github.com/museHD/MultiDefine
  pip install -r requirements.txt
  ```
- #### Downloading Release (Only on Windows)
  It is recommended to create a separate folder for the application.
  Download the latest [release](https://github.com/museHD/Vocab-List-Gen/releases) to the folder and run it. 
  Most of the dependencies will be contained within the release and those that aren't will be downloaded to the folder.


### Usage:

- #### Manually Installed
  Open a terminal.
  Run using `python multidefine.py`
- #### EXE File
  Open the folder where the exe is downloaded.
  Double click to run the program.

Simply enter words separated by commas into the program and it will return the list of words and the top definition for each word.
Note: Part of the program is still quite unstable and may not always give the most relevant definition.

## Contributing
Please feel free to raise issues and suggest changes to the project. We are always looking for improvements!
Please make sure that any pull requests are made to the `development` branch as these changes will later be merged to master once the `development` branch is stable.
Thank you!

## Dependencies:
The program uses the following libraries:
* <a href="https://github.com/SeleniumHQ/selenium">Selenium</a>
* <a href="https://github.com/pwaller/pyfiglet">PyFiglet</a>
<br>
The libraries have been taken care of in the <a href="https://github.com/museHD/Vocab-List-Gen/releases">exe release</a>
<br><br>
All users need to have the **matching/compatible** versions of Google Chrome and [Chromedriver](https://chromedriver.chromium.org/). If you are facing issues, make sure that the chromedriver.exe file is in the same directory as the application.
Eg. If you have Chrome 86, download the ChromeDriver v86 from the above link and place the exe in the same directory as this program.
<br>
<br>
<br>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
