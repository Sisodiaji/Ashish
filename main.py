import re

def extract_uid(post_url):
    # Facebook post ke URL patterns
    patterns = [
        r"facebook\.com\/([a-zA-Z0-9\.]+)\/posts\/([a-zA-Z0-9]+)",
        r"facebook\.com\/permalink\.php\?story_fbid=([a-zA-Z0-9]+)&id=[a-zA-Z0-9]+",
        r"facebook\.com\/([a-zA-Z0-9\.]+)\/videos\/([a-zA-Z0-9]+)",
        r"facebook\.com\/(?:[a-zA-Z0-9\.]+)\/posts\/([a-zA-Z0-9]+)"
    ]

    post_url = post_url.replace("www.", "").replace("https://", "").replace("http://", "")

    for pattern in patterns:
        match = re.search(pattern, post_url)
        if match:
            # Post ID extract karne ke liye
            if len(match.groups()) > 1:
                return match.group(len(match.groups()))
            else:
                return match.group(1)
    return None

def main():
    print("Facebook Post UID Extractor")
    post_url = input("Post ka link daalo: ")
    uid = extract_uid(post_url)
    if uid:
        print("Post ka UID hai:", uid)
    else:
        print("UID extract nahi ho saka. Kripya sahi link check karein.")

if __name__ == "__main__":
    main()
