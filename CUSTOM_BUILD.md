# Build notes

The GitHub Actions workflow performs these stages:

1. Checks out this custom build configuration.
2. Clones the upstream Android engine at a fixed commit.
3. Applies `.custom/brand.py` with strict one-match checks, so unexpected upstream changes stop the build rather than silently corrupt files.
4. Installs JDK 25, Gradle 8.14, Android platform/build tools 35, and NDK `28.2.13676358`.
5. Installs the Rust Android target using the exact toolchain pinned by upstream's `rust-toolchain.toml`.
6. Runs upstream public-tree checks and Android-related Python tests.
7. Prepares generated Minecraft engine tables using the upstream pinned game metadata.
8. Builds an optimized public ARM64 APK, signs it with an ephemeral development key, and runs the upstream APK payload audit.
9. Uploads the APK, SHA-256 checksum, build information, and license notices as a 30-day GitHub Actions artifact.

The development signing key is generated inside the runner and is not committed. Each run has a separate development version identity; do not expect data to be preserved across differently signed builds.
