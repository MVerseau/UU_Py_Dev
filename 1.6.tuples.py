immutable_var=(1,3,5,'string', True)
print(immutable_var)
#immutable_var[0]='string2' Нельзя выполнить операцию, т.к. кортеж не поддерживает изменения своих элементов

mutable_list=[2,4,6,'blabla', 'what ever']
mutable_list[1]='I can change the element'
print(mutable_list)
