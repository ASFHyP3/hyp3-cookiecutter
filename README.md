# HyP3 Cookiecutter

Use [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) to quickly 
generate a new HyP3 Plugin.

## Usage

### 0. Create a repository on GitHub

To create a new plugin, you'll first need to create a new repository on [GitHub](https://github.com) where you will contain your plugin.
  
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
cookiecutter git@github.com:ASFHyP3/hyp3-cookiecutter.git
```

Now, you should have a `hyp3-<process>` directory which contains a minimal HyP3
plugin.

### 2. Setup a development environment

We use a `conda`/`mamba` environments to manage our dependencies; you can get Mambaforge
(recommended) here:

https://github.com/conda-forge/miniforge#mambaforge

And you can get Miniconda here:

https://docs.conda.io/en/latest/miniconda.html

Once conda is installed, from the repository root, you can create and activate a
development environment with all the necessary dependencies

```bash
cd hyp3-<process>
conda env create -f conda_env.yml
conda activate hyp3-<process>
``` 

You should now have a development environment with all the required packages for
a generic HyP3 plugin. Later, as dependencies change, you can edit the `environment.yml`
file and then update your environment with

```bash
conda env update -f environment.yml
```

### 3. Push the repository to GitHub

We want to push the local copy we just created to our GitHub repository:

```bash
# From hyp3-<process>
git init .
git remote add origin git@github.com:YOUR-GITHUB-USERNAM-OR-ORG-NAME/hyp3-<process>.git
git add .
git commit -m "Minimal HyP3 plugin created with the hyp3 plugin cookiecutter"
git push -u origin develop
```

And a main (for production releases) branch:

```bash
git checkout -b main
git push -u origin main
```

We also want to create a zeroth production version from this initial commit so that
the plugin's auto-versioning will work correctly.

```bash
git tag -a v0.0.0 -m "Marking zeroth release for auto-versioning and CI/CD Tooling"
git push --tags
```

Now, go back to the development branch:

```bash
git checkout develop
```

### 4. Configure the GitHub repository settings

Once the zeroth release is pushed to GitHub, we need to configure the GitHub repository settings.
The settings detailed here are not required, but we **STRONGLY** recommend them as they make it much
 easier for others to collaborate on your project, and for you to control how the collaboration
occurs.

Go to your repository in GitHub and on the right, click "Settings", then:
1. In "Options" (left):
   * In the "Merge button" section
     * un-click "Allow squash merging"
     * Make sure "Automatically delete head branches" is clicked
2. In "Branches":
   * make sure the default branch is "develop"
   * Add a "Branch protection rule" for:
     * main:
       * set "Branch name pattern" to "main"
       * click "Require pull request review before merging"
       * click "Dismiss stale pull request approvals when new commits are pushed"
       * click "Require status checks to pass before merging"
       * click "Do not allow bypassing of the above settings"
       * click "Restrict who can push to matching branches"
       * Create
     * develop:
       * set "Branch name pattern" to "develop"
       * click "Require pull request review before merging"
       * click "Require status checks to pass before merging"
       * click "Do not allow bypassing of the above settings"
       * Create

For both the `main` and `develop` you can restrict who can push to the branch.
In the same page where you set the above options, you can also click "Restrict
who can push to matching branches", then search and add the desired people/organizations
who are allowed to push.

For more information on how to contribute to repositories set up in this manner,
check out GitHub's [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
article

### 5. Restart the GitHub Actions

Now you're all setup! You should be able to navigate to your repository "Actions",
restart the failed Workflows on `develop`, and watch it create minimal HyP3 plugin 
container for your process. 
