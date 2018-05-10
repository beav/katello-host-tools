import os
from yum.plugins import TYPE_CORE, TYPE_INTERACTIVE

from katello.repos import upload_enabled_repos_report

from logging import Logger

from katello.enabled_report import EnabledReport
from katello.constants import REPOSITORY_PATH

requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def close_hook(conduit):
    if not conduit.confBool("main", "supress_debug"):
        conduit.info(2, "Uploading Enabled Repositories Report")
    try:
        report = EnabledReport(REPOSITORY_PATH)
        upload_enabled_repos_report(report)
    except:
        if not conduit.confBool("main", "supress_errors"):
            conduit.error(2, "Unable to upload Enabled Repositories Report")
