# `carefree-cli`

**Usage**:

```console
$ cfi [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `add`: Add a new template.
* `delete`: Delete a template.
* `export`: Export templates to a (`cfi`) file.
* `import`: Import templates from a (`cfi`) file.
* `init`: Initialize your project.
* `list`: List your templates.
* `load`: Load a template.
* `update`: Update a template.

## `cfi add`

Add a new template.

**Usage**:

```console
$ cfi add [OPTIONS] TEMPLATE HIERARCHY
```

**Arguments**:

* `TEMPLATE`: The `cli` command template, there are two common formats:

  * plain command, i.e. the direct command to run.

  * placeholder template, which is a string with some '{}'s, and you canspecify the values of these '{}'s later in the `load` command.

> you can (and it is recommended) to provide a 'name' for each '{}' inthe placeholder template, so identify them in `load` will be easier.

> for example, 'echo {msg}' is preferred over 'echo {}'.

> be aware that the 'name' should be 'formattable', i.e. it should be able to pass to `str.format`.  [required]
* `HIERARCHY`: Hierarchy of the template, use '/' to separate levels, and:

  * at least 1 level should be provided.

  * it is recommended to use at most 2 levels.

  * the last level will be used as the template name.  [required]

**Options**:

* `--verbose / --no-verbose`: [default: verbose]
* `--help`: Show this message and exit.

## `cfi delete`

Delete a template.

**Usage**:

```console
$ cfi delete [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `cfi export`

Export templates to a (`cfi`) file.

**Usage**:

```console
$ cfi export [OPTIONS] [TARGET]
```

**Arguments**:

* `[TARGET]`: Path to export the templates to. It is recommended to use a '.cfi' file extension.  [default: templates.cfi]

**Options**:

* `--help`: Show this message and exit.

## `cfi import`

Import templates from a (`cfi`) file.

**Usage**:

```console
$ cfi import [OPTIONS] FILE
```

**Arguments**:

* `FILE`: Path of the file to import the templates from.

  [required]

**Options**:

* `--help`: Show this message and exit.

## `cfi init`

Initialize your project.

**Usage**:

```console
$ cfi init [OPTIONS]
```

**Options**:

* `-d, --data_dir TEXT`: Directory to store your templates.
* `--help`: Show this message and exit.

## `cfi list`

List your templates.

**Usage**:

```console
$ cfi list [OPTIONS] [HIERARCHY]
```

**Arguments**:

* `[HIERARCHY]`: Hierarchy of the template to list, use '/' to separate levels.

  * 'level1/level2' will list all templates under 'level1 -> level2'.

  * `None` will list all existing templates.



**Options**:

* `--help`: Show this message and exit.

## `cfi load`

Load a template.

**Usage**:

```console
$ cfi load [OPTIONS] HIERARCHY
```

**Arguments**:

* `HIERARCHY`: Hierarchy of the template, use '/' to separate levels, and:

  * at least 1 level should be provided.

  * it is recommended to use at most 2 levels.

  * the last level will be used as the template name.  [required]

**Options**:

* `--run / --dry`: Whether to run the command (with `subprocess.run`) or just print it.  [default: run]
* `--help`: Show this message and exit.

## `cfi update`

Update a template.

**Usage**:

```console
$ cfi update [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
