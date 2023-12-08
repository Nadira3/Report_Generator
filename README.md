# Report Generator Console Documentation
In this repository, you'll find the core of a Report Generator. This console application serves as the foundational step towards the development of a comprehensive web application. It operates without a visual interface and incorporates an initial Store Engine.

<div align="center"><img src="framework.png" width="600px"/></div>
The Report Generator Console provides a command-line interface (CLI) for manipulating data stored in a structured manner. It includes classes such as Patient, Complaint, History, and Review.

<div align="center"><img src="console.png" width="600px"/></div>

## Table of Contents

1. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Launching the Console](#launching-the-console)
2. [Available Commands](#available-commands)
   - [Creating Instances](#creating-instances)
   - [Displaying Instances](#displaying-instances)
   - [Deleting Instances](#deleting-instances)
   - [Listing Instances](#listing-instances)
   - [Updating Instances](#updating-instances)
   - [Counting Instances](#counting-instances)
   - [Exiting the Console](#exiting-the-console)
3. [Usage Examples](#usage-examples)
4. [Additional Notes](#additional-notes)

## Getting Started

### Installation

To use the Report_Generator, you need to have Python 3 installed on your system. Follow these steps to set up the environment:

1. Clone the HBNB repository:

   ```sh
   git clone https://github.com/Nadira3/Report_Generator.git
   cd Report_Generator
   ```
2. Install the following modules
    ```sh
    pip install termcolor
    pip install prettytable
    pip install colorama
    ```
3. Place the provided `console.py` file into the root directory of the project.

### Launching the Console

1. Open a terminal window.

2. Navigate to the directory where the `console.py` file is located.

3. Run the following command to start the Report_Generator:

   ```sh
   python3 console.py
   ```

   This will launch the Report_Generator, and you'll see the prompt indicating that the console is ready to accept commands.

## Available Commands

### Creating Instances

- `create <classname>`: Create a new instance of the specified class and generate a unique ID for it.
  Example:

  ```
  =>  create Patient
  05706e96-7951-431d-a5ce-2603b9bae47d
  ```

### Displaying Instances

- `show <classname> <instance_id>`: Display detailed information about a specific instance based on the class name and instance ID.
  Example:

  ```
  =>  show Patient 05706e96-7951-431d-a5ce-2603b9bae47d
  [Patient] (05706e96-7951-431d-a5ce-2603b9bae47d) {'id': '05706e96-7951-431d-a5ce-2603b9bae47d', 'created_at': datetime.datetime(2023, 8, 17, 0, 0), 'updated_at': datetime.datetime(2023, 8, 17, 0, 0)}
  ```

### Deleting Instances

- `destroy <classname> <instance_id>`: Delete a specific instance based on the class name and instance ID.
  Example:

  ```
  =>  destroy Patient 05706e96-7951-431d-a5ce-2603b9bae47d
  ```

### Listing Instances

- `all` or `all <classname>`: List all instances or all instances of a specific class.
  Example:

  ```
  =>  all
  [Patient] (05706e96-7951-431d-a5ce-2603b9bae47d) {'id': '05706e96-7951-431d-a5ce-2603b9bae47d', 'created_at': datetime.datetime(2023, 8, 17, 0, 0), 'updated_at': datetime.datetime(2023, 8, 17, 0, 0)}
  [Complaint] (f176d9ad-9bc7-4dd6-aa14-df50e0ab6b3f) {'id': 'f176d9ad-9bc7-4dd6-aa14-df50e0ab6b3f', 'created_at': datetime.datetime(2023, 8, 17, 0, 0), 'updated_at': datetime.datetime(2023, 8, 17, 0, 0)}
  ...
  ```

### Updating Instances

- `update <classname> <instance_id> <attribute_name> <attribute_value>`: Update the attributes of a specific instance.
  Example:

  ```
  =>  update Patient 05706e96-7951-431d-a5ce-2603b9bae47d first_name "John"
  =>  show Patient 05706e96-7951-431d-a5ce-2603b9bae47d
  [Patient] (05706e96-7951-431d-a5ce-2603b9bae47d) {'id': '05706e96-7951-431d-a5ce-2603b9bae47d', 'created_at': datetime.datetime(2023, 8, 17, 0, 0), 'updated_at': datetime.datetime(2023, 8, 17, 0, 0), 'first_name': 'John'}
  ```

### Counting Instances

- `count <classname>`: Count the number of instances of a specific class.
  Example:

  ```
  =>  count Patient
  3
  ```

### Exiting the Console

- `quit`: Exit the Report_Generator.
  Example:

  ```
  =>  quit
  ```

## Usage Examples

Here are some examples of how to use the Report_Generator:

1. Creating a new Patient instance:

   ```
   =>  create Patient
   ```

2. Displaying information about a Patient instance:

   ```
   =>  show Patient 05706e96-7951-431d-a5ce-2603b9bae47d
   ```

3. Updating the attributes of a Patient instance:

   ```
   =>  update Patient 05706e96-7951-431d-a5ce-2603b9bae47d first_name "John"
   ```

4. Listing all instances:

   ```
   =>  all
   ```

5. Counting instances of a specific class:

   ```
   =>  count Patient
   ```

6. Exiting the Report_Generator:

   ```
   =>  quit
   ```

## Additional Notes

- If you're using a script or a non-interactive environment, you can pass commands directly to the console using the `-c` flag:

  ```sh
  python3 console.py -c "create Patient"
  ```

- The Report_Generator provides auto-completion and command history functionality, making it easier to navigate and use.

- Make sure to follow the correct syntax for each command. Improperly formatted commands may

result in errors or unexpected behavior.

- This documentation provides a basic overview of the Report_Generator and its commands. For more detailed information and advanced usage, refer to the source code and comments in the `console.py` file.
