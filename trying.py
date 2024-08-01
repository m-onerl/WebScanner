import requests



def Checkingurl(page):
    page = requests.get(page)
    if  page.status_code == 200:
        print("This page is working", page.url)
        return page.url
    else:
        print("This page is not working", page.url, "and droped this error status:", page.status_code)
        return None
    
def main():
    workingurls = []
    inputFile = "C:\\Users\\moner\\Desktop\\praca\\Linki.txt"
    outputFile = "C:\\Users\\moner\\Desktop\\praca\\Działające.txt"

    with open(inputFile, "r", encoding = "utf-8") as file:
        urls = file.readlines()

        for url in urls:
            url = url.strip()
            workingurl = Checkingurl(url)
            if workingurl:
                workingurls.append(workingurl)

    with open(outputFile, "w", encoding = "utf-8") as file:
        for url in workingurls:
            file.write(url + "\n")

if __name__ == "__main__":
    main()




