import requests

def app_ios(app_id):
    url = f"https://itunes.apple.com/lookup?id={app_id}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if data["resultCount"] == 0:
        raise ValueError(f"No app found for ID {app_id}")

    result = data["results"][0]

    return {
        "title": result.get("trackName", "N/A"),
        "version": result.get("version", "N/A"),
        "category": result.get("primaryGenreName", "N/A"),
        "ratings_count": result.get("userRatingCount", 0),
        "average_rating": result.get("averageUserRating", 0),
        "description": result.get("description", "No description available"),
        "icon": result.get("artworkUrl100", "N/A"),
        "url": result.get("trackViewUrl", f"https://apps.apple.com/app/id{app_id}"),
        "screenshots": result.get("screenshotUrls", [])
    }

# Example usage
app_data = app_ios("6749009478")  # Facebook app ID
print(f"Name: {app_data['title']}")
print(f"Version: {app_data['version']}")
print(f"Category: {app_data['category']}")
print(f"Ratings: {app_data['ratings_count']}")
print(f"Average Rating: {app_data['average_rating']}")
