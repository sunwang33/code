__author__ = "sun wang"
python_class01 = ['sunwang','john','lilei']
linux_class02 = ['tom','jerry','lilei']
for p_name01 in python_class01:
    if p_name01 in linux_class02:
        linux_class02.remove(p_name01)
python_class01.extend(linux_class02)
print(python_class01)

