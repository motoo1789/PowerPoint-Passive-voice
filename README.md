# PowerPoint-Passive-voice

## Fix pyknp

### pyknp/knp/knp.py
jumancommand='juman'
jumanpp=False

### pyknp/juman/juman.py
command='juman'
jumanpp=False

### pyknp/utils/process.py
\# signal.signal(signal.SIGALRM, alarm_handler)
\# signal.alarm(self.process_timeout)
alarm = threading.Timer(self.process_timeout, alarm_handler)
alarm.start()

\# self.process.stdin.write(sentence.encode('utf-8'))
self.process.stdin.write(sentence.encode('cp932') + six.b('\n'))

\# line = self.process.stdout.readline().decode('utf-8').rstrip()
line = self.process.stdout.readline().rstrip().decode('cp932')

\# ignal.alarm(0)
alarm.cancel()
