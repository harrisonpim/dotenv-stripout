# Contributing

Before proceeding, make sure you take a look at the [code of conduct](CODE_OF_CONDUCT.md).

If you notice a bug or want to see a new feature in dotenv-stripout, [create a new issue](https://github.com/harrisonpim/dotenv-stripout/issues/new) describing what's wrong in the current state.

If you can't make the change yourself, that's all you need to do.

If you can make the change, follow the instructions for setting up a local development version of the package and contributing changes.

## Setup

Dotenv-stripout is packaged with [Flit](https://flit.readthedocs.io/en/latest/), and orchestrated with Make.

To install a symlinked version of the package for local development, run

```shell
make setup
```

## Contributing changes

First, create a local feature branch for your change, with a descriptive name.

Make your changes locally, and commit them to your local branch.

When you're satisfied with your implementation of the changes, push your local branch to github and create a new pull request. Write a short description of the fix, and link the PR to the original issue.

When the PR has been discussed and approved, you can merge it into the `main` branch and, if appropriate, release a new version of the package.

### Testing
To run the tests locally, run 
## Releasing new versions

New versions of dotenv-stripout are published to pypi by [a github action](.github/workflows/publish.yml) whenever new a new [release](https://github.com/harrisonpim/dotenv-stripout/releases) is created.

Dotenv-stripout uses [semantic versioning](https://semver.org/).
