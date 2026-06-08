#!/usr/bin/env python3
"""Sync Android app asset legal/en/*.md → docs/android/*.md with web-friendly transformations.

Source of truth: /Users/onurakcakavak/Downloads/Android/ColorCargo/app/src/main/assets/legal/en/
Destination:     <this repo>/docs/android/

Transformations (idempotent, mirrors iOS docs/sync_legal.py):
1. colorcargo://privacy|terms|about       → privacy.html | terms.html | about.html
2. colorcargo://report-ad                 → mailto: with subject + body prefilled
3. **email** (no link) / [**email**](mailto:email) → [email](mailto:email)
4. Plain email (not in a link)            → [email](mailto:email)
5. Bold-wrapped links **[text](url)**     → [text](url)  (UX feedback: bold itici)
6. Bold-spans containing a link           → unwrap bold (CommonMark flanking)
7. Version placeholders                   → resolved values

Recurring rule (HANDOFFAndroid + auto-memory): Android EN legal değişirse bu script
çalıştırılır + commit + push + GitHub Pages URL doğrulanır.

Run:
    python3 sync_android_legal.py
"""
import os
import re
import sys
from urllib.parse import quote

ANDROID_REPO = '/Users/onurakcakavak/Downloads/Android/ColorCargo'
ANDROID_SOURCE = os.path.join(ANDROID_REPO, 'app/src/main/assets/legal/en')
ANDROID_GRADLE = os.path.join(ANDROID_REPO, 'app/build.gradle.kts')
DEST_SUBDIR = os.path.join('docs', 'android')
DOCS = ['privacy', 'terms', 'about']
EMAIL = 'onuragames@gmail.com'


def read_android_version():
    """Parse versionName + versionCode from app/build.gradle.kts.

    Falls back to ('?', '?') if the file is missing or malformed, so the script
    still runs (placeholders just stay literal). Recurring rule: bump these in
    Android Gradle, re-run this script, public docs catch up automatically.
    """
    if not os.path.exists(ANDROID_GRADLE):
        return ('?', '?')
    with open(ANDROID_GRADLE) as f:
        text = f.read()
    name_m = re.search(r'versionName\s*=\s*"([^"]+)"', text)
    code_m = re.search(r'versionCode\s*=\s*(\d+)', text)
    return (
        name_m.group(1) if name_m else '?',
        code_m.group(1) if code_m else '?',
    )


def fix_web_links(content: str, version_short: str, version_build: str) -> str:
    email_re = re.escape(EMAIL)

    # 1. [**email**](mailto:email) → [email](mailto:email)
    content = re.sub(
        r'\[\*\*(' + email_re + r')\*\*\]\(mailto:\1\)',
        r'[\1](mailto:\1)',
        content,
    )
    # 2. **email** (no link yet) → [email](mailto:email)
    content = re.sub(
        r'\*\*(' + email_re + r')\*\*',
        r'[\1](mailto:\1)',
        content,
    )
    # 3. Plain email (not in any link) → [email](mailto:email)
    content = re.sub(
        r'(?<!mailto:)(?<!\[)\b(' + email_re + r')\b(?!\]\()',
        r'[\1](mailto:\1)',
        content,
    )
    # 4. Custom scheme → web pages
    content = content.replace('colorcargo://terms', 'terms.html')
    content = content.replace('colorcargo://about', 'about.html')
    content = content.replace('colorcargo://privacy', 'privacy.html')
    # 5. Report Ad custom scheme → mailto with subject + body
    subject = 'ColorCargo — Report an Ad'
    body = (
        "Hi — please describe the ad you'd like to report above. "
        "A screenshot helps if possible. Thanks!"
    )
    subject_enc = quote(subject)
    body_enc = quote(body)
    content = re.sub(
        r'\[Report Ad\]\(colorcargo://report-ad\)',
        f'[Report Ad](mailto:{EMAIL}?subject={subject_enc}&body={body_enc})',
        content,
    )
    # 6. Idempotent: legacy subject-only mailto → subject+body
    content = re.sub(
        r'\(mailto:' + email_re + r'\?subject=ColorCargo%20Ad%20Report\)',
        f'(mailto:{EMAIL}?subject={subject_enc}&body={body_enc})',
        content,
    )
    # 7. Bold-wrapped link **[text](url)** → [text](url)
    content = re.sub(
        r'\*\*(\[[^\]]+\]\([^\)]+\))\*\*',
        r'\1',
        content,
    )
    # 8. Bold-span containing a link (CommonMark flanking — see iOS docs/sync_legal.py)
    content = re.sub(
        r'(?<![A-Za-z0-9])\*\*([^*\n]*\[[^\]]+\]\([^\)]+\)[^*\n]*)\*\*(?![A-Za-z0-9])',
        r'\1',
        content,
    )
    # 9. Version placeholders — pulled from Android app/build.gradle.kts
    content = content.replace('{{VERSION_SHORT}}', version_short)
    content = content.replace('{{VERSION_BUILD}}', version_build)
    return content


def main():
    repo_root = os.path.dirname(os.path.abspath(__file__))
    dest_dir = os.path.join(repo_root, DEST_SUBDIR)
    if not os.path.isdir(dest_dir):
        print(f'⚠️  Destination missing: {dest_dir}', file=sys.stderr)
        return 1
    if not os.path.isdir(ANDROID_SOURCE):
        print(f'⚠️  Android source missing: {ANDROID_SOURCE}', file=sys.stderr)
        return 1
    version_short, version_build = read_android_version()
    print(f'Android version: {version_short} ({version_build})')
    changed = 0
    for name in DOCS:
        src = os.path.join(ANDROID_SOURCE, f'{name}.md')
        dst = os.path.join(dest_dir, f'{name}.md')
        if not os.path.exists(src):
            print(f'⚠️  Source missing: {src}', file=sys.stderr)
            continue
        with open(src) as f:
            new_content = fix_web_links(f.read(), version_short, version_build)
        prev = ''
        if os.path.exists(dst):
            with open(dst) as f:
                prev = f.read()
        if prev == new_content:
            print(f'= {dst}  (unchanged)')
            continue
        with open(dst, 'w') as f:
            f.write(new_content)
        print(f'✓ {src}  →  {dst}')
        changed += 1
    print(f'\n{changed} file(s) changed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
