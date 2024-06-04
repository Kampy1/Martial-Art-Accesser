import requests

MA_list = "https://en.wikipedia.org/wiki/List_of_Japanese_martial_arts"

def fetch_data(option):
    result = []
    url = f"https://en.wikipedia.org/wiki/{option}"

    while len(result) < count:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            result.extend(data["results"])

            url = data["next"]

        except requests.HTTPError as e:
            print(f"Error fetching data {e}")
            return None
        if url == None:
            break    
    
    print(f"Martial Arts Found: {len(result)}")
    for art in result:
        return result[:count]

count = int(input("How many entities would you like to see? "))

print("what Martial Art would you like to learn about?")
Martial_Art = input()

result = fetch_data(Martial_Art)

if result:
    for art in result:
        print(art["name"])
else:
    print("Unable to download data")