def test_{{cookiecutter.__package_name}}(script_runner):
    ret = script_runner.run('{{cookiecutter.__package_name}}', '-h')
    assert ret.success


def test_{{cookiecutter.__process_name}}(script_runner):
    ret = script_runner.run('{{cookiecutter.__process_name}}', '-h')
    assert ret.success
