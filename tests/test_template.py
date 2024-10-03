"""Tests for PinP-Role-Template Python specific build."""

from __future__ import annotations

from pathlib import Path

import copier
import pytest

PROJECT_ROOT = Path(__file__).parent.parent


def test_fully_templated(tmp_path: Path, base_answers: dict[str, str | bool], helpers):

    dst_path = tmp_path / base_answers["role_name"]
    worker = copier.run_copy(
        src_path=str(PROJECT_ROOT),
        dst_path=dst_path,
        data=base_answers,
        defaults=True,
        unsafe=True,
    )
    assert worker is not None
    assert dst_path.exists()
    helpers.detect_unprocessed_jinja(
        dst_path,
        [
            dst_path / ".gitea",
        ],
    )


def test_readme_file_content(
    tmp_path: Path, base_answers: dict[str, str | bool], helpers
):
    dst_path = tmp_path / base_answers["role_name"]
    worker = copier.run_copy(
        src_path=str(PROJECT_ROOT),
        dst_path=dst_path,
        data=base_answers,
        defaults=True,
        unsafe=True,
    )
    assert worker is not None
    assert dst_path.exists()
    title = f"# { base_answers['collection_name'] }.{base_answers['role_name']}"
    readme_path = dst_path / "README.md"

    helpers.assert_file_content(
        readme_path,
        [
            title,
            base_answers["short_description"],
            f"{base_answers['author_name']} ({base_answers['author_email']})",
        ],
    )


@pytest.mark.parametrize(
    "license,content",
    [
        ("MIT", "MIT License"),
        ("Apachev2", "Apache License"),
        ("BSD", "BSD License"),
        ("ISC", "ISC License"),
        ("GNUv3", "GNU GENERAL PUBLIC LICENSE"),
        ("GNULesserv3", "GNU LESSER GENERAL PUBLIC LICENSE"),
        ("Other", ""),
    ],
)
def test_license_file_exists(
    tmp_path: Path, base_answers: dict[str, str | bool], helpers, license, content
):
    dst_path = tmp_path / base_answers["role_name"]
    base_answers["license"] = license
    worker = copier.run_copy(
        src_path=str(PROJECT_ROOT),
        dst_path=dst_path,
        data=base_answers,
        defaults=True,
        unsafe=True,
    )
    assert worker is not None
    assert dst_path.exists()
    license_path = dst_path / "LICENSE"
    assert license_path.exists()
    helpers.assert_file_content(license_path, [content])
