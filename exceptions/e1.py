# class AnimeshError(Exception) :
#     def __init__(self, msg='hii you got an error'):
#         self.msg=msg
#         super().__init__(msg)

# a=10
# b=4
# try:
#     print(a/b)
#     try:
#         x=10
#         if x<90:
#             raise AnimeshError()
#     except Exception as e:
#         print(f'Exception is {e}')
# except ZeroDivisionError as e: # executed only when cache is came from try block
#     print('cant divided by 0')
# else:# will be executed while no exception done
#     print('hiiiiii')
# finally:# willl be executed if or not if error occured
#     print('I am finally')


try:
    a=10
    b=2

    print(a/b)
    l=[1,2,3]
    print(l[1])
    str=int('Animesh')
    print(str)

except ZeroDivisionError:
    print('zero division not possible')
except ValueError:
    print('not  parsing')
except IndexError:
    print('cant access the index')
except Exception as e:
    print(e)



