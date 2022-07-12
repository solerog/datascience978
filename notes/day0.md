# Day 0 - Setup & git basics

## Lecture

### Git

```sh
git init
```

Starts a local git repository on the current folder

```sh
gh repo create
```

Creates a repository on GitHub. Can be an existing or a new one.

```sh
git clone git@github.com:solerog/dotfiles.git
```

This clones data into a new folder `dotfiles` created in the folder it was executed.

```sh
 git status
 gst
```

gives the status of the current local repository.

```sh
git diff
```

compares changes between the current repository and the original one.

```sh
git add .
```

Adds (stages) all the files that are ready to be commited. You can specify a certain file or folder instead of `.`

```sh
git commit -m 'Commit message'
```

Commits the added (staged) files or folders in the step above so they can be pushed (stored as valid).

```sh
git push origin master
```

Forward commited files to GitHub. Files and commit messages can be seen in `https://github.com/username/reponame.git`

```sh
git log
```

Shows all commit history in the terminal.

### Challenges

Write code in VS Code.
Do `make` after finishing the code to test if it works AND the **style**
There can be non explained restrictions in the instructions that are checked in tests.
After a push has been made, the mark for the assignment appears in _Kitt_

If you're stuck, you can raise a ticket through _Kitt_.

### Flashcards

They are questions about the lectures of the day.
They don't take long, you have to answer correctly all of them being honest.
