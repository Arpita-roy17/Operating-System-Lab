import os

print("Before Fork")
print("Current PID:", os.getpid())

pid = os.fork()

if pid == 0:
    print("\nChild Process")
    print("Child PID :", os.getpid())
    print("Parent PID:", os.getpid())

else:
    os.wait()

    print("\nParent Process")
    print("Parent PID:", os.getpid())
    print("Child PID :", pid)

# Before fork():
# Parent (PID = 2500)

# After fork():
# Parent PID = 2500 --> Child PID = 2501
#             Child PPID = 2500