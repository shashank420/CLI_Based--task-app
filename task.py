import sys
def help():
    x = """Usage :-
$ ./task help
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(x.encode('utf8'))

def add(p, s):
    if int(p)>=0:
        try:
            f = open('task.txt', 'r')
            fr=f.readlines()
            index=0
            for i,line in enumerate(fr):
                prio=int(line.split()[0])
                if prio>int(p):
                    break
                index+=1
            fr.insert(index,p+" "+s+"\n")
            fr="".join(fr)
        except:
            fr=p+" "+s+"\n"

        f=open('task.txt','w+')
        f.write(fr)
        f.close()
        s = '"' + s + '"'
        print(f"Added task: {s} with priority {p}")
    else:
        print("vvvvvvvvvvvvvvvvvvvvvvv")
def ls():
    try:
        file_to_format()
        for i,m in add1.items():
            sys.stdout.buffer.write(f"{i}.{m}\n".encode('utf8'))
    except Exception as e:
        raise e

def deL(no, notify = True):
    if int(no)<=0:
        print("Error: task with index #{} does not exist. Nothing deleted.".format(no))
        return
    try:
        no = int(no)
        file_to_format()
        with open("task.txt", "r+") as f:
            lines = f.readlines()
            if no>len(lines):
                raise("k")
            f.seek(0)
            for i,line in enumerate(lines):
                if i+1!=no:
                    f.write(line)
            f.truncate()
        if notify:
            print(f"Deleted task #{no}")

    except:
        print(f"Error: task with index #{no} does not exist. Nothing deleted.")
def done(no):
    try:

        file_to_format()
        no = int(no)
        f = open('completed.txt', 'a')
        st = add1[no]
        x=st.split('[')
        f.write(x[0])
        f.write("\n")
        f.close()
        print(f"Marked item as done.")
        deL(no,False)

        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            for i in lines:
                if i.strip('\n') != add1[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: no incomplete item with index #{no} exists.")

def report():
    file_to_format()
    try:
        nf = open('task.txt', 'r')
        nf1=nf.readlines()
        sys.stdout.buffer.write("Pending : {}\n".format(len(nf1)).encode('utf8'))
        for i, line in enumerate(nf1):
            line = line.split()
            sys.stdout.buffer.write("{}. {} [{}]\n".format(i+1," ".join(line[1:]),line[0]).encode('utf8'))
        nf = open('completed.txt', 'r')
        nf1=nf.readlines()
        sys.stdout.buffer.write("\nCompleted : {}\n".format(len(nf1)).encode('utf8'))
        for i, line in enumerate(nf1) :
            line = line.split()
            sys.stdout.buffer.write("{}. {}\n".format(i+1," ".join(line[:])).encode('utf8'))
    except:
        print(
            f'Pending : {len(add1)} Completed : {len(comple)}')
def file_to_format():
    try:
        f = open('task.txt', 'r')
        c = 1
        for line in f:
            pr = line.split()
            line = line.strip('\n')
            line = line + f" [{pr[0]}]"
            add1.update({c: line[1:]})
            c = c + 1
    except:
        sys.stdout.buffer.write("There are no pending tasks!\n".encode('utf8'))

if __name__ == '__main__':
    try:
        add1 = {}
        comple = {}
        args = sys.argv
        if (args[1] == 'del'):
            args[1] = 'deL'
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting tasks.".encode('utf8'))
        if (args[1] == 'add' and len(args[3:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing tasks string. Nothing added!".encode('utf8'))

        elif (args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking tasks as done.".encode('utf8'))

        elif (args[1] == 'del' and len(args[3:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting todo.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])

    except Exception as e:

        x1 = """Usage :-
$ ./task help
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
        sys.stdout.buffer.write(x1.encode('utf8'))
