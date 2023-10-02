from locust import HttpUser, task


class LoadTest(HttpUser):

    def on_start(self):
        self.login()

    def login(self):
        response = self.client.post(
            '/authentication/token/',
            {
                'username': 'root',
                'password': '09106850351'
            }
        )
        content = response.json()
        access_token = content['access']
        self.client.headers = {'Authorization': f"Bearer {access_token}"}

    @task(1)
    def get_products(self):
        self.client.get('/product-management/products')

    # @task(2)
    # def get_users(self):
    #     self.client.get('/user-management/users')
