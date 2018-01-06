txt = input("Enter some text: ")
start_idx = 0;
end_idx = 0;
n = txt.count(" ") + 1
txt = txt.replace("Carlton", "Chutia")
for i in range(n):
    end_idx = txt.find(" ", start_idx)
    #print("Start index: ", start_idx)
    #print("End index: ", end_idx)
    if i != (n-1):
        word = txt[start_idx:end_idx+1]
    else:
        word = txt[start_idx:]
    start_idx = end_idx+1
    print(word)
