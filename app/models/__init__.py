class ModelBase:
    def update(self, data, not_update=[]):
        for key, value in data.items():
            if key in not_update:
                continue
            setattr(self, key, value)