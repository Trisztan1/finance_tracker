import time, random

class ID:
    @staticmethod
    def generate_timestamp_id() -> str:
        return f"{int(time.time()*1000)}_{random.randint(1000, 9999)}_{random.randint(1000, 9999)}"