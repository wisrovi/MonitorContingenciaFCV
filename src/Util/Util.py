class Util(object):
    import base64

    def decoBase64UrlSafe(self, s):
        return self.base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))

    def decodeBase64(self, s):
        return self.base64.b64decode(s)


if __name__ == '__main__':
    util = Util()
    msn = "aG9sYQ=="
    print(len(msn))
    a = util.decodeBase64(msn).decode('utf-8')
    print(a)