# heroku-buildpack-chromedriver

This buildpack installs **Google Chrome browser** `chrome` &
[`chromedriver`](https://chromedriver.chromium.org/), the Selenium driver for Chrome, in a Heroku app.

## Configuring the downloaded version of chromedriver.

By default, this buildpack will download the latest `Stable` release, which is provided
by [Google](https://googlechromelabs.github.io/chrome-for-testing/).

You can control the channel of the release by setting the `GOOGLE_CHROME_CHANNEL`
config variable to `Stable`, `Beta`, `Dev`, or `Canary`, and then deploy/build the app.

Chrome is "evergreen", so they do not support downloading specific versions, 
but instead the latest from any of these channels.

## Releasing a new version

Make sure you publish this buildpack in the buildpack registry

`heroku buildpacks:publish heroku/chromedriver master`
