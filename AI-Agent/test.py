from functions.get_files_info import get_files_info

def test():
    result = get_files_info("calculator",".")
    print("Result for current directory:")
    print(result) 
    print("")

    result = get_files_info("calculator","pkg")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator","/bin")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator","../")
    print("Result for current directory:")
    print(result)
    print("")
