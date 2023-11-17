import re

def detectar_handles(texto):

    user = re.findall(r"@\w+", texto)
    hashtag = re.findall(r"#\w+", texto)
    url = re.findall(r"www\.[a-zA-Z0-9]+\.[a-z]+|https://[a-zA-Z0-9]+\.[a-z]+|http://[a-zA-Z0-9]+\.[a-z]+", texto)

    dict = {
        "user": user,
        "hashtag": hashtag,
        "url": url
    }
    return dict

print(detectar_handles("En esta actividad de @mouredev, resolvemos #retos de #programacion desde https://retosdeprogramacion.com/semanales2022, que @braismoure aloja en www.github.com"))





