def test_{{cookiecutter.package_name}}(script_runner):
    ret = script_runner.run('{{cookiecutter.package_name}}', '-h')
    assert ret.success


def test_{{cookiecutter.process_name}}(script_runner):
    ret = script_runner.run('{{cookiecutter.process_name}}', '-h')
    assert ret.success
