# cookiecutter-hyp3plugin

Use [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) to quickly 
generate a new HyP3 Plugin

## Usage

### 0. Create a repository on GitHub

To create a new plugin, you'll first need to create a new HyP3 repository in ASF's
GitHub:

* https://github.com/organizations/asfadmin/repositories/new

*Note: If you don't have repo create permissions in the `asfadmin` org, ask the 
 APD/Tools team to create you a repo! 
  
You should enter a repository name like `hyp3-<process>` where `<process>` is the 
short name of your process (e.g., `hyp3-insar-isce`), write a short (1 sentence)
description of the plugin (e.g., `HyP3 plugin for <process> processing`) set the 
repository to "Public", and *do not* click the "Initialize repository with a 
README" box (or add a `.gitignore` or add a license). 


### 1. Create the plugin with Cookiecutter

From a terminal on your local development machine, navigate to where you'd like 
to create the local copy of the plugin's repository. Then run cookiecutter and 
follow the prompts:

```bash
python3 -m pip install cookiecutter
cookiecutter git@scm.asf.alaska.edu:hyp3/cookiecutter-hyp3plugin.git
```

Now, you should have a `hyp3-<process>` directory which contains a minimal HyP3
plugin.


### 2. Setup a development environment

You can, create a development environment with [conda](https://docs.conda.io/en/latest/miniconda.html):

```bash
cd hyp3-<process>
conda env create -f conda_env.yaml
``` 

You should now have a development environment with all the required packages for
a generic HyP3 plugin


### 3. Push the repository to GitHub

We want to push the local copy we just created to our GitHub repository:

```bash
# From hyp3-<process>
git init .
git remote add origin git@github.com:asfadmin/hyp3-<process>.git
git add .
git commit -m "Minimal HyP3 plugin created with the hyp3plugin cookiecutter"
git push -u origin develop
```

And a master (for production releases) branch:

```bash
git checkout -b master
git push -u origin master
```

We also want to create a zeroth production version from this initial commit so 
our the plugin's auto-versioning will work correctly.

```bash
git tag -a v0.0.0 -m "Marking zeroth release for auto-versioning and CI/CD Tooling"
git push --tags
```

And go back to the development branch:

```bash
git checkout develop
```


### 4. Configure the AWS ECR repository

Create a docker repository for your plugin in the `hyp3-full-access` account:
   ```bash
   # Assuming your aws cli is setup to use the hyp3-full-access profile
   aws ecr create-repository \
       --repository-name hyp3-<process> \
       --image-scanning-configuration scanOnPush=false \
       --region us-east-1
   ```


### 5. Configure the GitHub repository settings

Once the zeroth release is pushed to GitHub, we need to configure the GitHub repository settings. 

Go to your repository in GitHub and on the right, click "Settings", then:
1. In "Options" (left):
   * In the "Features" section, un-click "Wikis"
   * In the "Merge button" section
     * un-click "Allow squash merging"
     * Make sure "Automatically delete head branches" is clicked
2. In "Manage access":
   * click "Invite teams or people" and: 
     * add "asfadmin/tools-admin" with the "Admin" role
     * add "asfadmin/engineering" with the "write" role
3. In "Branches":
   * make sure the default branch is "develop"
   * Add a "Branch protection rule" for:
     * master:
       * set "Branch name pattern" to "master"
       * click "Require pull request review before merging"
       * click "Dismiss stale pull request approvals when new commits are pushed"
       * click "Require status checks to pass before merging"
       * click "Restrict who can push to matching branches"
         * add "asfadmin/tools-admin" to who can push
       * Create
     * develop:
       * set "Branch name pattern" to "develop"
       * click "Require pull request review before merging"
       * click "Dismiss stale pull request approvals when new commits are pushed"
       * click "Require status checks to pass before merging"
       * click "Restrict who can push to matching branches"
         * add "asfadmin/tools-admin" to who can push
       * Create
4. In "Secrets":
   * Add `AWS_ACCESS_KEY_ID` for the AWS "tools-bot" role
   * Add `AWS_SECRET_ACCESS_KEY` for the AWS "tools-bot" role
   * Add `TOOLS_BOT_PAK` with the GitHub @tools-bot personal access key

### labels! ... 

Make sure these labels exist, or add them to the repository: 

* major -- Bump the major version number of this project -- f981a1
* minor -- Bump the minor version number of this project -- fca6af
* patch -- Bump the patch version number of this project -- f7e4e5
* bumpless -- Changes to documentation, CI/CD pipelines, etc that don't affect the software's version -- b5b5b5
* CI/CD -- Changes to CI/CD strategy -- 5e92db
* tools-bot -- PRs and Issues opened by the Tools Bot -- fbca04


### 6. Add the GitHub repository to codefactor.io

Navigate to https://www.codefactor.io/repository/new and, when logged in as `asfadmin` 
(if you don't have permissions, get whoever created the repo to do this step):
* Search for your github repository `asfadmin/hyp3-<process>` and "Import" it
* In the left menu, click on repository and then navigate to "Settings" in the upper left
  * Make sure these tools are on:
    * Yamllint
    * Hadolint
    * Pylint
    * Bandit
    * Duplication checker 
  * Navigate to "active branches" at the top and make sure these branches are "on":
    * develop
    * master

### 7. Restart the GitHub Actions

Now you're all setup and you should be able to navigate to your repository "Actions",
restart the failed Workflows on `develop`, and watch it create minimal HyP3 plugin 
container for your process. 
