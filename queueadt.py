import queue
import random
q=queue.Queue(maxsize=10)
for v in range(0,5):
    q.put((random.random()*100))
print("queue size:",q.qsize())
for v in range(0,5):
    print(v,"value remove from queue:",q.get())
print("queue size:",q.qsize())
print("queue is empty:",q.empty())
print("queue is full:",q.full())
for v in range(0,10):
    q.put((random.random()*100))
print("queue is full:",q.full())
print("queue is empty:",q.empty())
for v in range(0,10):
    print(v,"value remove from queue:",q.get())
