def test_function(ar1 = 'default a1 value', ar2 = 'devault ar2 value'):
    print ar1
    print ar2


# test_function(ar2 = 123)



def func2( *args, **kwargs):
    #print str(abcargs)
    print str(kwargs)#abcargs['a']
    print "-------------------"
    print str(args)


func2(1, 2,3,3,4,b=5,c=7,"Fsdf")
