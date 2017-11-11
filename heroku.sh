#!/bin/bash
# This is a temp workaround file to get the worker and web process running
# on a single dyno, which is not recommended but allows us to do this on the
# free heroku plan
gunicorn app:app --daemon
python worker.py