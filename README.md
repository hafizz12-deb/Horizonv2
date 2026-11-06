# Horizon Custom — Android ARM64

This repository is a **custom build layer** for an Android Minecraft Java launcher based on the open-source `Vasysik/horizon-android` engine. It is not a complete reimplementation of Minecraft or a repackaged APK.

## What this project customizes

- App name: **Horizon Custom**
- Dark teal / mint visual theme for the launcher's dark and light appearances
- Android accent color
- A separate development-channel package ID, so this build can be installed alongside a stable upstream app
- Reproducible ARM64 build workflow with source checks, APK signing, payload audit, checksum, and license notices

The build workflow downloads the pinned engine source during GitHub Actions, applies the theme patch, prepares the engine's generated data, and compiles the APK.

## Build the APK

1. Push the contents of this repository to the `main` branch of your GitHub repository.
2. Open the repository's **Actions** tab.
3. Select **Build Horizon Custom (ARM64)**.
4. Select **Run workflow**.
5. Wait for all steps to finish successfully.
6. Open the completed workflow run and download the **Horizon-Custom-ARM64** artifact.
7. Extract the artifact ZIP. Install `Horizon-Custom-arm64-v8a.apk`.

A push changing the build configuration on `main` also triggers the workflow.

## Compatibility

- APK ABI: `arm64-v8a`
- Minimum Android version: Android 9 / API 28
- Minecraft engine version: the version pinned by the selected upstream source commit (currently documented upstream as Minecraft Java 26.3)
- Resource packs and sandboxed `.hmod` features depend on upstream engine support.
- Shader support is GPU/driver dependent and is not guaranteed on every phone.
- Fabric, Forge, and NeoForge Java mods are not supported by this Android engine.
- Native `.hnmod` compilation/loading is not supported on Android.
- Microsoft account integration is not described as production-ready; upstream documents project-owned Microsoft/Mojang registration as pending. Offline use follows upstream behavior.

## Important limitations

- This repository contains the custom patch and build workflow, **not the complete upstream source tree**.
- The workflow compiles the source on GitHub Actions. It has not been run from this handoff package yet, so no successful APK build is claimed.
- A successful CI build proves compilation and packaging checks, not that the APK works on every Android device.
- Physical-device testing is still needed for GPU compatibility, controls, performance, and multiplayer.
- The build is an experimental development-channel APK, not a Play Store release.
- The upstream engine does not bundle Minecraft game assets in the public APK; it downloads required game resources on first setup from official endpoints. Use a legitimate Minecraft Java Edition account for authenticated play.

## Source and licensing

Engine source: https://github.com/Vasysik/horizon-android

Pinned engine commit: `150a414b09a18c900489d9462a7fc035dae744b7`

This project is unofficial and is not affiliated with Mojang or Microsoft. Upstream license and third-party notices are copied into the build artifact.
