# mrjob notes

## external files

- since mrjob *copies* files potentially to many remote hosts, one has to tell mrjob about any and all resources that have to be made available, besides the stdin and stdout expected by hadoop streaming.

- one choice is [add_file_option](https://pythonhosted.org/mrjob/job.html#mrjob.job.MRJob.add_file_option)
    - which will pass a file reference to each job

- [add_file_option](https://pythonhosted.org/mrjob/job.html#mrjob.job.MRJob.add_file_option) suggests passing in a sqlite3dbm as an idiom for an on-disk hash table.

> All dependencies must either be contained within the file, available on the task nodes, or uploaded to the cluster by mrjob when your job is submitted. ([Runners](https://pythonhosted.org/mrjob/guides/runners.html) explains how to do those things.)

> If you need to load some kind of support file, like a sqlite3 database, or perhaps create a temporary file, you can use these methods to do so. (See [File options](https://pythonhosted.org/mrjob/guides/writing-mrjobs.html#writing-file-options) for an example.)

## from writing mrjobs

> See [Making files available to tasks](https://pythonhosted.org/mrjob/guides/configs-all-runners.html#configs-making-files-available) if you want to upload a file to your tasks’ working directories without writing a custom command line option.

> Warning You must wait to read files until after class initialization. That means you should use the [*_init()](https://pythonhosted.org/mrjob/guides/writing-mrjobs.html#single-step-method-names) methods to read files. Trying to read files into class variables will not work.

- [counters example](https://pythonhosted.org/mrjob/guides/writing-mrjobs.html#counters)

## from [Config file format and location](https://pythonhosted.org/mrjob/guides/configs-basics.html#config-file-format-and-location)

## from [Job Environment Setup Cookbook](https://pythonhosted.org/mrjob/guides/setup-cookbook.html)

- [Using a virtualenv](https://pythonhosted.org/mrjob/guides/setup-cookbook.html#using-a-virtualenv)

## from [Hadoop Cookbook](https://pythonhosted.org/mrjob/guides/hadoop-cookbook.html)

- [Writing compressed output](https://pythonhosted.org/mrjob/guides/hadoop-cookbook.html#writing-compressed-output)

## todo

- read mrjob: [defining your job](https://pythonhosted.org/mrjob/job.html#)

## [SECONDARY_SORT](https://pythonhosted.org/mrjob/job.html#secondary-sort)

- sorts by value the data passed into the reducer.

- there is some very useful info in [MRJOB.jobconf](https://pythonhosted.org/mrjob/job.html#mrjob.job.MRJob.jobconf) about passing values into the reducer to have hadoop sort values differently, like being aware of integers, reverse sorting numbers, etc

## examples

- read through all of the examples

### mr_grep

- runs grep via the mapper_cmd interface; calls *nix grep directly passing the match pattern via -e
- would be good to test to see if .gz input is expanded by default.
- Can I run mr_grep directly on the bgp inputs?
