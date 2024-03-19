def fullJustify(words, maxWidth):
  res = []
  cur = []
  cnt = 0

  for w in words:
    if cnt + len(w) + len(cur) > maxWidth:
      num_gaps = len(cur) - 1
      total_spaces = maxWidth - cnt
      if num_gaps == 0:
        cur[0] += ' ' * total_spaces
      else:
        base_space = total_spaces // num_gaps
        extra_space = total_spaces % num_gaps
        for i in range(num_gaps):
          cur[i] += ' ' * (base_space + (i < extra_space))
      res.append(' '.join(cur))
      cur, cnt = [], 0
    cur.append(w)
    cnt += len(w)

  if cur:
    res.append(' '.join(cur).ljust(maxWidth))

  return res


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
result_model_a = fullJustify(words, maxWidth)
print("Model A Revised Solution:")
for line in result_model_a:
  print(line)
