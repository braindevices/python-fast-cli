import asyncio
from .api import fast_config_t, run_speedtest
async def main():
    res = await run_speedtest(
        fast_config_t(
            minDuration=5,
            maxDuration=5,
            minConnections=1,
            maxConnections=1
        )
    )

if __name__ == "__main__":
    auto_install_browsers = True
    if auto_install_browsers:
        from .utils import auto_install_browsers
        auto_install_browsers()
    asyncio.run(main())
