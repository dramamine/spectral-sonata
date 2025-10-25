import subprocess
import signal

external_python = r'C:\Python311\python.exe'
def start_process():
  global process
  process = subprocess.Popen([external_python, '../bridge/artnet-to-serial-sender.py'])
  return

