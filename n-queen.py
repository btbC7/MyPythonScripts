#! python3

#n-Queen
#recursive
#backtracking

a=0

def output_str( n, s ):
    global a
    a = a+1
    print( "No{}: ".format( a ), end='' )

    for i in range( n ):
        print( "({},{})".format( s[i*2], s[i*2+1] ), end='' )
    return print()

def n_queen( n, s ):
    for i in range( n ):
        for j in range( i+1, n ):
            if s[i*2+1]==s[j*2+1] or abs( int( s[i*2] ) - int( s[j*2] ) ) == abs( int( s[i*2+1] ) - int( s[j*2+1] ) ):
                return False
    return True

def backtracking( n, m, s ):
    if n_queen( m, s )==False:
        return
    return search( n, m+1, s )

def search( n, m, l ):
    if n<m:
        if n_queen( n, l )==True:
            return output_str( n,l )
        return
    for i in range( n ):
        o = l
        o = o + str( m ) + str( (i+1) )
#        search( n, m+1, o )
        backtracking( n, m, o )
        

print( "This is a program to solve the N Queen" )
n = int( input( "Input height( 4 or more positive number ) >> " ) )
search( n, 1, '' )    #The second and third argument is initial value
