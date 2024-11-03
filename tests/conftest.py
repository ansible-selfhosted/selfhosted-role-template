"""Configuration module for the tests."""

from pathlib import Path
from typing import Sequence

import pytest


class Helpers:
    """Reusable functions for testing."""

    @classmethod
    def detect_unprocessed_jinja(
        cls,
        top_path: Path,
        ignored_subfolder: Sequence[Path] = (),
    ) -> None:
        """Walk the top path recursively to check for unprocessed jinja template."""
        for p in Path(top_path).iterdir():
            for symbols in ["{%", "%}", "{{", "}}"]:
                assert symbols not in p.name

            if p.is_dir():
                if p not in ignored_subfolder:
                    cls.detect_unprocessed_jinja(p)
                continue
            try:
                file_content = p.read_text()
            except UnicodeDecodeError:  # catch for non text files (i.e: .png, .jpg)
                continue
            if "# skip jinja testing" in file_content:
                continue
            for symbols in ["{%", "%}", "{{", "}}"]:
                assert symbols not in file_content

    @staticmethod
    def assert_file_content(
        file_path: Path,
        expected_strs: Sequence[str] = (),
        unexpected_strs: Sequence[str] = (),
    ) -> None:
        """Check the provided file's content for expected and unexpected strings."""
        assert file_path.exists()
        file_content = file_path.read_text()
        for content in expected_strs:
            assert content in file_content
        for content in unexpected_strs:
            assert content not in file_content


@pytest.fixture
def helpers():
    return Helpers


@pytest.fixture
def base_answers():
    return {
        "author_name": "SpeakinTelnet",
        "author_email": "SpeakinTelnet@example.com",
        "author_company": "",
        "role_name": "rolename",
        "related_url": "example.com",
        "collection_name": "services",
        "license": "MIT",
        "copyright_holder": "SpeakinTelnet",
        "short_description": "Template test description",
        "repository_host": "codeberg.org",
        "repository_url": "https://www.codeberg.org/SpeakinTelnet/python-test",
    }
