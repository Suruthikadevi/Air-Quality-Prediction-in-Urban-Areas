import requests

def download_file(url, file_name):
    """Download a file from a given URL and save it locally."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for HTTP issues

        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"✅ File downloaded successfully: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading file: {e}")

if __name__ == "__main__":
    # Example dataset URL (replace with actual link)
    file_url = "https://example.com/air_quality_data.csv"
    save_as = "air_quality_data.csv"

    download_file(file_url, save_as)
