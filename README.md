![Tests](https://github.com/harrisonpim/dotenv-stripout/workflows/test/badge.svg)

# :see_no_evil: .env stripout

Automagically removes sensitive data from your `.env` files, while maximising collaboration and reproducibility.

Loosely inspired by [nbstripout](https://github.com/kynan/nbstripout).

## An example

**Your local `.env`**

```.env
MY_SECRET_USERNAME=something-very-secret
MY_SECRET_PASSWORD=IqLTLrFviwHTDKWGZoR7uB2JtM1wjwE34MBwoztE
```

**Your `.env` on GitHub**

```.env
MY_SECRET_USERNAME=
MY_SECRET_PASSWORD=
```

## Why?

Many software projects require the inclusion of sensitive data which shouldn't be committed to version control.

The usual approach is for each collaborator to create a [gitignored](https://git-scm.com/docs/gitignore) `.env` file in their local copy of a repo with a common set of secret environment variables. 

However, knowing the required variables for a project is not always obvious, and it's all too easy for a project's code to fall out of sync with the instructions for creating the `.env`.

Using `dotenv-stripout` instead, a pre-commit hook removes the sensitive values from your repo's `.env` files as you commit your changes. This way, every named secret in your real environment will automatically be listed for your collaborators in a blank `.env` file - the only thing they'll need to fill in are the values themselves.

## How?

Installing the hook is a two-stage process. First, install the python package which handles the stripping and manages the hook.

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

You can check whether the hook is installed by running

```shell
dotenv-stripout status
```

Adding the `--global` flag to any command will point them to your global git config instead, with the installed hook applying to commits in any repo.

## Really?

Nah, probably not... It works, but using this IRL is probably a bad idea.

The use of `.env` files is a well established convention at this point, and this stripout approach has just as many potential flaws as using a standard, blunt `.gitignore`.

If nothing else, this project might serve as a provocation or reminder of how crap the general state of secret management is. It's also been a good opportunity for me to learn more of the arcane black magic which powers git.
