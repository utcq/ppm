from pmlib.utils.colors import Colors as fg


                                                                                              #####################
                                                                                                                                              #########################
help_str=f"""{fg.BOLD + fg.LIGHT_PURPLE}                                ─[ HELP ]─{fg.RESET}
{fg.BLUE}┌──────────────────────────────────────────────────────────────────────────┐{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}help   {fg.RESET}      :  {fg.CYAN}Shows commands help{fg.RESET}                                     {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}init   {fg.RESET}      :  {fg.CYAN}Initialize the project{fg.RESET}                                  {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}ls   {fg.RESET}        :  {fg.CYAN}List project dependencies {fg.RESET}                              {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}run (1){fg.RESET}      :  {fg.CYAN}Run Project script{fg.RESET}                                      {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}start  {fg.RESET}      :  {fg.CYAN}Run start script{fg.RESET}                                        {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}test  {fg.RESET}       :  {fg.CYAN}Run test script{fg.RESET}                                         {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}build  {fg.RESET}      :  {fg.CYAN}Run build script{fg.RESET}                                        {fg.BLUE}│{fg.RESET}
{fg.BLUE}│{fg.RESET}  {fg.GREEN}{fg.BOLD}install [1]  {fg.RESET}:  {fg.CYAN}Install a package or install all the packages{fg.RESET}           {fg.BLUE}│{fg.RESET}
{fg.BLUE}└──────────────────────────────────────────────────────────────────────────┘{fg.RESET}"""

no_arg="No cli argument provided"
help_sugg=fg.FAINT+"Use "+fg.RESET+fg.LIGHT_GRAY+fg.NEGATIVE+"help"+fg.RESET+fg.LIGHT_GRAY+fg.ITALIC+fg.FAINT+" for info"


frameworks=[
    'flask',
    'fastapi',
    'django',
    'pyunit'
]

framework_deps={
    "flask": [
        'flask'
    ],
    'fastapi': [
        'fastapi'
    ],
    'django': [
        'django'
    ],
    'pyunit': [
        'pyunit'
    ]
}
