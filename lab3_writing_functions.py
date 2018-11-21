#Zad1
def speak_excitedly(msg, expl=1,capt=False):
    x = msg + "!" * expl
    if capt == True:
        print(x.upper())
    else:
        print(x)


speak_excitedly("I love python",1)
speak_excitedly("Keyword arguments are great",4)
speak_excitedly("I guess Java is okay...",0)
speak_excitedly("let's go stanford",2,True)



#Zad2
def average(*args, sr=None):
    if args.__len__()>0:
        sr = sum(args)/args.__len__()
    print(sr)


average()
average(5)
average(6,8,9,11)



#Zad3
def make_table(key_justify='left', value_justify='right', **kwargs):

    tran = {'left':'<', 'center':'^', 'right':'>'}

    key_aligment = tran[key_justify]
    value_aligment = tran[value_justify]


    key_pad = max(map(len, kwargs.keys()))
    value_pad = max(map(len, kwargs.values()))
    full_pad = 2+key_pad+3+value_pad+2

    print("="*full_pad)
    for key, value in kwargs.items():
        print('| {:{key_aligment}{key_pad}} | {:{value_aligment}{value_pad}} |'.format(key, value,
                                                                                       key_aligment=key_aligment,
                                                                                       key_pad = key_pad,
                                                                                       value_aligment=value_aligment,
                                                                                       value_pad = value_pad))
    print("=" * full_pad)




make_table(
    first_name="Sam",
    last_name="Redmond",
    shirt_color="pink"
)

make_table(
    key_justify="right",
    value_justify="center",
    song="Style",
    artist_fullname="Taylor $wift",
    album="1989"
)