# SPDX-FileCopyrightText: 2022 Susumu OTA <1632335+susumuota@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

import colabrsync
from colabrsync import __version__, RsyncMirror

def test_version():
  assert __version__ == '0.2.0'

def test_rsyncmirror():
  mirror = RsyncMirror('/tmp/src', '/tmp/dst')
  assert mirror.command == 'rsync -aq --log-file /tmp/rsync.log /tmp/src /tmp/dst'
  assert mirror.process
  assert mirror.process.pid
  assert mirror.process.returncode == None
  assert mirror.process.args == 'while true ; do rsync -aq --log-file /tmp/rsync.log /tmp/src /tmp/dst ; sleep 60 ; done'
