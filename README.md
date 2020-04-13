# cookiecutter-hyp3plugin

Use [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) to quickly 
generate a new HyP3 Plugin

## Usage

### 0. Create a project on GitLab

To create a new plugin, you'll first need to create a new HyP3 project in ASF's
GitLab:

* https://scm.asf.alaska.edu/projects/new?namespace_id=56
  
You should enter a project slug like `hyp3-<process>` where `<process>` is the 
short name of your process (e.g., `hyp3-insar-isce`), write a short (1 sentence)
description of the plugin (e.g., `HyP3 plugin for <process> processing`) set the 
visibility to "Internal", and *do not* click the "Initialize repository with a 
README" box. 

### 1. Setup a project environment

From a terminal on your local development machine, create a project environment 
with [conda](https://docs.conda.io/en/latest/miniconda.html):

```bash
conda create -c conda-forge -n "hyp3-<process>" python=3.7 boto3 gdal imageio \ 
    importlib_metadata lxml matplotlib netCDF4 numpy pillow proj psycopg2 pyshp \
    pytest pytest-console-scripts pytest-cov requests scipy setuptools six \
    statsmodels wheel
``` 

And `pip` install a couple of packages unavailable on conda into the environment:
```bash
python3 -m pip install cookiecutter s3pypi setuptools-scm[toml]
```

You should now have a development environment with all the required packages for
a generic HyP3 plugin

### 2. Create the plugin with Cookiecutter

Now that we have a development environment, we can create the plugin. Again, 
from a terminal on your local development machine, navigate to where you'd like 
to create the project. Then run cookiecutter and follow the prompts:

```bash
cookiecutter git@scm.asf.alaska.edu:hyp3/cookiecutter-hyp3plugin.git
```

Now, you should have a `hyp3-<project>` directory which contains a minimal HyP3
plugin.

### 3. Upload the project to GitLab

Now, we want to add the project we just created to our GitLab repository:

```bash
cd "hyp3-<plugin>"
git init .
git remote add origin git@scm.asf.alaska.edu:hyp3/hyp3-<plugin>.git
git add .
git commit -m "Minimal HyP3 plugin created with the hyp3plugin cookiecutter"
git push -u origin master
```

We also want to create a zeroth production version from this initial commit so 
our the plugin's auto-versioning will work correctly.

```bash
git tag -a v0.0.0 -m "Marking zeroth release for auto-versioning and CI/CD Tooling"
git push --tags
```

And a development branch:

```bash
git checkout -b develop
git push -u origin develop
```

### 4. Configure the GitLab project settings

Once your project is created, we need to set some of the Gitlab repository settings. 
Go to your project in Gitlab and:
1. On the left, click "Settings" and then the sub item "Repository"
   * In the "Default Branch" section, change the default branch to `develop` and 
     save changes
   * In the "Protected Branches" section, protect both `master` and `develop` 
     with these settings:
     * `master`
       * Allowed to merge: Maintainers
       * Allowed to push: No one
     * `develop`
       * Allowed to merge: Developers + Maintainers
       * Allowed to push: Maintainers
   * In the "Portected Tags" section, create a `v*` wildcard with "Allowed to create:
     Maintainers" permissions
2. On the left side, click the "CI / CD" settings sub item
   * In the "General Pilelines" section, find the "Test coverage parsing" box and
     copy the regex for "pytest-cov (Python)" into the box and save changes

### 5. Configure the AWS ECR repository

And finally, create a docker repository for your project in the `hyp3-full-access` account:
   ```bash
   # Assuming your aws cli is setup to use the hyp3-full-access profile
   aws ecr create-repository \
       --repository-name hyp3-<project> \
       --image-scanning-configuration scanOnPush=false \
       --region us-east-1
   ```

### 6. Restart the development pipeline

Now you're all setup and you should be ble to navigate to your project in GitLab
and restart the development pipeline and watch it create a demo HyP3 plugin container. 
On the left side, click "CI / CD" and then restart the pipeline that came from the 
`develop` branch if it had failed (if you're fast at doing all the above, it may not!). 
