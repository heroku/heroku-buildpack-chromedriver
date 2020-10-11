# heroku-buildpack-chromedriver

This buildpack installs
[`chromedriver`](https://sites.google.com/a/chromium.org/chromedriver/)
 (the Selenium driver for Chrome) in a Heroku slug.
 
 This buildpack only installs the `chromedriver` binary. To use Selenium with Chrome
 on Heroku, you'll also need Chrome. We suggest one of these buildpacks:
 
 - [heroku-buildpack-google-chrome](https://github.com/heroku/heroku-buildpack-google-chrome) 
   to run Chrome with the `--headless` flag
    - Make sure you've installed heroku-buildpack-google-chrome BEFORE heroku-buildpack-chromedriver, so it can install the latest supported chromedriver for the verison of Chrome installed previously.
 - [heroku-buildpack-xvfb-google-chrome](https://github.com/heroku/heroku-buildpack-xvfb-google-chrome)
   to run Chrome against a virtual window server


## Configuring the downloaded version of chromedriver.

By default, this buildpack will download the latest release, which is provided
by [Google](https://chromedriver.storage.googleapis.com/LATEST_RELEASE).

If you've installed heroku-buildpack-google-chrome before this buildpack, it will download the latest supported chromedriver which has the same build version of the Chrome installed previously.
    - Here's the rule of the version number of Google Chrome: <https://www.chromium.org/developers/version-numbers>
    - Here's the rule of version selection implemented in this buildpack: <http://chromedriver.chromium.org/downloads/version-selection>
        - This only works for stable version and beta version of Chrome as describe in this document.

You can control the specific version by setting the `CHROMEDRIVER_VERSION`
environment variable to an explicit version e.g. `2.39`.


## Releasing a new version

Make sure you publish this buildpack in the buildpack registry

`heroku buildpacks:publish heroku/chromedriver master`
