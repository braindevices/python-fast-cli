from argparse import ArgumentParser
import asyncio
import json
from .api import fast_config_t, run_speedtest, speedtest_config_t
DEFAULT_BROWSER = ["chromium"]

def camel_to_snake(s, sep="_"):
    return ''.join([sep+c.lower() if c.isupper() else c for c in s]).lstrip(sep)


def snake_to_camel(s, sep="_"):
    components = s.split(sep)
    # Capitalize the first letter of each component except the first one
    return components[0] + ''.join(x.title() for x in components[1:])


def parse_arguments():
    config = fast_config_t()
    parser = ArgumentParser()
    dests = []
    for key, val in config._asdict().items():
        option = camel_to_snake(key, sep="-")
        dests.append(option.replace("-", "_"))
        parser.add_argument(
            "--" + option,
            type=int,
            default=val,
            help="[default: %(default)s]"
        )
    
    parser.add_argument(
        "--no-install-browser",
        dest="auto_install_browsers",
        action="store_false",
        default=True,
        help=f"automatically install {DEFAULT_BROWSER}"
    )

    parser.add_argument(
        "--no-upload",
        dest="upload",
        action="store_false",
        default=True,
        help=f"do not wait for upload test"
    )

    parser.add_argument(
        "--interval",
        dest="check_interval",
        type=float,
        default=1.0,
        help="data collection interval [default: %(default)s]"
    )

    parser.add_argument(
        "--json",
        dest="output_json",
        action="store_true",
        default=False
    )

    parsed = parser.parse_args()
    d = {}
    for dest in dests:
        key = snake_to_camel(dest)
        d[key] = getattr(parsed, dest)
    fast = fast_config_t(**d)
    config = speedtest_config_t(
        fast_config=fast,
        upload=parsed.upload,
        check_interval=parsed.check_interval,
        print=True
    )
    return config, parsed.auto_install_browsers, parsed.output_json


def main():
    config, auto_install_browsers, output_json = parse_arguments()
    if auto_install_browsers:
        from .utils import auto_install_browsers
        auto_install_browsers()
    
    res = asyncio.run(run_speedtest(
        config
    ))
    if output_json:
        jstr = json.dumps(res, indent=True)
        print(jstr)


if __name__ == "__main__":
    main()
