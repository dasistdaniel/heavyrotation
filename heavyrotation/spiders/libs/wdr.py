class playlist():
    def __init__(self, data):
        self.data = data
        self.playlist = []
        print data.css('title::text').extract()
