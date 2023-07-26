import os
import shutil

import uvicorn

from src.config import settings


def set_multiproc_dir() -> None:
    """
    Sets mutiproc_dir env variable.

    This function cleans up the multiprocess directory
    and recreates it. This actions are required by prometheus-client
    to share metrics between processes.

    After cleanup, it sets two variables.
    Uppercase and lowercase because different
    versions of the prometheus-client library
    depend on different environment variables,
    so I've decided to export all needed variables,
    to avoid undefined behaviour.
    """
    shutil.rmtree(settings.PROMETHEUS_DIR, ignore_errors=True)
    os.makedirs(settings.PROMETHEUS_DIR, exist_ok=True)
    os.environ["prometheus_multiproc_dir"] = str(
        settings.PROMETHEUS_DIR.expanduser().absolute(),
    )
    os.environ["PROMETHEUS_MULTIPROC_DIR"] = str(
        settings.PROMETHEUS_DIR.expanduser().absolute(),
    )


def main() -> None:
    """Entrypoint of the application."""
    set_multiproc_dir()
    uvicorn.run(
        "src.application:get_app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.SERVER_RELOAD,
        log_level=settings.LOG_LEVEL.value.lower(),
        workers=settings.SERVER_WORKERS_COUNT,
        factory=True,
    )


if __name__ == "__main__":
    main()
