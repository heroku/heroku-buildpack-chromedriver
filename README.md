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

Due to limitations on Heroku, you may observe unpredictable behavior when
using a screen size that is too large.  This can result in ambiguous error
messages such as "chrome not reachable" or "session deleted because of page
crash from tab crashed."  In the event you see either of these messages,
try reducing your window size.  1200x800 has generally seemed safe for use
on a free dyno.
