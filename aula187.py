import _thread

def filho(tid):
    print('Ola da thread',tid)

def pai():
    i = 0
    while True:
        i += 0
        _thread.start_new_thread(filho,(i,))
        if input() == 'q': break

pai()

