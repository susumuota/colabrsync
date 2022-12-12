# SPDX-FileCopyrightText: 2022 Susumu OTA <1632335+susumuota@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT

from colabrsync import RsyncMirror

def test_rsyncmirror():
  mirror = RsyncMirror('/tmp/src', '/tmp/dst')
  assert mirror.command == 'rsync -aq --log-file /tmp/rsync.log /tmp/src /tmp/dst'
  assert mirror.process
  assert mirror.process.args == 'while true ; do rsync -aq --log-file /tmp/rsync.log /tmp/src /tmp/dst ; sleep 60 ; done'
