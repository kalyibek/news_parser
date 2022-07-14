from urllib.parse import urlparse


class New:

    def __init__(self, id, date, category, title, link, desc, img):
        self.id = id
        self.date = date
        self.category = category
        self.title = title
        self.link = link
        self.desc = str(desc)
        self.img = img
        self.site_name = urlparse(link).netloc
        self.check_site_name(self.site_name)

    def __str__(self):
        return f'id: {self.id}\n' \
               f'date: {self.date},\n' \
               f'title: {self.title},\n' \
               f'link: {self.link},\n' \
               f'desc: {self.desc}\n' \
               f'img: {self.img}\n' \
               f'site_name: {self.site_name}\n'

    def check_site_name(self, site_name):
        if 'www.' in site_name:
            self.site_name = site_name[4:]
