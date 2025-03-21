import requests
import argparse
import time

def verbose_check(verbose, username, pushEvent, pullRequestEvent, commitEvent, releaseEvent, createEvent, deleteEvent, unknownEvent):
    if verbose:
        print(f"{username} issued a push request {pushEvent} times")
        print(f"{username} issued a pull request {pullRequestEvent} times")
        print(f"{username} issued a commit {commitEvent} times")
        print(f"{username} issued a release {releaseEvent} times")
        print(f"{username} issued a create event {createEvent} times")
        print(f"{username} issued a delete event {deleteEvent} times")
        print(f"{username} issued an unknown event {unknownEvent} times")
    else:
        print(f"PushEvent: {pushEvent}")
        print(f"PullRequestEvent: {pullRequestEvent}")
        print(f"CommitEvent: {commitEvent}")
        print(f"ReleaseEvent: {releaseEvent}")
        print(f"CreateEvent: {createEvent}")
        print(f"DeleteEvent: {deleteEvent}")
        print(f"UnknownEvent: {unknownEvent}")

def check_rate_limit(headers):
    remaining = int(headers.get('X-RateLimit-Remaining', 1))
    reset_time = int(headers.get('X-RateLimit-Reset', time.time()))

    if remaining == 0:
        # If no requests are remaining, wait until the reset time
        wait_time = reset_time - time.time()
        if wait_time > 0:
            print(f"Rate limit exceeded. Sleeping for {wait_time} seconds.")
            time.sleep(wait_time)
    return remaining

def event_types(username, verbose):
    push_event = 0
    pull_request_event = 0
    commit_event = 0
    release_event = 0
    create_event = 0
    delete_event = 0
    unknown_event = 0

    url = f"https://api.github.com/users/{username}/events"

    response = requests.get(url)
    if response.status_code == 200:
        events = response.json()
        for event in events:
            event_type = event["type"]
            match event_type:
                case "PushEvent":
                    push_event += 1
                case "PullRequestEvent":
                    pull_request_event += 1
                case "CommitEvent":
                    commit_event += 1
                case "ReleaseEvent":
                    release_event += 1
                case "CreateEvent":
                    create_event += 1
                case "DeleteEvent":
                    delete_event += 1
                case _:
                    unknown_event += 1
        verbose_check(verbose, username, push_event, pull_request_event, commit_event, release_event, create_event, delete_event, unknown_event)
    else:
        print(f"Error: Received status code {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Get the activity of a GitHub user")

    parser.add_argument("-u", help="The GitHub username", type=str)
    parser.add_argument("-v", action="store_true", help="Print verbose output")

    args = parser.parse_args()

    event_types(args.u, args.v)

if __name__ == "__main__":
    main()
