def front_back(str):
    if len(str) >= 2:
        return str[-1] + str[1:-1] + str[0]
    else:
        return str


print(front_back("code"))
print(front_back("ab"))
print(front_back("a"))
