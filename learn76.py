import itchat
hotReload = True
itchat.auto_login()

friends = itchat.get_friends()
# print(friends)
info = {}
for friend in friends[1:]:
    if friends['Sex'] == 1:
        info['male'] = info.get('male',0) + 1
    elif friends['Sex'] == 2:
        info['female'] = info.get('female',0) + 1
    else:
        info['other'] = info.get('other',0) + 1
print(info)