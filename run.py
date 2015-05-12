import re
log = open("sample_log")
log_depurado = []
keys = ['datetime', 'severity', 'resource', 'server', 'message']
for line in log.readlines():
  line = line.replace('  ', ' ')
  log_depurado.append(dict(zip(keys,line.split(' ', 4))))

print log_depurado[0]
