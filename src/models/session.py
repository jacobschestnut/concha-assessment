class Session():
    def __init__(self, id, userId, selected_tick, step_count):
        self.id = id
        self.userId = userId
        self.selected_tick = selected_tick
        self.step_count = step_count
        self.ticks = None