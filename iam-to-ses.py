#!/usr/bin/env python

from __future__ import print_function

import base64
import hashlib
import hmac
import sys


MESSAGE = b'SendRawEmail'


def get_ses_password(iam_secret):
    sig = hmac.new(
        key = iam_secret,
        msg = MESSAGE,
        digestmod=hashlib.sha256,
    ).digest()

    return base64.b64encode(b'\x02' + sig)


def main():
    print(get_ses_password(sys.argv[1]))


if __name__ == '__main__':
    main()
