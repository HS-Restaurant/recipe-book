
#pip install locust

from locust import HttpUser, task, between

class User(HttpUser):

    @task
    def keyword_sim(self):
        wait_time = between(1, 2)

        self.client.get("/similarity?word1=안성기&word2=최민수")

    def on_start(self):
        print("START LOCUST")

    def on_stop(self):
        print("STOP LOCUST")

