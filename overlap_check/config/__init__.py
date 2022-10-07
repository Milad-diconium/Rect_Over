# overlap_check license info.

"""
overlap_check-sdk

This provides access to different configurations.
"""

from pathlib import Path

from pyhocon import ConfigFactory

this_dir = Path(__file__).parent
platform_path = this_dir / "platform.conf"
platform_conf = ConfigFactory.parse_file(platform_path)
