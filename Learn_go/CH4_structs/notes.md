# Why Golang ? 
It creates machine readable code. So you just have to compile once and then that code can be used on any machine regardless it has go installed or not. 

#### How is it better than JS or Python ? Why should we choose it over these ? 

## Structs

### What is struct? 
Struct (structure in short) is a custom data type which we can use to define combination of datatypes for our program. For example : 
```go
type car struct{
    wheels int
    colour string
}
``` 
To use these struct, dot notation is used.


### Nested Struct
A nested struct is a struct inside another struct. For example: 
```go
type car struct{
    frontwheel wheel 
    backwheel wheel
    colour string
    engine string
}

type wheel struct{
    radius int 
    material string
}

myCar := car{}
myCar.frontWheel.radius = 5
```

### Anonymus structs 
Anonymus structs are used when the struct will only be used once or in a limit. These structs are created instantly and used instantly. 
For example : 
```go
myVisorColor:= struct{
   color string 

}{
    color: "Green"
}

```


### Embeded Structs
Embeded struct are used to embedd structs and their fields can be used at the top level like normal fields.
For example: 
```go
type car struct{
    brand string,
    model string
}

type truck struct{
    bedSize int
    car

}

myTruck := truck{
    bedSize : 10,
    car:car{
    brand : "Toyota",
    model : "L1"
},
}
fmt.Println(myTruck.brand)
fmt.Println(myTruck.model)
```
### Memory Layout in structs
Structs should be layed out from descending order of memory to avoid bad memory layot and left over space between the datatypes.

for example : 
```go
type car struct{
    model string
    wheels int16
}
```
### Something interesting i came accross : 
When we store sting the memory is distributed as : 
1. Header : is a small struct that stays on the stack and describes where the string data is:
- On 64 bit system : 8 byte for pointer + 8 byte for the length of string
- On 32 bit system : 4 byte for pointer + 4 byte for the length of string

2. Backing Array:
Backing array is the array where the stirng characters are store. Go uses UTF-8 by default to store the ascii and non ascii characters.
- Ascii character takes 1 byte or 8 bit per character in the array. 
- Non ascii character takes 2 to 3 bytes each.
- Emojis take upto 4 bytes each.

### The big brain :
Let say we save name := "garvit"
Under the hood the variable 'name' is 16-byte header (on 64-bit)
the data (backing array) is sitting elsewhere in the memory and the header is just pointing to that memory.
So the struct of the header will be:
```go
type StringHeader struct{

    PointerToBytes  uintpr  // 8 bytes pointer
    LengthToBytes   int     // 8 bytes
}
```
so wherever you are using the 'name' , we are using the header which is pointing to the memory where the backing array is. So go effectively only copies the header and not the backing array. This is the reason go passes long sting fast.
