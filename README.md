# Vocabulary List Generator

## Description:
📝This program queries Google, WikiPedia and Oxford Dictionary for the definitions of multiple words and compiles these definitions into a single "vocabulary" list

## Installation

Use one of the following methods:

- ### Using Terminal
  Open a terminal 
  ``` 
  cd <PATH FOR INSTALLATION>
  git clone https://github.com/museHD/Vocab-List-Gen
  pip install -r requirements.txt
  ```
- ### Downloading Release
  It is recommended to create a separate folder for the application.
  Download the latest [release](https://github.com/museHD/Vocab-List-Gen/releases) to the folder and run it. 
  Most of the dependencies should be contained within the release and those that aren't will be downloaded to the folder.


## Usage:
Simply enter words separated by commas into the program and it will return the list of words and the top definition for each word.

Note: Part of the program is still quite unstable and may not always give the most relevant definition

## Contributing
Please feel free to raise issues and suggest changes to the project. We are always looking for improvements!
Please make sure that any pull requests are made to the `development` branch as these changes will later be merged to master once the `development` branch is stable.
Thank you!

## Dependencies:
The program uses the following libraries:
<a href="https://github.com/SeleniumHQ/selenium">Selenium</a>, <a href="https://github.com/pwaller/pyfiglet">PyFiglet</a>
<br>
The libraries have been taken care of in the <a href="https://github.com/museHD/Vocab-List-Gen/releases">exe release</a>
<br><br>
However, all users will need to get the **matching/compatible** versions of Google Chrome and [Chromedriver](https://chromedriver.chromium.org/). Make sure that the chromedriver.exe file is in the same directory as the application.
Eg. If you have Chrome 86, download the ChromeDriver v86 from the above link and place the exe in the same directory as this program.
<br>
<br>
<br>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
