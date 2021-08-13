# :see_no_evil: .env stripout

A pre-commit hook for removing sensitive data from your projects, while still maximising collaboration and reproducibility.

Loosely inspired by [nbstripout](https://github.com/kynan/nbstripout).

## Why?

Many projects require sensitive data which shouldn't be committed to version control.

The usual approach is for each collaborator to create a gitignored `.env` file in their local copy of the repo with a common set of secret environment variables. However, knowing the required variables for a project is not always obvious, and instructions for creating them often fall out of sync with the code itself.

`dotenv-stripout` removes the sensitive parts of your repo's `.env` files when you commit your changes, while leaving the variable names for collaborators to complete.

No more writing dotenv documentation. Everything you're working with IRL will be listed for your collaborators in a blank `.env` file - the only thing they'll need are the values themselves.

For example:

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

## How?

Run

```shell
pip install dotenv-stripout
```

