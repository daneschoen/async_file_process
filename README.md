# Async File Processing

## Making File IO Faster 

File IO operations, such as reading and writing files, would normally employ a serial procedure in nature. 
This blocks IO, which would be acceptable for small file sizes and low number of files.
However when either of these get large, each file operation would have to wait for the others to 
complete before each are able to make progress.

One way to improve upon serial coding is to employ Python's asyncio module.
However this does not support asynchronous file IO operations. There is a reason for this: 
it is actually recommended to use multithreading for IO blocking situations. 

The aiofiles library actually employs a thread pool under the hood. So why would one want to use 
aiofiles? For its async syntax, which looks closer to synchronous code than threading does.
In addition it corresponds nicely with other async code that may exist for example if you are using FastAPI.

## Async and Pandas

What if you want to use Pandas? Pandas does not have async capability so Python's threading paradigm is needed. But fear not! 
Python's concurrent framework has got you covered so that you don't have to muck about with semaphores,
critical sections, race conditions, etc. Python makes the complex easy, which is what makes Python
so great and powerful!

