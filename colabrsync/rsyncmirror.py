# SPDX-FileCopyrightText: 2022 Susumu OTA <1632335+susumuota@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

from shlex import quote
from subprocess import Popen, run

class RsyncMirror:
  def __init__(self, src, dst, log='/tmp/rsync.log', sleep_seconds=60):
    self.command = f'rsync -aq --log-file {quote(log)} {quote(src)} {quote(dst)}'
    self.process = Popen(f'while true ; do {self.command} ; sleep {quote(str(sleep_seconds))} ; done', shell=True)
  def __del__(self):
    self.process.terminate()
    run(self.command, shell=True)
