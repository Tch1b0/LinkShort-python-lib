import unittest
import requests
import requests_mock
import LinkShort

url = "https://ls.johannespour.de/"

class TestLinker(unittest.TestCase):
    def test_create(self):
        with requests_mock.Mocker() as m:
            m.post(f"{url}create", json={"short": "1234", "token": "4321"})
            self.assertTrue(isinstance(LinkShort.Linker.create("https://example.com"), LinkShort.Linker))

    def test_edit(self):
        with requests_mock.Mocker() as m:
            m.put(f"{url}")
            example = "https://example.com"
            l = LinkShort.Linker(example, "1234", "4321")
            l.edit("https://another.example.com")
            self.assertTrue(l.link != example)

    def test_delete(self):
        with requests_mock.Mocker() as m:
            m.delete(f"{url}")
            l = LinkShort.Linker("https://example.com", "1234", "4321")
            l.delete()

    def test_original(self):
        with requests_mock.Mocker() as m:
            m.post(f"{url}create", json={"short": "1234"})
            
            l = LinkShort.Linker.create("https://example.com")

            self.assertFalse(l.original())

            m.post(f"{url}create", json={"short": "1234", "token": "4321"})

            l = LinkShort.Linker.create("https://example.com")

            self.assertTrue(l.original())

    def test_secure(self):
        with requests_mock.Mocker() as m:
            m.post(f"{url}create", json={"short": "1234"})
            
            l = LinkShort.Linker.create("http://example.com")

            self.assertFalse(l.secure())

            m.post(f"{url}create", json={"short": "1234", "token": "4321"})

            l = LinkShort.Linker.create("https://example.com")

            self.assertTrue(l.secure())

unittest.main()