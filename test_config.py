"""Basic config loading tests."""

import os
import tempfile
import pytest


def test_example_config_exists():
    assert os.path.isfile("config.example.yml")


def test_example_config_parseable():
    import yaml
    with open("config.example.yml") as f:
        cfg = yaml.safe_load(f)
    assert "device_address" in cfg
    assert "adapter" in cfg
