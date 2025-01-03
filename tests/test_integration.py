import chatterbotaiai
from .fixtures import prepare_and_teardown  # noqa: F401


def test_agent_builder_job(prepare_and_teardown):
    data = prepare_and_teardown

    jobs = chatterbotai.AgentBuilderJob.list(agent_id=data["agent_id"])
    assert jobs.total_count == 1
    assert jobs.results[0].id == data["agent_builder_job_id"]

    job = chatterbotai.AgentBuilderJob.retrieve(data["agent_builder_job_id"])
    assert job.id == data["agent_builder_job_id"]


def test_build(prepare_and_teardown):
    data = prepare_and_teardown

    builds = chatterbotai.Build.list(agent_builder_job_id=data["agent_builder_job_id"])
    assert builds.total_count == 1
    assert builds.results[0].id == data["build_id"]

    build = chatterbotai.Build.retrieve(data["build_id"])
    assert build.id == data["build_id"]


def test_execution(prepare_and_teardown):
    data = prepare_and_teardown

    executions = chatterbotai.Execution.list(agent_id=data["agent_id"])
    assert len(executions.results) == 1
    assert executions.results[0].id == data["execution_id"]

    execution = chatterbotai.Execution.retrieve(data["execution_id"])
    assert execution.id == data["execution_id"]


def test_agent_executor_job(prepare_and_teardown):
    data = prepare_and_teardown

    chatterbotai.AgentExecutorJob.create(agent_id=data["agent_id"], payload={"foo": "bar"})

    jobs = chatterbotai.AgentExecutorJob.list(agent_id=data["agent_id"])
    assert len(jobs.results) == 2

    job = chatterbotai.AgentExecutorJob.retrieve(data["agent_executor_job_id"])
    assert job.id == data["agent_executor_job_id"]


def test_agent(prepare_and_teardown):
    data = prepare_and_teardown

    agent = chatterbotai.Agent.create(
        name="testagent2",
        script="def main():\n    print('hello world')\n",
        requirements="requests",
        env_vars="FOO=BAR",
        python_version="3.9",
    )
    assert chatterbotai.Agent.update(agent.id, name="updated").name == "updated"
    assert chatterbotai.Agent.list().total_count == 2
    assert chatterbotai.Agent.retrieve(agent.id).id == agent.id
    chatterbotai.Agent.delete(agent.id)
    assert chatterbotai.Agent.list().total_count == 1


def test_execute_agent(prepare_and_teardown):
    data = prepare_and_teardown

    agent = chatterbotai.Agent.retrieve(data["agent_id"])

    execution = agent.execute()
    assert type(execution) is chatterbotai.Execution

    agent_executor_job = agent.execute(wait=False)
    assert type(agent_executor_job) is chatterbotai.AgentExecutorJob
