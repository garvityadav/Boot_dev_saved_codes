# Packages 
Every go program is made up of packages. 
A package is a directory of go code that's all compiled together. 
```go
package main
```

main package is the entry point of the main() function. A main package is compiled into an executable program.
- A package by any other name is called as library package.

## Directory as a package. 
Go has one rule : **One Directory , One Package**. 
```go
|---  utils/
|     |--- math.go
|     |--- strings.go
|     |--- helper.go
```

The above all will be under one package name , "utils".
If we want to create a seperate package , we put the .go files under different directory. 
```go
|--- myapp/
|     |--- main.go          // package main
|     |--- server/          
|     |     |--- server.go  // package server
```

## Modules 
Modules are collection of go packages that are released together. 
- A file named go.mod will be at the root of the project. It declares the module. It contains:
1. Module path. 
2. the version of go language required for the program. 
3. Optinally, any external repo/package used in the program.

# Go build & Go run

- to make the module executable in any machine => go build. Go run 
- to temp run the module => go run

## Clean Packages
Functions names starting with a lowercase letter are unexported and private to the package,while the functions with uppercase letters are exported and can be accessed extrernally.
- Don't export functions from the main package. 
- a package should never know anything about it's dependents. In other words , a package should never have specific knowledge about a partcular application that uses it.
