__all__ = ["Move", "Look", "Get", "Quit", "Use", "Drop", "Command", "details", "wait_for_enter"]


def details(prompt, validList):
    detail = ""
    while detail not in validList:
        print "\nYour choices:"
        for itemName in validList:
            print "\t", itemName
        detail = raw_input(prompt)
    return detail


def wait_for_enter():
    raw_input("\n\nHit enter to continue")


class Command(object):
    """Base Class for Pyventure Commands"""
    def __init__(self, name, game, function, **checkList):
        super(Command, self).__init__()
        self.name = name
        self.game = game
        self.function = function
        self.checkList = checkList

    def do(self, *arguments):
        for condition, test in self.checkList:
            if not test(*arguments):
                return condition
        self.function(*arguments)
        return ""


class Move(Command):
    """ move around """
    def __init__(self, game):
        super(Move, self).__init__("move", game, self.move)

    def move(self):
        self.game.direction = details("\nWhich direction would you like to go?: ", self.game.map.validDirections(self.game.currentRoom))
        self.game.changeRoom()


class Look(Command):
    """ find hidden items """
    def __init__(self, game):
        super(Look, self).__init__("look", game, self.look)

    def look(self):
        self.game.rooms[self.game.currentRoom].look()
        wait_for_enter()


class Get(Command):
    """Get items"""
    def __init__(self, game):
        super(Get, self).__init__("get", game, self.get)

    def get(self):
        room = self.game.rooms[self.game.currentRoom]
        if room.searched and len(room.items) > 0:
            itemNames = []
            for item in room.items:
                itemNames.append(item.name)
            getItem = details("\nWhich thing would you like to get? ", itemNames)

            self.game.player.addToInventory(room.takeItem(getItem))
            print "\nYou got the", getItem, "!\n"
            wait_for_enter()


class Use(Command):
    """Use items"""
    def __init__(self, game):
        super(Use, self).__init__("use", game, self.use)

    def use(self):
        if len(self.game.player.inventory):
            item = details("\nWhich item do you want to use? ", self.game.player.inventory.keys() + ['nothing'])
            if item != "nothing":
                self.game.player.use(item)
                self.game.rooms[self.game.currentRoom].use(item)
            wait_for_enter()


class Drop(Command):
    """Drop items"""
    def __init__(self, game):
        super(Drop, self).__init__("drop", game, self.drop)

    def drop(self, itemName=""):
        if itemName not in self.game.player.inventory.keys() and len(self.game.player.inventory):
            itemName = details("\nWhat would you like to drop? ", self.game.player.inventory.keys() + ['nothing'])
        if itemName != "nothing":
            item = self.game.player.drop(itemName)
            if item:
                self.game.rooms[self.game.currentRoom].items.append(item)


class Quit(Command):
    """Quit game"""
    def __init__(self, game):
        super(Quit, self).__init__("quit", game, self.quit)

    def quit(self):
        pass
