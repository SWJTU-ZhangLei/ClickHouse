from praktika import Workflow

from ci.jobs.scripts.workflow_hooks.should_skip_job import should_skip_job
from ci.workflows.defs import ARTIFACTS, BASE_BRANCH, SECRETS
from ci.workflows.job_configs import JobConfigs

workflow = Workflow.Config(
    name="MasterCI",
    event=Workflow.Event.PUSH,
    branches=[BASE_BRANCH],
    jobs=[
        *JobConfigs.build_jobs,
        *JobConfigs.unittest_jobs,
        JobConfigs.docker_sever,
        JobConfigs.docker_keeper,
        *JobConfigs.install_check_jobs,
        *JobConfigs.compatibility_test_jobs,
        *JobConfigs.functional_tests_jobs_required,
        *JobConfigs.functional_tests_jobs_non_required,
        *JobConfigs.functional_tests_jobs_azure_master_only,
        *JobConfigs.integration_test_jobs_required,
        *JobConfigs.integration_test_jobs_non_required,
        *JobConfigs.stress_test_jobs,
        *JobConfigs.stress_test_azure_master_jobs,
        *JobConfigs.clickbench_master_jobs,
        *JobConfigs.ast_fuzzer_jobs,
        *JobConfigs.buzz_fuzzer_jobs,
        *JobConfigs.performance_comparison_amd_jobs,
        *JobConfigs.sqlancer_master_jobs,
        JobConfigs.sqltest_master_job,
    ],
    artifacts=ARTIFACTS,
    # dockers=DOCKERS,
    secrets=SECRETS,
    enable_cache=True,
    enable_report=True,
    enable_cidb=True,
    enable_commit_status_on_failure=True,
    pre_hooks=[
        "python3 ./ci/jobs/scripts/workflow_hooks/store_data.py",
        "python3 ./ci/jobs/scripts/workflow_hooks/version_log.py",
    ],
    workflow_filter_hooks=[should_skip_job],
    post_hooks=[],
)

WORKFLOWS = [
    workflow,
]
