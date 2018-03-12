class playlist():
    def __init__(self):
        self.iteratorType = "css"
        self.iteratorSearch = "#searchPlaylistResult table tbody tr"
        
        self.dateType = "xpath"
        self.dateSearch = "th/text()[1]"
        
        self.timeType = "xpath"
        self.timeSearch = "th/text()[2]"
        
        self.iterator = {'Type': 'css', 'Search': '#searchPlaylistResult table tbody tr'} 
        self.date     = {'Type': 'xpath', 'Search': 'translate(th/text()[1], ",", "")'} 
        self.time     = {'Type': 'xpath', 'Search': 'translate(substring-before(th/text()[2]," Uhr"),".", ":")'} 
        self.artist   = {'Type': 'xpath', 'Search': 'normalize-space(td[2]/text())'} 
        self.title    = {'Type': 'xpath', 'Search': 'normalize-space(td[1]/text())'} 
