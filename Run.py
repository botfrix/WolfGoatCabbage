from Commands import Commands


class Run:

    def __init__(self, boat: [], start_coast: [], finish_coast: [], move_yn: str):
        self.boat: [] = boat
        self.start_coast: [] = start_coast
        self.finish_coast: [] = finish_coast
        self.move_yn: str = move_yn

    def run(self, action, beast):
        c = Commands(self.boat, self.start_coast, self.finish_coast, self.move_yn)
        if action == 'take':
            if not beast:
                raise Exception(f'Command {action} has no object')
            c.take(beast)
            print(f'DELETE {beast} from Start Coast\nADD {beast} to Boat')
        elif action == 'put':
            if not beast:
                raise Exception(f'Command {action} has no object')
            c.put(beast)
            print(f'DELETE {beast} from Boat\nADD {beast} to Finish Coast')
        elif action == 'move':
            self.move_yn = c.move()
            print(f'Boat MOVES to another Coast')
        else:
            raise Exception(f'Command {action} not found')
        return self.move_yn
