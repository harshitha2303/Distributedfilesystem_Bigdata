# EC-Team-56-Yet Another Distributed File System (YADFS)

## Introduction
This project is done as a part of the course requirements of the Big Data course (UE21CS343AB2) at PES University, Bengaluru. It possesses the capability to replicate data across numerous nodes, monitor file metadata and execute operations within the file system.

The Distributed File Storage System is a high-performance and fault-tolerant solution designed to efficiently store and manage large volumes of data across multiple machines. This system employs a distributed architecture consisting of two key components: Data Nodes and Name Nodes.

# How to run YADFS
## Setting up YADFS
1. Install the dependencies.
   ```
   pip3 install -r requirements.txt
   ```
2. Setup the Distributed File System. The sample configuration to setup a distributed file system is provided in the `config_sample.json` file.

   Example:
    ```
    python3 setup.py --CONFIG config_sample.json --CLEANUP True
    ```
4. Running the `setup.py` script will generate a configuration file to load the distributed file system from. A sample one is provided in `dfs_setup.json`. Run the CLI to access the distributed file system.
   Example
   ```
   python3 dfs_team56.py --CONFIG dfs_setup.json
   ```

## Features
1. ### `ls`

List all the files and folders in a directory in the distributed file system.

```
usage: ls DIR_NAME [-r RECURSIVE]
```

2. ### `put`

Move a file to the distributed file system.

```
usage: put SOURCE_FILE_IN_LOCAL DESTINATION_FILE_IN_DFS
```

3. ### `get`

Download a file from the distributed file system.

```
usage: put SOURCE_FILE_IN_DFS DESTINATION_FILE_IN_LOCAL
```

4. ### `cat`

View the contents of a file in the distributed file system.

```
usage: cat FILE_NAME
```

5. ### `mkdir`

Create a directory in the distributed file system.

```
usage: mkdir DIR_NAME
```

6. ### `rm`

Remove a file from the distributed file system.

```
usage: rm FILE_NAME
```

7. ### `rmdir`

Remove a directory recursively from a distributed file system.

```
usage: rmdir DIR_NAME
```

8. ### `move`

Move a file from one directory to another in the distributed file system.

```
usage: mv SOURCE_DIR DESTINATION_DIR
```

9. ### `format`

Formats contents of the namenode and datanode

```bash
usage: format
```
