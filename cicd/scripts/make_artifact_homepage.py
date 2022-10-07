#! /usr/bin/env python3
"""This makes a HTML index file pointing to all generated CI/CD artifacts."""

import datetime
import os
import textwrap


def make_index_html() -> None:
    """Print simple HTML index file to standard out."""
    now_utc = datetime.datetime.utcnow().isoformat()[:-7]

    project_url = os.getenv("CI_PROJECT_URL")
    project_title = os.getenv("CI_PROJECT_TITLE")
    job_id = os.getenv("CI_JOB_ID")
    job_url = os.getenv("CI_JOB_URL")
    pipeline_id = os.getenv("CI_PIPELINE_ID")
    pipeline_url = os.getenv("CI_PIPELINE_URL")

    print(
        textwrap.dedent(
            f"""\
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1,
              shrink-to-fit=no">
        <meta name="description"
              content="Overview of build artifacts from a GitLab pipeline.">
        <meta name="author" content="HERE.com">

        <title>Build Artifacts</title>

        <link rel="canonical"
              href="https://getbootstrap.com/docs/4.0/examples/sticky-footer/">

        <!-- Bootstrap core CSS -->
        <link rel="stylesheet"
              href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
      </head>

      <body>

        <!-- Begin page content -->
        <main role="main" class="container">
          <h1 class="mt-5">GitLab Build Artifacts</h1>
          <p class="lead">
            This is an overview of build artifacts
            for job <a href="{job_url}">{job_id}</a>
            in pipeline <a href="{pipeline_url}">{pipeline_id}</a>
            of project <a href="{project_url}">{project_title}</a>.
          </p>
          <p>
            <ul>
              <li><a href="apiref/index.html">API Reference</a></li>
              <li><a href="htmlcov/index.html">Coverage Report</a></li>
            </ul>
          </p>
        </main>

        <footer class="footer">
          <div class="container">
            <span class="text-muted">Generated on {now_utc} UTC.</span>
          </div>
        </footer>
      </body>
    </html>
    """
        )
    )


if __name__ == "__main__":
    make_index_html()
