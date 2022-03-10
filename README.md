# :see_no_evil: dotenv-stripout

An easily-installable git filter which hides your projects' sensitive data, while maximising collaboration and reproducibility.

It's like [nbstripout](https://github.com/kynan/nbstripout) for your `.env` files.

Eg. your local `.env` looks like this

```.env
MY_SECRET_USERNAME=something-very-secret
MY_SECRET_PASSWORD=IqLTLrFviwHTDKWGZoR7uB2JtM1wjwE34MBwoztE
```

but your `.env` on GitHub looks like this

```.env
MY_SECRET_USERNAME=
MY_SECRET_PASSWORD=
```

If you want to know more, I've written a [blog post](https://harrisonpim.com/blog/you-should-commit-your-env-files-to-version-control) about how and why I created this package.

## Installation & Use

First, install the python package which does the stripping and manages the git filter.

```shell
pip install dotenv-stripout
```

Then, to install the filter in the current repo, run

```shell
dotenv-stripout install
```

To remove the filter from the current repo, run

```shell
dotenv-stripout uninstall
```

You can check whether the filter is installed in a repo by running

```shell
dotenv-stripout status
```

Adding the `--global` flag to any command will point them to your _global_ git config instead, with the installed filter applying to commits in any repo.

You can also use the CLI to strip your actual working `.env` files in the current repo. Just run

```shell
dotenv-stripout
```
