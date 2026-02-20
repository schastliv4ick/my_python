l = input().lower().split(' ')
cnt = {}
m_c = 0
m_w = ""

for word in l:
    if word not in cnt.keys():
        cnt[word] = 1
    else:
        cnt[word] += 1
    if cnt[word] > m_c:
        m_c, m_w = cnt[word], word

print(m_w, m_c)