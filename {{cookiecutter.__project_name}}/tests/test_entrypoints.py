def test_{{cookiecutter.__package_name}}(script_runner):
    ret = script_runner.run('python -m {{cookiecutter.__package_name}}', '-h')
    assert ret.success
