class Vegetable:
    def __init__(self, name, price, ready, url):
        self._name = name
        self._price = price
        self.ready_time = ready
        self._img = url
#Properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, vname):
        self._name = vname
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, number):
        self._price = number

    @property
    def readytime(self):
        return self.ready_time
    
    @readytime.setter
    def readytime(self,period):
        self.ready_time = period

    @property
    def img(self):
        return self._img

# Methods
    def is_self(self, name):
        if name == self._name:
            return True
        else:
            return False


class Farm:
    def __init__(self, name, dist, rating):
        self._name = name
        self._dist = dist
        self._rating = rating
        self.prod_dict = {}
    
    #Properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, text):
        self._name = text

    @property
    def dist(self):
        return self._dist
    
    @dist.setter
    def dist(self, value):
        self._dist = value
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, number):
        self._rating = number

    #Methods
    def create_prod(self, vname, vprice, vready, url):
        return Vegetable(vname, vprice, vready, url)
        
    def add_prod(self, vname, vprice, vready, url):
        if vname not in self.prod_dict:
            veg = self.create_prod(vname, vprice, vready, url)
            self.prod_dict[veg._name] = veg
    
    def get_prod(self, vname):
        return self.prod_dict.get(vname)
    
    def get_prod_list(self):
        return self.prod_dict.keys()
    
    def __contains__(self, val):
        return val in self.prod_dict.keys()
    
product_data_a = {
    "Nama Produk": ["Bayam", "Wortel", "Tomat", "Kentang"],
    "Harga (Rp)": [5000, 7000, 8000, 10000],
    "Ready": ["Sekarang", "Sekarang", "Dalam 2 bulan", "Dalam 1 bulan"],
    "Gambar": [
        "https://akcdn.detik.net.id/visual/2018/07/11/cc01493c-6a04-4bea-b33d-3be0086c9f09_169.jpeg?w=650",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3zWb4BCP-FZVsUZFWPvjfXktU6PEYutg1UA&s",
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1629681328/attached_image/9-manfaat-tomat-buah-yang-disangka-sayur.jpg",
        "https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/03/30033712/Tak-Hanya-Meningkatkan-Fungsi-Otak-Ini-11-Manfaat-kentang-untuk-Kesehatan.jpg.webp",
    ],
}
a = Farm("Farm A", '1.0 km', 4.8)
for idx in range(0,4):
    names = product_data_a['Nama Produk']
    prices = product_data_a["Harga (Rp)"]
    ready = product_data_a["Ready"]
    urls = product_data_a["Gambar"]
    a.add_prod(names[idx], prices[idx], ready[idx], urls[idx])

