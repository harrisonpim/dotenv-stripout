![Tests](https://github.com/harrisonpim/dotenv-stripout/workflows/test/badge.svg)

# :see_no_evil: .env stripout

Installs a pre-commit hook for removing sensitive data from your projects, while still maximising collaboration and reproducibility.

Loosely inspired by [nbstripout](https://github.com/kynan/nbstripout).

## An example

**What you see on your machine**

```.env
MY_SECRET_USERNAME=something-very-secret
MY_SECRET_PASSWORD=IqLTLrFviwHTDKWGZoR7uB2JtM1wjwE34MBwoztE
```

**What ends up on GitHub**

```.env
MY_SECRET_USERNAME=
MY_SECRET_PASSWORD=
```

## Why?

Many projects require sensitive data which shouldn't be committed to version control.

The usual approach is for each collaborator to create a gitignored `.env` file in their local copy of a repo with a common set of secret environment variables. However, knowing the required variables for a project is not always obvious, and it's all too easy for a project's code to fall out of sync with the instructions for creating the `.env`.

Using `dotenv-stripout` instead, a pre-commit hook removes the sensitive values from your repo's `.env` files when you commit your changes. This way, every named secret in your real environment will automatically be listed for your collaborators in a blank `.env` file - the only thing they'll need to fill in are the values themselves.

## How?

Installing the hook is a two-stage process - first, install the python package which handles the stripping and manages the hook.

```shell
pip install dotenv-stripout
```

Then, to install the hook in the current repo, run

```shell
dotenv-stripout install
```

To remove the hook from the current repo, run

```shell
dotenv-stripout uninstall
```

Add the `--global` flag to the `install` or `uninstall` commands to run the hook in all repos.

## Really?

Nah, probably not...

The use of `.env` files is a well established convention at this point, and this stripout approach has just as many potential flaws as using a standard, blunt `.gitignore`. My implementation here works, on a basic level, but is also likely to contain plenty of holes which might trip you up if using the hook in anger.

If nothing else, this project might serve as a good provocation/reminder about how crap the current state of secret management is, and has provided me an opportunity to learn more about git hooks.
