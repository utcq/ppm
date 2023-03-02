from pmlib.utils.colors import Colors as fg
class Log:
    def warnerror(message)->None:
        print(fg.RED+fg.BLINK+"[!]"+fg.RESET+" "+fg.RED+fg.BOLD+fg.ITALIC+message+fg.RESET)
    def info(message)->None:
        print(fg.LIGHT_GRAY+fg.ITALIC+message+fg.RESET)
    def question(message)->str:
        ine=input(f"{fg.BLUE}[{fg.GREEN}?{fg.BLUE}]{fg.RESET}  {fg.BOLD}{fg.FAINT}{fg.LIGHT_PURPLE}{message}:   {fg.RESET}{fg.ITALIC}{fg.YELLOW}"); print(fg.RESET,end='');
        return ine
    def pkgtree(root,children)->None:
        tmp=root.split("   ");tmp[1]=f"{fg.RESET}{fg.LIGHT_RED}{tmp[1]}{fg.RESET}{fg.YELLOW}"
        root='   '.join(tmp)
        tree=f"{fg.YELLOW}{fg.ITALIC}{root}"
        ic=1
        for child in children:
            if (len(children)==ic): tree+=f"\n{fg.BOLD}  └── {fg.RESET}{fg.YELLOW}{fg.FAINT}{child}{fg.RESET}{fg.YELLOW}"
            else: tree+=f"\n{fg.BOLD}  ├── {fg.RESET}{fg.YELLOW}{fg.FAINT}{child}{fg.RESET}{fg.YELLOW}"
            iic=1
            for dep in children[child]:
                if (len(children[child])==iic):
                    if (len(children)==ic): tree+=f"\n{fg.BOLD}         └── {fg.RESET}{fg.YELLOW}{fg.FAINT}{dep}{fg.RESET}{fg.YELLOW}"
                    else: tree+=f"\n{fg.BOLD}  │      └── {fg.RESET}{fg.YELLOW}{fg.FAINT}{dep}{fg.RESET}{fg.YELLOW}"
                else: 
                    if (len(children)==ic): tree+=f"\n{fg.BOLD}         ├── {fg.RESET}{fg.YELLOW}{fg.FAINT}{dep}{fg.RESET}{fg.YELLOW}"
                    else:tree+=f"\n{fg.BOLD}  │      ├── {fg.RESET}{fg.YELLOW}{fg.FAINT}{dep}{fg.RESET}{fg.YELLOW}"
                iic+=1
            ic+=1
        print(tree)
