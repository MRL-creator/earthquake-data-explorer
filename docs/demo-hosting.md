# Hosting the public demo

The application starts with its bundled 2025 Q1 USGS catalog snapshot. No
API key, credentials, or live catalog request is needed to open the dashboard.

## Streamlit Community Cloud

1. Sign in at https://share.streamlit.io/ and connect the GitHub account.
2. Create an app from `MRL-creator/earthquake-data-explorer`.
3. Select branch `main`, entry point `app.py`, and Python 3.12 under advanced settings.
4. Deploy. The root `requirements.txt` supplies the dependencies; `app.py`
   adds the repository's `src` directory to its import path.
5. Verify the initial view shows **396 events**, **largest reported M 7.7**,
   and the bundled-source label. Raise the minimum magnitude to **6.0**:
   the view should show **22 events** and **0 deep events**.
6. Copy the actual assigned app URL into the README after the deployment is healthy.

The bundled snapshot is static. Live requests still depend on USGS availability,
and a public demo is not a private workspace for sensitive uploaded data.
Avoid adding credentials or personal datasets to the repository or demo.

## Updating and rollback

Community Cloud follows the deployed branch. Verify changes with the offline
test suite before publishing. If an update breaks the demo, revert the specific
Git commit and redeploy; the bundled catalog stays versioned with the code.

Official deployment instructions:
https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
