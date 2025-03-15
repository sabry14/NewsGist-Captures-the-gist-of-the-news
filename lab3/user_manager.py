import json
import os

USER_DATA_FILE = "userPrefrence.json"

class UserManager:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        """Loads user preferences and history from JSON."""
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, "r") as file:
                return json.load(file)
        return {"preferences": [], "history": []}

    def save_data(self):
        """Saves user preferences and history to JSON."""
        with open(USER_DATA_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_preference(self, topic):
        """Adds a new topic preference."""
        if topic not in self.data["preferences"]:
            self.data["preferences"].append(topic)
            self.save_data()

    def add_search_history(self, topic):
        """Logs search history."""
        self.data["history"].append({"topic": topic})
        self.save_data()

