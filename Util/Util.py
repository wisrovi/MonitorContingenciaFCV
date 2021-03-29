class Util(object):
    import base64

    def decoBase64UrlSafe(self, s):
        return self.base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))
