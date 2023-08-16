import json
import requests

def get_stable_version():
    good_versions_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions.json"

    good_versions = requests.get(good_versions_url).json()

    return good_versions["channels"]["Stable"]["version"]


def get_chrome_driver_version():
    platform = "linux64"
    stable_version = get_stable_version()
    versions_map_url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"

    versions_map = requests.get(versions_map_url).json()

    for version in versions_map["versions"]:
        if version["version"] == stable_version:
            chrome_driver_downloads = version["downloads"]["chromedriver"]
            for download in chrome_driver_downloads:
                if download["platform"] == platform:
                    return download["url"]

    raise Exception("Could not find ChromeDriver version for Chrome version: " + stable_version)


if __name__ == "__main__":
    print(get_chrome_driver_version())
