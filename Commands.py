class Commands:

    def __init__(self, boat: [], start_coast: [], finish_coast: [], move_yn: str):
        self.boat: [] = boat
        self.start_coast: [] = start_coast
        self.finish_coast: [] = finish_coast
        self.move_yn: str = move_yn

    def take(self, object):
        if not self.boat:
            if self.move_yn == 'start':
                self.start_coast.remove(object)
                self.boat.append(object)
            elif self.move_yn == 'finish':
                self.finish_coast.remove(object)
                self.boat.append(object)

    def put(self, object):
        if self.boat:
            if self.move_yn == 'start':
                self.start_coast.append(object)
                self.boat.remove(object)
            elif self.move_yn == 'finish':
                self.finish_coast.append(object)
                self.boat.remove(object)

    def move(self):
        if self.move_yn == 'start':
            return 'finish'
        elif self.move_yn == 'finish':
            return 'start'

