# Async File Processing

## Making File IO Faster 

File IO operations, such as reading and writing files, would normally employ a procedure 
that is serial in nature. This blocks IO - each file operation has to wait for other 
operations to complete before making progress themselves.

One way to improve upon serial coding is to employ Python's asyncio module.
However this does not support asynchronous file IO operations. The reason for this 
is because it is actually recommended to use multithreading for IO blocking. 

The aiofiles library actually employs a thread pool under the hood. So why would one want to use 
aiofiles? For its async syntax, which looking closer to serial syntax than threading 
would. Another reason it corresponds nicely with other async code that may exist 
for example in FastAPI.


## Async and Pandas

Pandas does not have async capability so Python's threading paradigm is needed. But fear not! 
Python's async framework has got you covered so you don't have to muck about with semaphores,
critical sections, race conditions, etc. Python makes the complex easy, which is what makes Python
so great and powerful!

