# Channels 
- Channel is a complex , thread safe data structure managed by go runtime.
- Channels are the pipeline which are used to transfer data from different goroutines. 
- The transfer is via references instead of values. 
- GO is concurrent i.e.. it uses parallel process to help execute programs faster. 
- The 'go' keyword is used to use the concurrent processing. 
- the data is transfered in FIFO manner.

## Creating a channel
- Use make to create buffered or unbuffered channels. 
```go 
ch := make(chan int) // for unbuffered channel
ch2 := make(chan int, n int)  // for buffered channel.
```

## What are buffered and unbuffered channel?
### Buffered:
- If we use a buffer channel , there is a predefined array inside it, but it's managed as a circular queue. This is where the data sits. 
- can be created by defining the length of the array while creating the channel as shown above.
- The buffer channel will not hold up the process till the process is finished on all the objects are filled in the array.
### Un-buffered : 
- No need to predifine the length the array.
- Waits for the receiver to receive the data before moving onto the next data.

## Pros of Channel : 
A. Mutex lock : Because the goroutines can touch a channel at once , the channel has a built in lock to ensure only one goroutine can access the channel at once. 
B. Waiting Queues: A list of goroutines wait to send data , and a list of goroutines wait to receive data.

## Sending data through the channel
```go 
ch :=make(chan bool,2)
```
- send data : 
```go 
ch<-true
```

- receive data : 
```go 
v:=<-ch
```
