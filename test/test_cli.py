from loguru import logger
import subprocess
import os
import shutil

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
VIDEO_PATH = os.path.join(PROJECT_PATH, "demo.mp4")


def test_cli():
    logger.info("checking main")
    subprocess.check_call(["python", "-m", "stagesepx.cli"])

    logger.info("checking one_step ...")
    subprocess.check_call(["stagesepx", "one_step", VIDEO_PATH])
    subprocess.check_call(["stagesepx", "one_step", VIDEO_PATH, "output"])
    shutil.rmtree("output")
