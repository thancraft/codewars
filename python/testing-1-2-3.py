## Best Practices ##
# 1.
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# 2.
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# 3.
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]
