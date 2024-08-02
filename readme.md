# python-fast-cli

Test your download and upload speed using netflix's [fast.com](https://fast.com).

This package provides a command-line and Python interface for Fast.com,
offering a comprehensive alternative to other similar tools.
Unlike others, it **allows you to modify all settings** directly
from the interface as you would on the Fast.com website.
Additionally, it outputs results as a **time series**,
enabling more detailed analysis of bandwidth performance.

## implementation

this is pure python package based on python version of [playwright](https://playwright.dev/python/)

The playwright need to install browsers at the first time it is been used.

## Usage

```
usage: cli.py [-h] [--min-duration MIN_DURATION] [--max-duration MAX_DURATION] [--measure-upload-latency MEASURE_UPLOAD_LATENCY]
              [--min-connections MIN_CONNECTIONS] [--max-connections MAX_CONNECTIONS] [--should-persist SHOULD_PERSIST]
              [--show-advanced SHOW_ADVANCED] [--no-install-browser] [--no-upload] [--interval CHECK_INTERVAL] [--json]

options:
  -h, --help            show this help message and exit
  --min-duration MIN_DURATION
                        [default: 5]
  --max-duration MAX_DURATION
                        [default: 30]
  --measure-upload-latency MEASURE_UPLOAD_LATENCY
                        [default: False]
  --min-connections MIN_CONNECTIONS
                        [default: 1]
  --max-connections MAX_CONNECTIONS
                        [default: 8]
  --should-persist SHOULD_PERSIST
                        [default: True]
  --show-advanced SHOW_ADVANCED
                        [default: True]
  --no-install-browser  do not automatically install ['chromium']
  --no-upload           do not wait for upload test
  --interval CHECK_INTERVAL
                        data collection interval [default: 1.0]
```

By default, when this command is run for the first time, it will attempt to install the browser using the Playwright command. If you are certain that the browser is already installed via Playwright, you can suppress this behavior by using the --no-install-browser flag.
