from bs4 import BeautifulSoup
import requests


def main():
    session = requests.session()
    url = "https://rockprivet.ru/muzyika.html"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(
        response.content,
        "lxml"
    )
    audios = soup.find_all("audio")

    print(f"Find {len(audios)} songs at site")

    for i, audio in enumerate(audios, 1):
        src: str = audio.get("src")
        name = src.split("/")[-1]
        with open(f"./songs/{name}", "wb") as file:
            print(f"Download song #{i} - {name}")
            link = f"https://rockprivet.ru{src}"
            audio_response = session.get(link, headers=headers)
            file.write(audio_response.content)


if __name__ == '__main__':
    main()
