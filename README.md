# GitHub Activity Checker

This script fetches and displays the GitHub events of a given user. It shows the number of times the user has performed different actions, such as push requests, pull requests, commits, releases, creates, deletes, and other types of events.

## Features

- Retrieves GitHub events using GitHub's REST API.
- Counts and displays different event types: Push, PullRequest, Commit, Release, Create, Delete, and unknown events.
- Option for verbose output to display detailed event counts.

## Installation

You need Python 3.x and the `requests` library to run this script. If you don't have `requests` installed, you can install it via pip:

```bash
pip install requests
```

## Usage

### Basic Usage
Run the script with the username of the GitHub user whose events you want to track.

```bash
python activity_checker.py -u <username>
```

### Verbose Output
If you want detailed information about each event type, you can enable verbose output by using the `-v` flag.

```bash
python activity_checker.py -u <username> -v
```

### Example

```bash
python activity_checker.py -u octocat -v
```

This will print the count of each event type for the user `octocat` in verbose mode.

## Rate Limiting

GitHub's API has rate limits. If the rate limit is exceeded, the script will automatically wait until the limit is reset before continuing to fetch data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to modify the file as needed!
