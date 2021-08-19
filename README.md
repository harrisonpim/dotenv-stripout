# :see_no_evil: .env stripout

Automagically remove sensitive data from your `.env` files, while maximising collaboration and reproducibility.

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

Many software projects require the inclusion of sensitive data which shouldn't be committed to version control. You don't want Bad Guys to see your usernames, passwords, API keys, etc.

To get around this, many projects require each that collaborator creates a local `.env` file with a list of secret environment variables used in the code. The file is then [gitignored](https://git-scm.com/docs/gitignore) so that the sensitive values never appear on GitHub for malicious users to steal.

However, for well-intentioned new collaborators, the complete absence of a `.env` file means that the required variables for a project are rarely obvious. It's easy for a project's code to fall out of sync with the instructions for creating a `.env`, and not knowing which secrets to provide can be a significant source of friction while trying to get started.

I _want_ to share my `.env` files with my collaborators, but without the secret bits.

Using `dotenv-stripout`, a git filter removes the sensitive values from all of the `.env` files in your repo at the moment they're staged for commit, while keeping the _names_ of the secrets intact (see the [example](#an-example)). The result for your collaborators is an always-up-to-date set of required secrets, in the actual `.env` file where they need to be filled out.

## How?

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

You can check whether the filter is installed by running

```shell
dotenv-stripout status
```

Adding the `--global` flag to any command will point them to your global git config instead, with the installed filter applying to commits in any repo.

You can also use the CLI to strip your actual working `.env` files in the current repo. Just run

```shell
dotenv-stripout
```

## Really?

Nah, probably not... The package works, but using it IRL is probably a bad idea.If nothing else, this little project has been as a good opportunity for me to learn more of the arcane black magic which powers git.

The use of `.env`s and `.gitignore` files is a well established convention at this point, and this stripout approach has just as many potential flaws as a standard, blunt `.gitignore`.

There are also plenty of other common patterns for sharing secrets which already work very well (eg use of [AWS secrets manager](https://aws.amazon.com/secrets-manager/), or environment variable management with providers like [vercel](https://vercel.com/docs/environment-variables) or [netlify](https://docs.netlify.com/configure-builds/environment-variables/)), though making sense of them can be just as tricky for newcomers.
