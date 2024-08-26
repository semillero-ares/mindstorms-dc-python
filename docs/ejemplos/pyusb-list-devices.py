import usb.core

d = usb.core.find(find_all=1)
print(list(d))
