# heroku-buildpack-chromedriver

This buildpack installs
[`chromedriver`](https://sites.google.com/a/chromium.org/chromedriver/)
 (the Selenium driver for Chrome) in a Heroku slug.
 
 This buildpack only installs the `chromedriver` binary. To use Selenium with Chrome
 on Heroku, you'll also need Chrome. We suggest one of these buildpacks:
 
 - [heroku-buildpack-google-chrome](https://github.com/heroku/heroku-buildpack-google-chrome) 
   to run Chrome with the `--headless` flag
 - [heroku-buildpack-xvfb-google-chrome](https://github.com/heroku/heroku-buildpack-xvfb-google-chrome)
   to run Chrome against a virtual window server

The `chromedriver` binary depends on Chrome. You need to put Chrome buildpack first in the order.

e.g;

1. https://github.com/heroku/heroku-buildpack-google-chrome.git
2. https://github.com/heroku/heroku-buildpack-chromedriver.git

## Configuring the downloaded version of chromedriver.

By default, this buildpack will download the latest release, which is provided
by [Google](https://chromedriver.storage.googleapis.com/LATEST_RELEASE).

You can control the specific version by setting the `CHROMEDRIVER_VERSION`
variable to an explicit version e.g. `2.39`.


## Releasing a new version

Make sure you publish this buildpack in the buildpack registry

`heroku buildpacks:publish heroku/chromedriver master`
