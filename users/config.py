class SiteConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SiteConfig, cls).__new__(cls)
            cls._instance.article_limit = 10
            cls._instance.allowed_file_types = ['jpg', 'png', 'mp4', 'mp3']
        return cls._instance
