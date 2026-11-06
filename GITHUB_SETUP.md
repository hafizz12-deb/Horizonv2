# Push this package to your GitHub repository

1. Download and extract `Horizon-Custom-Project.zip`.
2. Open your repository: `https://github.com/hafizz12-deb/Horizon-Android-Custom.-`
3. Upload the **contents inside the extracted folder**, not the outer folder itself.
4. Keep the folder structure exactly as shown:
   - `.github/workflows/android-arm64.yml`
   - `.custom/brand.py`
   - `README.md`
   - `CUSTOM_BUILD.md`
   - `GITHUB_SETUP.md`
   - `.gitignore`
5. Commit the files to the `main` branch.
6. Open **Actions** and run **Build Horizon Custom (ARM64)**.

If the Actions tab is disabled, enable GitHub Actions for the repository. The workflow requests only `contents: read`; it does not need a repository write token or secrets.

## If the build fails

Open the failed run, expand the first red step, and copy its error text. Common causes include an upstream source change, Android SDK package availability, or a temporary dependency download failure. Do not rename upstream files to force the patch through; the patch intentionally stops if the expected source layout has changed.
