import requests

url = "https://ls.johannespour.de/"

class Linker:
    def __init__(self, link: str, short: str, token: str) -> None:
        self.__link = link
        self.__short = short
        self.__token = token

    def __str__(self) -> str:
        if len(self.__short) == 0:
            return "empty"
        
        return f"{url}{self.__short}"

    def __repr__(self) -> str:
        return f"<link: {self.__link}>"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Linker):
            return (self.__link == o.link and
                    self.__short == o.short and
                    self.__token == o.token)

        return False

    @property
    def link(self):
        return self.__link

    @property
    def short(self):
        return self.__short

    @property
    def token(self):
        return self.__token

    @staticmethod
    def create(link: str):
        """
        Create a new Linker object

        Required args:
            str link: The link you want to get redirected to

        returns a Linker object
        """
        res = requests.post(f"{url}create", json={
            "link": link
        }).json()
        
        short = res["short"]

        try:
            token = res["token"]
        except KeyError:
            token = ""

        return Linker(
            link = link,
            short = short,
            token = token
        )

    def edit(self, new_link: str) -> None:
        """
        Change the destination of the shortcut

        Required args:
            str new_link: The new destination of the shortcut 
        """
        requests.put(url, json={
            "short": self.__short,
            "token": self.__token,
            "link": new_link
        })

        self.__link = new_link

    def delete(self) -> None:
        """
        Delete this shortcut
        """
        requests.delete(url, json={
            "short": self.__short,
            "token": self.__token
        })

        self.__link = ""
        self.__short = ""
        self.__token = ""

    def update(self) -> None:
        """
        Update the destination link if it was changed somewhere else
        """
        resp = requests.get(f"{url}{self.__short}")
        self.__link = resp.url

    def original(self) -> bool:
        """
        Is this object the original creator of the shortcut?
        """
        return not self.__token == ""

    def secure(self) -> bool:
        """
        Does the destination link have a SSL certificate?
        """
        return self.__link.startswith("https")

    def empty(self) -> bool:
        """
        Does this object still contain information?
        """
        return (len(self.__link) == 0 and
                len(self.__short) == 0 and
                len(self.__token) == 0)