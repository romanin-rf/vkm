
# ! Base Client Class
class Client:
    def __init__(
        self,
        user_agent: str,
        client_id: str,
        client_secret: str
    ) -> None:
        self.user_agent = user_agent
        self.client_id = client_id
        self.client_secret = client_secret

# ! Clients Vars
KateMobile = Client(
    user_agent='KateMobileAndroid/56 lite-460 (Android 4.4.2; SDK 19; x86; unknown Android SDK built for x86; en)',
    client_id='2685278',
    client_secret='lxhD8OD7dMsqtXIm5IUY'
)

# ! Main Vars
clients = {
    'Kate': KateMobile
}
