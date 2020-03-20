def test_proc_insar_isce(script_runner):
    ret = script_runner.run('{{cookiecutter.package_name}}', '-h')
    assert ret.success


def test_proc_insar_isce(script_runner):
    ret = script_runner.run('{{cookiecutter.process_name}}', '-h')
    assert ret.success

