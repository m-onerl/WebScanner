import requests

def process_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("This page is avilable:", response.url)
        return url
    else:
        print(f"This page", response.url, "sent a failed request with status code",{response.status_code})
        return None

def main():
    working_urls = []
    input_file = "C:\\Users\\moner\\Desktop\\praca\\Linki.txt"
    output_file = "C:\\Users\\moner\\Desktop\\praca\\response.txt"

    with open(input_file, "r", encoding="utf-8") as file:
        urls = file.readlines()
 
    for url in urls:
        url = url.strip()
        working_url = process_response(url)
        if working_url:
            working_urls.append(working_url)

    with open(output_file, "w", encoding="utf-8") as file:
        print("Działające linki:")
        for url in working_urls:
            file.write(url + "\n")

if __name__ == "__main__":
    main()