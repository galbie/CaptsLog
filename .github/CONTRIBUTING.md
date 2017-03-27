# Contributing to CaptsLog

We are test-driven, though we gonna do some switching between test first and test second method.

## How to Git

Follow this guideline:

```
git clone git@github.com:your-user-name/captslog.git captslog-yourname
cd capts-yourname
git remote add upstream git://github.com/jaehoonhwang/captslog.git
```

Create a branch to submit your PR and **make your branch name something relevant**:

```
git branch descriptive-branch-name
git checkout descriptive-branch-name
```

To update the branch use following line:

```
git fetch upstream
git rebase upstream/master
```

**NOTE**: Be descriptive in your commit name.
I don't care about summary, but, in your commit title, it should be summary of what you did.

**Example**:
```
git commit -m "ThingsthatIdid" (NO)
git commit -m "Fixed UI Error and created helper function" (YES)
```

## Source Code

Every source code should be `source/` (It will be change to `captslog/` later)

Create different directories for UI, DB, and call them `tests` files.

### Example of test directory

File directories should look like as this

**Database**
```
source/DB/
    - source/DB/tests
```

**UI**
```
source/UI/
    - source/UI/tests
```

## Submitting PR

Please use following guideline for github.

`[Category] (#Number) Title`

Example: `[Test](#15) Announcements`

**Categories**:
- [Feature]: Any feature we might add
- [Bug]: Bug fixes
- [Test]: Anything test related
- [Doc]: Documentation Related

**Number**:
Issue number referencing the pull request.

**Title**:
Brief Description for what pull request is about.

## Testing Environment

We are going to use `py.test` module.

Read documentations for individual file testing, but in general, it should go something like this

```
pytest /source/path/to/tests/
```

It should be very short and we'll talk about UI testing later

## Travis-CI

If you have any problem with Travis-CI, email me or create github issue.

Every single tests will be tested through following command:

```bash
py.test source/tests/tests.py --pep8 source/tests/ -v --cov source/tests/ --cov-report term-missing
```

## Coveralls

We are shooting for that **85%+** coverage
